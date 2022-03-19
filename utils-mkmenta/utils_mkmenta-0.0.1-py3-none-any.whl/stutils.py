from contextlib import contextmanager
from typing import Union, Sequence
import streamlit as st
import numpy

__all__ = ["Grid", "image"]


class Grid:
    """
    Streamlit Grid Layout.

    Use it as following (example for a grid of 4 columns):
    ```
    grid = Grid(4)
    for i in whatever:
        with grid.next():
            # Your streamlit elements of each cell
            ...
    ```
    """

    def __init__(self, spec: Union[int, Sequence[Union[int, float]]]):
        """Initialize.

        Args:
            - spec: Parameter for `streamlit.columns` of the grid. Check official documentation of `streamlit.columns`
        """
        self.spec = spec
        self._i = 0
        self._columns = st.columns(self.spec)
        self._container = st.container()

    @contextmanager
    def next(self):
        """Returns next grid cell's context manager."""
        if self._i == len(self._columns):
            self._columns = st.columns(self.spec)
            self._container = st.container()
            self._i = 0
        with self._container as container, self._columns[self._i] as column:
            yield container, column
        self._i += 1


def image(image: numpy.ndarray, caption=None, max_width=None, max_height=None, clamp=False,
          channels='RGB', output_format='auto'):
    """Streamlit Image with max width and height."""
    if image.ndim in (2, 3):
        height, width = image.shape[:2]
    else:
        raise ValueError(f"image with {image.ndim} dimensions: {image.shape}")
    effective_width = max_width if max_width is not None else width
    if max_height is not None:
        mhwidth = int(width * (max_height / height))
        effective_width = min(mhwidth, effective_width)
    if effective_width == width:
        effective_width = None
    return st.image(image, caption=caption, width=effective_width, clamp=clamp,
                    channels=channels, output_format=output_format)
