import numpy as np


def describe(arr: np.ndarray) -> None:
    """Print shape, dimensions, dtype, size, and memory details for a NumPy array."""
    print(f"array:\n{arr}")
    print(
        f"shape={arr.shape}, ndim={arr.ndim}, dtype={arr.dtype}, "
        f"size={arr.size}, itemsize={arr.itemsize}B, nbytes={arr.nbytes}B"
    )


def main() -> None:
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy {np.__version__} ready!")
    describe(arr)
