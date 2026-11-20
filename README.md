# NumPy Study

Python project managed with `uv` for studying NumPy using Jupyter notebooks and standalone scripts.

## Project Structure

```text
.
├── notebooks/              # Topic-by-topic Jupyter notebooks
│   ├── 00_getting_started.ipynb
│   └── README.md
├── scripts/                # Quick standalone Python scripts
│   └── playground.py
├── data/                   # Sample datasets / .npy / .npz / .csv files
├── src/numpy_study/        # Reusable study helpers (importable anywhere)
│   └── __init__.py
├── pyproject.toml
├── uv.lock
└── .python-version
```

## Setup

```bash
uv sync
```

## Running Jupyter

- Launch classic Jupyter Notebook:
  ```bash
  uv run jupyter notebook
  ```
- Or launch JupyterLab:
  ```bash
  uv run jupyter lab
  ```
- In VS Code / IDE notebooks, select the `.venv` Python kernel (`Python 3.14`).

## Running Scripts

- Run the package entrypoint:
  ```bash
  uv run numpy-study
  ```
- Run a script in `scripts/`:
  ```bash
  uv run python scripts/playground.py
  ```

## Adding Packages

```bash
uv add matplotlib pandas       # runtime study libraries
uv add --dev pytest ruff       # dev tools
```
