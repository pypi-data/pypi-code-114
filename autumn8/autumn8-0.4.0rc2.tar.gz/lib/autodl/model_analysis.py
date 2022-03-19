import json

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


def get_layers_configs(model, dummy_input):
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

    return layers_configs


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
