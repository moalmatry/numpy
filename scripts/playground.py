import numpy as np
from numpy_study import describe


def run() -> None:
    arr = np.linspace(0, 1, 6).reshape(2, 3)
    describe(arr)


if __name__ == "__main__":
    run()
