from typing import Tuple, Union

from pytorch3d.ops.knn import knn_points  # type: ignore
from torch import Tensor, sqrt, sum, zeros


def f_score(
    predictions: Union[Tensor, None],
    groundtruth: Union[Tensor, None],
    dist_pred_gt: Union[Tensor, None] = None,
    dist_gt_pred: Union[Tensor, None] = None,
    threshold: float = 0.01,
) -> Tuple[Tensor, Tensor, Tensor]:
    """Compute the F1-Score using the treshold as defined in:

    Knapitsch, A., Park, J., Zhou, Q. Y., & Koltun, V. (2017).
    Tanks and temples: Benchmarking large-scale scene reconstruction.
    ACM Transactions on Graphics (ToG), 36(4), 1-13.


    Args:
        predictions: the predicted point cloud with shape (B, NUM_POINTS, 3).
        groundtruth: the groundtruth point cloud with shape (B, NUM_POINTS, 3).
        dist_pred_gt (optional): per point distances from predictions to groundtruth
        with shape (B, NUM_POINTS, 3). Defaults to None.
        dist_gt_pred (optional): per point distances from groundtruth to predictions
        with shape (B, NUM_PTS_GT, 3). Defaults to None.
        threshold: the distance treshold to use. Defaults to 0.01.

    Returns:
        A Tuple with:
        - The fscore with shape (B,).
        - The precision with shape (B,).
        - The recall with shape (B,).
    """

    if dist_pred_gt is None:
        dist_pred_gt, _, _ = knn_points(predictions, groundtruth)
        dist_pred_gt = dist_pred_gt.squeeze(-1)
        dist_pred_gt = sqrt(dist_pred_gt)

    if dist_gt_pred is None:
        dist_gt_pred, _, _ = knn_points(groundtruth, predictions)
        dist_gt_pred = dist_gt_pred.squeeze(-1)
        dist_gt_pred = sqrt(dist_gt_pred)

    dist_precision = dist_pred_gt
    dist_recall = dist_gt_pred

    batch_size = len(dist_precision)
    f_scores = zeros(batch_size).to(dist_precision.device)
    recall = zeros(batch_size).to(dist_precision.device)
    precision = zeros(batch_size).to(dist_precision.device)

    num_samples_prec = dist_precision.shape[1]
    num_samples_rec = dist_recall.shape[1]

    precision = sum((dist_precision < threshold), dim=-1) / max(num_samples_prec, 1)
    recall = sum((dist_recall < threshold), dim=-1) / max(num_samples_rec, 1)

    prec_and_rec = recall + precision
    mask = prec_and_rec > 0

    f_scores[mask] = 2 * recall[mask] * precision[mask] / prec_and_rec[mask]

    return f_scores, precision, recall
