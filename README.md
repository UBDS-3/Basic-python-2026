# UBDS^3 2026 Basic-python-2026
Repo for basic Python track of UBDS^3

Basic Python course for UBDS^3 2026, focusing on intro to programming, data types, dataframes, and intro to data science


| Day | Topic |
|-----|-------|
| 1 | Python - variables, lists - [notebook](day1/python_basic_day_1.ipynb) |
| 2 | Functions, expressions, dictionary, loops - [Chapter 2](day2/Chapter%202.ipynb), [Chapter 3](day2/Chapter%203.ipynb), [Chapter 4](day2/Chapter%204.ipynb) |
| 3 | Writing functions, reading errors, debugging, classes - [notebook](day3/Day_3.ipynb), [alignment practical](day3/real_aligment/notebooks/dna_translation_alignment.ipynb) |
| 4 | Pandas & matplotlib - [intro notebook](day4/Intro_to_Pandas_Matplotlib.ipynb), [GFF notebook](day4/querying_gff.ipynb) |
| 5 | EDA, statistics, regression - [notebook](day5/Day%205%20solutions.ipynb) |

## Install all practical dependencies with uv

This repository includes a shared `pyproject.toml` for all practicals. 

### 1. Install uv

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS with Homebrew:

```bash
brew install uv
```

macOS without Homebrew:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installing, close and reopen the terminal, then check that `uv` works:

```bash
uv --version
```

### 2. Install everything for the course

From the `Basic-python-2026` folder, run:

```bash
uv sync
```

This creates a local virtual environment in `.venv` and installs Jupyter, BioPython,
NumPy, pandas, matplotlib, SciPy, statsmodels, scikit-learn, seaborn, and pytest.

If you need to recreate or update the lock file, run:

```bash
uv lock
```

### 3. Open the notebooks

Use Jupyter from the uv environment:

```bash
uv run jupyter notebook
```

You can also run tests for the day 3 alignment practical:

```bash
uv run pytest day3/real_aligment/tests
```

## Useful uv commands

`uv init` creates a new Python project by adding a `pyproject.toml` file. You do
not need to run it for this repository because the project file is already here.

```bash
uv init
```

`uv add` installs a new package and records it in `pyproject.toml`. Use this if a
new practical needs an extra package.

```bash
uv add package-name
```

For example:

```bash
uv add requests
```

`uv sync` installs everything listed in `pyproject.toml` and `uv.lock` into the
local `.venv` environment.

```bash
uv sync
```

`uv lock` resolves package versions and updates `uv.lock`. Use it after changing
dependencies, then share the updated `uv.lock` with the repository.

```bash
uv lock
```

To run commands inside the uv environment, prefix them with `uv run`:

```bash
uv run python --version
uv run jupyter notebook
```
