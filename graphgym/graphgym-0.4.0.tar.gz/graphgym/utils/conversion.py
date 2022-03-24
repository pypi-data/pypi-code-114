import torch

NODE_FEATURE = ['x', 'node_feature']
EDGE_FEATURE = ['edge_attr', 'edge_feature']


def set_dataset_attr(dataset, name, value, size):
    dataset._data_list = None
    dataset.data[name] = value
    dataset.slices[name] = torch.tensor([0, size], dtype=torch.long)


def del_dataset_attr(dataset, name):
    del dataset.data[name]
    del dataset.slices[name]


def convert_batch_attr(dataset):
    if 'node_feature' in dataset:
        set_dataset_attr(dataset, 'x', dataset.node_feature)


def decide_attr_name(batch, name_pair=('x', 'node_feature')):
    if name_pair[0] in batch:
        return name_pair[0]
    else:
        return name_pair[1]


def get_attr_name(batch, name='x'):
    if name in batch:
        return name
    if name in NODE_FEATURE:
        decide_attr_name(batch, NODE_FEATURE)
    if name in EDGE_FEATURE:
        decide_attr_name(batch, EDGE_FEATURE)
