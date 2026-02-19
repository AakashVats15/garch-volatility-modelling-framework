import os

base_path = r"E:\Personal\GitHub\Python Code Repo\garch-volatility-modelling-framework"

folders = [
    "data/raw",
    "data/processed",
    "src/models",
    "src/diagnostics",
    "src/forecasting",
    "src/simulation",
    "src/utils",
    "examples",
    "tests",
    "docs/figures"
]

files = [
    "src/models/arch_model.py",
    "src/models/garch_model.py",
    "src/models/mle_estimation.py",

    "src/diagnostics/acf_pacf.py",
    "src/diagnostics/qq_plots.py",
    "src/diagnostics/residual_tests.py",

    "src/forecasting/volatility_forecast.py",

    "src/simulation/garch_simulation.py",

    "src/utils/data_loader.py",
    "src/utils/plotting.py",
    "src/utils/stats_helpers.py",
    "src/__init__.py",

    "examples/run_estimation.py",
    "examples/run_diagnostics.py",
    "examples/run_forecasting.py",
    "examples/run_simulation.py",

    "tests/test_models.py",
    "tests/test_diagnostics.py",
    "tests/test_forecasting.py",

    "docs/methodology.md",
    "docs/interpretation.md",

    "requirements.txt",
    "README.md",
    "LICENSE",
    ".gitignore"
]

# Create folders
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

# Create empty files
for file in files:
    file_path = os.path.join(base_path, file)
    with open(file_path, "w") as f:
        pass

print("Repository structure created successfully.")