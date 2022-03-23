from typing import Tuple, Union

import torch
import torch.nn.functional as F
from einops import repeat  # type: ignore
from torch import Tensor
from torch.nn import BatchNorm1d, Conv1d, Dropout, Linear, Module


class TNet(Module):
    """Model class respresenting the T-Net as proposed in:

    Qi, Charles R., et al.
    "Pointnet: Deep learning on point sets for 3d classification and segmentation."
    Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

    """

    def __init__(self, dimension: int = 3):
        """Create a new instance of T-Net

        Args:
            dimension: the dimension for the learned transformation. Defaults to 3.
        """
        super(TNet, self).__init__()
        self.dim = dimension
        self.conv_1 = Conv1d(dimension, 64, 1)
        self.conv_2 = Conv1d(64, 128, 1)
        self.conv_3 = Conv1d(128, 1024, 1)
        self.fc_1 = Linear(1024, 512)
        self.fc_2 = Linear(512, 256)
        self.fc_3 = Linear(256, self.dim * self.dim)

        self.bn_1 = BatchNorm1d(64)  # type: ignore
        self.bn_2 = BatchNorm1d(128)  # type: ignore
        self.bn_3 = BatchNorm1d(1024)  # type: ignore
        self.bn_4 = BatchNorm1d(512)  # type: ignore
        self.bn_5 = BatchNorm1d(256)  # type: ignore

    def forward(self, x: Tensor) -> Tensor:
        """Process input point cloud and produce the transformation matrix.

        Args:
            x: The input clouds with shape (B, DIM, NUM_PTS). The method internally
            does NOT transposes the data tensor to correctly operate with PyTorch convetion (B CH N).

        Returns:
            The learned transformation with shape (B, DIMENSION, DIMENSION).
        """
        batch_size = x.shape[0]
        x = F.relu(self.bn_1(self.conv_1(x)))
        x = F.relu(self.bn_2(self.conv_2(x)))
        x = F.relu(self.bn_3(self.conv_3(x)))
        x = torch.max(x, 2, keepdim=True)[0]
        x = x.view(batch_size, -1)

        x = F.relu(self.bn_4(self.fc_1(x)))
        x = F.relu(self.bn_5(self.fc_2(x)))
        x = self.fc_3(x)

        iden = torch.eye(self.dim).view(1, self.dim * self.dim)
        iden = iden.to(x.device)
        iden = repeat(iden, "b d -> (r b)  d", r=x.size(0))
        x = x + iden
        x = x.view(-1, self.dim, self.dim)

        return x


class PointNetEncoder(Module):
    """Model class respresenting the PointNet Encoder as proposed in:

    Qi, Charles R., et al.
    "Pointnet: Deep learning on point sets for 3d classification and segmentation."
    Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

    """

    def __init__(
        self,
        size_latent: int = 1024,
        global_feature: bool = True,
        use_pts_tnet: bool = True,
        use_feats_tnet: bool = True,
    ) -> None:
        """Create a new instance of PointNet Encoder.

        Args:
            size_latent: the size for the global feature. Defaults to 1024.
            global_feature (optional): If True return a global embedding. Defaults to True.
            use_pts_tnet (optional): If True use the points T-Net. Defaults to True.
            use_feats_tnet (optional): If True use the features T-Net. Defaults to True.
        """
        super(PointNetEncoder, self).__init__()
        self.size_latent = size_latent
        self.use_pts_tnet = use_pts_tnet
        self.use_feat_tnet = use_feats_tnet

        if self.use_pts_tnet:
            self.tnet_pts = TNet(3)

        self.conv_1 = Conv1d(3, 64, 1)
        self.conv_2 = Conv1d(64, 128, 1)
        self.conv_3 = Conv1d(128, self.size_latent, 1)
        self.bn_1 = BatchNorm1d(64)  # type: ignore
        self.bn_2 = BatchNorm1d(128)  # type: ignore
        self.bn_3 = BatchNorm1d(self.size_latent)  # type: ignore
        self.global_feature = global_feature

        if self.use_feat_tnet:
            self.tnet_feats = TNet(64)

    def forward(self, x: Tensor) -> Tuple[Tensor, Union[Tensor, None], Union[Tensor, None]]:
        """Process input point cloud and produce point net features.

        Args:
            x: The input clouds with shape (B, NUM_PTS, DIM). The method internally
            transposes the data tensor to correctly operate with PyTorch convetion (B CH N).

        Returns:
            A tuple containing:
                - The computed global feature vector with shape (B, SIZE_LATENT) if global_feature is True
                  else the concatenation of global feature and per point features.
                - The learned transformation matrix for the input points.
                - The learned transformation matrix for the features.
        """
        num_pts = x.shape[1]
        x = x.transpose(2, 1)  # B DIM NUM_PTS
        if self.use_pts_tnet:
            trans_pts = self.tnet_pts(x)
            x = x.transpose(2, 1)
            x = torch.bmm(x, trans_pts)
            x = x.transpose(2, 1)
        else:
            trans_pts = None

        x = F.relu(self.bn_1(self.conv_1(x)))

        if self.use_feat_tnet:
            trans_feat = self.tnet_feats(x)
            x = x.transpose(2, 1)
            x = torch.bmm(x, trans_feat)
            x = x.transpose(2, 1)
        else:
            trans_feat = None

        features_per_point = x
        x = F.relu(self.bn_2(self.conv_2(x)))
        x = self.bn_3(self.conv_3(x))
        x = torch.max(x, 2, keepdim=True)[0]
        global_embedding = x.view(-1, self.size_latent)

        if self.global_feature:
            return global_embedding, trans_pts, trans_feat
        else:
            global_embedding = global_embedding.view(-1, self.size_latent, 1).repeat(1, 1, num_pts)
            return torch.cat([global_embedding, features_per_point], 1), trans_pts, trans_feat


class PointNetClassification(Module):
    def __init__(
        self,
        use_pts_tnet: bool = True,
        use_feats_tnet: bool = True,
        dropout_p: float = 0.3,
        num_classes: int = 10,
    ) -> None:
        """Create a new instance of PointNet Classification Network.

        Args:
            use_pts_tnet (optional): If True use the points T-Net. Defaults to True.
            use_feats_tnet (optional): If True use the features T-Net. Defaults to True.
            dropout_p: the dropout probability. Defaults to 0.5.
            num_classes: the number of classes. Defaults to 10.
        """

        super(PointNetClassification, self).__init__()
        self.encoder = PointNetEncoder(
            size_latent=1024,
            global_feature=True,
            use_pts_tnet=use_pts_tnet,
            use_feats_tnet=use_feats_tnet,
        )
        self.fc_1 = Linear(1024, 512)
        self.fc_2 = Linear(512, 256)
        self.fc_3 = Linear(256, num_classes)
        self.dropout = Dropout(dropout_p)
        self.bn_1 = BatchNorm1d(512)  # type: ignore
        self.bn_2 = BatchNorm1d(256)  # type: ignore

    def forward(self, x: Tensor) -> Tuple[Tensor, Union[Tensor, None], Union[Tensor, None]]:
        """Process input point clouds and produces claffication scores.

        Args:
            x: The input clouds with shape (B, NUM_PTS, DIM). The method internally
            transposes the data tensor to correctly operate with PyTorch convetion (B CH N).

        Returns:
            A tuple containing:
                - The computed classification scores with shape (B, NUM_CLASSES).
                - The learned transformation matrix for the input points.
                - The learned transformation matrix for the features.
        """
        x, trans_pts, trans_feat = self.encoder(x)
        x = F.relu(self.dropout(self.bn_1(self.fc_1(x))))
        x = F.relu(self.dropout(self.bn_2(self.fc_2(x))))
        x = self.fc_3(x)
        return x, trans_pts, trans_feat


class PointNetSegmentation(Module):
    def __init__(
        self, use_pts_tnet: bool = True, use_feats_tnet: bool = True, num_classes: int = 10
    ) -> None:
        """Create a new instance of PointNet Semantic Segmentation Network.

        Args:
            use_pts_tnet (optional): If True use the points T-Net. Defaults to True.
            use_feats_tnet (optional): If True use the features T-Net. Defaults to True.
            num_classes: the number of classes. Defaults to 10.
        """
        super(PointNetSegmentation, self).__init__()
        self.num_classes = num_classes
        self.encoder = PointNetEncoder(
            global_feature=False, use_feats_tnet=use_feats_tnet, use_pts_tnet=use_pts_tnet
        )
        self.conv_1 = Conv1d(1088, 512, 1)
        self.conv_2 = Conv1d(512, 256, 1)
        self.conv_3 = Conv1d(256, 128, 1)
        self.conv_4 = Conv1d(128, self.num_classes, 1)
        self.bn_1 = BatchNorm1d(512)  # type: ignore
        self.bn_2 = BatchNorm1d(256)  # type: ignore
        self.bn_3 = BatchNorm1d(128)  # type: ignore

    def forward(self, x: Tensor) -> Tuple[Tensor, Union[Tensor, None], Union[Tensor, None]]:
        """Process input point clouds and produces per points claffication scores.

        Args:
            x: The input clouds with shape (B, NUM_PTS, DIM). The method internally
            transposes the data tensor to correctly operate with PyTorch convetion (B CH N).

        Returns:
            A tuple containing:
                - The computed classification scores with shape (B, NUM_PTS, NUM_CLASSES).
                - The learned transformation matrix for the input points.
                - The learned transformation matrix for the features.
        """
        batchsize = x.size()[0]
        n_pts = x.size()[1]
        x, trans_pts, trans_feat = self.encoder(x)
        x = F.relu(self.bn_1(self.conv_1(x)))
        x = F.relu(self.bn_2(self.conv_2(x)))
        x = F.relu(self.bn_3(self.conv_3(x)))
        x = self.conv_4(x)
        x = x.transpose(2, 1).contiguous()
        x = x.view(batchsize, n_pts, self.num_classes)

        return x, trans_pts, trans_feat
