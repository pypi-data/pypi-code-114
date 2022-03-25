"""PyTorch-specific DataLoader implementations."""
from typing import Any, Iterator, List, Optional, cast

import numpy as np
from torch.utils.data import DataLoader as PyTorchDataLoader

from bitfount.backends.pytorch.data.datasets import _PyTorchBaseDataset
from bitfount.data.dataloader import _BitfountDataLoader


class _PyTorchBitfountDataLoader(_BitfountDataLoader):
    """Wraps a PyTorch DataLoader with bitfount functions."""

    def __init__(self, dataset: _PyTorchBaseDataset, batch_size: Optional[int] = None):

        super().__init__(dataset, batch_size)

        # We set both dataloader and dataset, the former to allow length and
        # iteration to work, the latter to allow the get_*_dataframe() methods to work.
        # Explicitly set batch_size to 1 for the dataloader to ensure "batching" still
        # takes place.
        if not self.batch_size:
            self.batch_size = 1
        self.dataloader: PyTorchDataLoader = self._create_pytorch_dataloader()

    def _create_pytorch_dataloader(self, **kwargs: Any) -> PyTorchDataLoader:
        return PyTorchDataLoader(
            cast(_PyTorchBaseDataset, self.dataset),
            batch_size=self.batch_size,
            **kwargs,
        )

    def __iter__(self) -> Iterator[List[np.ndarray]]:
        """Yield a batch of data or a single element if batch_size is None."""
        for batch in self.dataloader:
            yield [x for x in batch]

    def __len__(self) -> int:
        """Number of batches or number of elements if batch size is None."""
        return len(self.dataloader)
