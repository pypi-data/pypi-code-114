import importlib
import os
import sys
from pathlib import Path

import autodl
from click import ClickException

sys.path.append(os.getcwd())


def analyze_pytorch_source(model_file_path):
    # spec = importlib.util.spec_from_file_location("model", model_file_path)
    # module = importlib.util.module_from_spec(spec)
    # spec.loader.exec_module(module)
    args = sys.argv
    sys.argv = [args[0]]
    importlib.import_module(
        model_file_path[:-3]
    )  # TODO relative imports not working
    sys.argv = args
    # exec(open(model_file_path).read(), {})
    models = autodl.attached_models

    if len(models) < 1:
        # TODO try to manually find the model without autodl attachments
        raise ClickException(
            "The provided model file does not contain any models attached with `autodl.attach_model`.\n"
            + "Please refer to our documentation to read on how to attached your models."
        )
    if len(models) > 1:
        raise ClickException(
            "Our current CLI implementation does not support multiple models in one file yet. Please contact us and file an inquiry to add this feature if you need it."
        )

    model, dummy_input, interns, externs, max_search_depth = models[0]
    model_file_bytes = autodl.export_pytorch_model_repr(
        model, dummy_input, interns, externs, max_search_depth
    )

    return model_file_bytes, dummy_input


def load_tensorflow_protobuf(model_file_path):
    import tensorflow.compat.v1 as tf
    from google.protobuf.message import DecodeError
    from tensorflow.core.protobuf import saved_model_pb2
    from tensorflow.python.platform import gfile
    from tensorflow.python.util import compat

    graph_def = tf.GraphDef()

    with tf.Session() as sess:
        try:
            # this load method cannot load models from https://tfhub.dev/
            # crashes with `google.protobuf.message.DecodeError: Error parsing message with type 'tensorflow.GraphDef'`

            with tf.gfile.GFile(model_file_path, "rb") as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())

                return [n for n in graph_def.node]

        except DecodeError:
            # this load method cannot load models from @marcink
            # nasnet is missing input dimensions
            # posenet is missing meta_graphs - crashes with `IndexError: list index (0) out of range` on tf.import_graph_def(sm.meta_graphs[0].graph_def)
            with gfile.GFile(model_file_path, "rb") as f:
                data = compat.as_bytes(f.read())
                sm = saved_model_pb2.SavedModel()
                sm.ParseFromString(data)
                tf.import_graph_def(sm.meta_graphs[0].graph_def)
                return [n for n in sm.meta_graphs[0].graph_def.node]


def infer_tensorflow_protobuf_input_shape(model_file_path):
    graph_nodes = load_tensorflow_protobuf(model_file_path)
    inferred_batch_size, inferred_width, inferred_height, inferred_channels = (
        None,
        None,
        None,
        None,
    )

    for node in graph_nodes:
        if node.op == "Placeholder":
            shape_proto = node.attr["shape"]
            dim_sizes = [dim.size for dim in shape_proto.shape.dim]
            print("Detected input layer with shape", dim_sizes)
            dim_sizes += [None, None, None, None]
            dim_sizes = dim_sizes[0:4]
            dim_sizes = [None if size == -1 else size for size in dim_sizes]

            if len(shape_proto.shape.dim) > 0:
                [
                    inferred_batch_size,
                    inferred_width,
                    inferred_height,
                    inferred_channels,
                ] = dim_sizes

    return (
        inferred_batch_size,
        inferred_width,
        inferred_height,
        inferred_channels,
    )


def analyze_model_file(model_file_path):
    extension = "".join(Path(model_file_path).suffixes)

    output = None, None, None, None, None, None, None, None
    (
        model_file,
        inferred_model_name,
        framework,
        inferred_quantization,
        inferred_channels,
        inferred_width,
        inferred_height,
        inferred_batch_size,
    ) = output

    model_file = model_file_path
    inferred_model_name = Path(model_file_path).stem
    inferred_quantization = "FP32"

    if extension in [".py"]:
        framework = "PYTORCH"
        model_file, dummy_input = analyze_pytorch_source(model_file_path)
        [
            inferred_batch_size,
            inferred_channels,
            inferred_width,
            inferred_height,
        ] = dummy_input.shape

    if extension in [".mar"]:
        framework = "PYTORCH"
        # TODO analyze .mar file for input shape

    if extension in [".pb"]:
        framework = "TENSORFLOW"

        [
            inferred_batch_size,
            inferred_width,
            inferred_height,
            inferred_channels,
        ] = infer_tensorflow_protobuf_input_shape(model_file_path)

    if extension in [
        ".tflite"
    ]:  # TODO - add this extension also to the UI autofiller
        framework = "TFLITE"
        raise ClickException(f"Files with '{extension}' are not supported yet")

    if extension in [".pt", ".pth"]:
        raise ClickException(f"Files with '{extension}' are not supported")

    return (
        model_file,
        inferred_model_name,
        framework,
        inferred_quantization,
        inferred_channels,
        inferred_width,
        inferred_height,
        inferred_batch_size,
    )
