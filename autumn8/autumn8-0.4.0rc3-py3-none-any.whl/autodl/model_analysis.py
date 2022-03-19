import json
from inspect import signature

import torch
import torchvision


class LayerConfig(object):
    params = list()
    name = None

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()


# example message: mat1 and mat2 shapes cannot be multiplied (1x576 and 1000x500)
# we want to get 576 and 1000 from this example
def extract_inner_dimensions(message):
    firstIntIndex = message.find("x") + 1
    firstIntIndexEnd = message.find(" ", firstIntIndex)
    first = int(message[firstIntIndex:firstIntIndexEnd])

    secondIntIndex = firstIntIndexEnd + len(" and ")
    secondIntIndexEnd = message.find("x", secondIntIndex)
    second = int(message[secondIntIndex:secondIntIndexEnd])

    return first, second


def try_infer_input_shape(model, batch_size):
    sig = signature(model.forward)
    print(sig)
    input_signature = [1, 1]
    tries = 0
    ok = False
    previousMessage = None
    min_size = 1
    max_size = None

    while not ok and tries < 20:
        print(input_signature)
        dummy_input = torch.randn(tuple(input_signature))
        try:
            model(dummy_input)
            ok = True
        except Exception as e:
            message = e.args[0]
            print(message)
            # Example error
            # Expected 4-dimensional input for 4-dimensional weight [5, 3, 3, 3], but got 2-dimensional input of size [1, 1] instead
            if "dimensional" in message:
                num_dim = int(message[len("Expected ")])
                input_signature = [1 for i in range(num_dim)]
            # Calculated padded input size per channel: (1 x 1). Kernel size: (3 x 3). Kernel size can't be greater than actual input size
            elif "Kernel size can't be greater" in message:
                new_size = input_signature[2] * 2
                for i in range(2, len(input_signature)):
                    input_signature[i] = new_size
            # Given groups=1, weight of size [5, 3, 3, 3], expected input[1, 1, 1, 1] to have 3 channels, but got 1 channels instead
            elif "channels" in message:
                end = message.find("channels") - 1
                start = message.find("to have") + len("to have") + 1
                input_signature[1] = int(message[start:end])
            # mat1 and mat2 shapes cannot be multiplied (10x200 and 1000x100)
            elif "shapes cannot be multiplied" in message:
                if "shapes cannot be multiplied" in previousMessage:
                    first, second = extract_inner_dimensions(message)
                    first2, second2 = extract_inner_dimensions(previousMessage)
                    if first2 != first:
                        ours = first
                        theirs = second
                    else:
                        theirs = first
                        ours = second

                    size = input_signature[-1]

                    if ours > theirs:
                        if max_size is None:
                            max_size = size
                            size = (max_size + min_size) // 2
                        else:
                            max_size = size
                            size = (max_size + min_size) // 2
                    else:
                        if max_size is None:
                            min_size = size
                            size = min_size * 2
                        else:
                            min_size = size
                            size = (max_size + min_size) // 2

                    new_size = size

                    if len(input_signature) > 2:
                        for i in range(2, len(input_signature)):
                            input_signature[i] = new_size
                    else:
                        input_signature[1] = new_size
                else:
                    new_size = input_signature[2] * 2
                    for i in range(2, len(input_signature)):
                        input_signature[i] = new_size

            previousMessage = message

        tries += 1

    if ok:
        input_signature[0] = batch_size
        dummy_input = torch.randn(tuple(input_signature))
        return (dummy_input,), input_signature
    else:
        return None, None


def get_layers_configs(model, dummy_input, batch_size=None):
    layers = get_children_of_model(model)

    input_shapes = {}

    def get_input_shape(name):
        def hook(model, input, output):
            # activation[name] = output.detach()
            try:
                input_shapes[name] = input[0].shape
            except:
                pass

        return hook

    output_shapes = {}

    def get_output_shape(name):
        def hook(model, input, output):
            # activation[name] = output.detach()
            try:
                output_shapes[name] = output.shape
            except:
                pass

        return hook

    for i, layer in enumerate(layers):
        layer.register_forward_hook(get_input_shape(str(i)))
        layer.register_forward_hook(get_output_shape(str(i)))

    new_input_signature = None
    if dummy_input is None:
        dummy_input, new_input_signature = try_infer_input_shape(model, batch_size)

    model(*dummy_input)

    layers_configs = []

    for i, layer in enumerate(layers):
        try:
            input_shape = input_shapes[str(i)]
            output_shape = output_shapes[str(i)]
        except:
            continue
        if isinstance(layer, torch.nn.Conv2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(layer.out_channels),
                float(layer.kernel_size[0]),
                float(layer.stride[0]),
                float(layer.dilation[0]),
                float(layer.padding[0]),
                float(input_shape[0]),
            ]
            config = LayerConfig("Conv2D", params)
        elif isinstance(layer, torch.nn.Linear):
            params = [float(input_shape[1]), layer.out_features, float(input_shape[0])]
            config = LayerConfig("Linear", params)
        elif isinstance(layer, torch.nn.ReLU):
            x = input_shape[2] if len(input_shape) > 2 else 1
            params = [float(input_shape[1]), x, float(input_shape[0])]
            config = LayerConfig("ReLU", params)
        elif isinstance(layer, torch.nn.EmbeddingBag):
            params = [
                float(input_shape[0]),
                float(output_shape[0]),
                float(output_shape[1]),
                float(layer.num_embeddings),
            ]
            config = LayerConfig("EmbeddingBag", params)
        elif isinstance(layer, torch.nn.Dropout2d):
            x = input_shape[2] if len(input_shape) > 2 else 1
            params = [float(input_shape[1]), x, layer.p, float(input_shape[0])]
            config = LayerConfig("Dropout2d", params)
        elif isinstance(layer, torch.nn.Dropout):
            params = [float(input_shape[1]), layer.p, float(input_shape[0])]
            config = LayerConfig("Dropout", params)
        elif isinstance(layer, torchvision.ops.misc.FrozenBatchNorm2d):
            params = [
                float(input_shape[2]),
                layer.weight.shape[0],
                float(input_shape[0]),
            ]
            config = LayerConfig("BatchNorm2d", params)
        elif isinstance(layer, torch.nn.BatchNorm2d):
            params = [float(input_shape[2]), layer.num_features, float(input_shape[0])]
            config = LayerConfig("BatchNorm2d", params)
        elif isinstance(layer, torch.nn.MaxPool2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(layer.kernel_size),
                float(layer.stride),
                float(layer.dilation),
                float(layer.padding),
                float(input_shape[0]),
            ]
            config = LayerConfig("MaxPool2d", params)
        elif isinstance(layer, torch.nn.AdaptiveAvgPool2d):
            params = [
                float(input_shape[1]),
                float(input_shape[2]),
                float(input_shape[3]),
                float(layer.output_size[0]),
            ]
            config = LayerConfig("AdaptiveAvgPool2d", params)
        else:
            # unknown layer type
            config = LayerConfig(type(layer).__name__, None)

        layers_configs.append(config)

    return layers_configs, new_input_signature


def get_children_of_model(model: torch.nn.Module):
    # get children from model!
    children = list(model.children())
    flatt_children = []
    if children == []:
        # return wrapped in array, it will be flattened and return type will be consistant
        # also protects from error from fully functional models
        return [model]
    else:
        # look for children from children... to the last child!
        for child in children:
            try:
                flatt_children.extend(get_children_of_model(child))
            except TypeError:
                flatt_children.append(get_children_of_model(child))
    return flatt_children
