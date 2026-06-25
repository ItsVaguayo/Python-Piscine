import sys
import importlib


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
}

OPTIONAL_PACKAGES: dict[str, str] = {
    "requests": "requests",
}


def check_dependencies() -> dict[str, tuple[bool, str]]:
    results: dict[str, tuple[bool, str]] = {}

    for name, module in {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}.items():
        try:
            mod = importlib.import_module(module)
            version = getattr(mod, "__version__", "unknown")
            results[name] = (True, version)
        except ImportError:
            results[name] = (False, "")

    return results


def print_dependency_status(results: dict[str, tuple[bool, str]]) -> None:
    labels: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }

    print("Checking dependencies:")
    missing: list[str] = []

    for name, (ok, version) in results.items():
        if name == "requests":
            continue
        label = labels.get(name, "")
        if ok:
            print(f"  [OK] {name} ({version}) - {label}")
        else:
            print(f"  [MISSING] {name} - {label}")
            missing.append(name)

    if "requests" in results:
        ok, version = results["requests"]
        if ok:
            print(f"  [OK] requests ({version}) - {labels['requests']}")

    if missing:
        print("")
        print("Missing dependencies! Install with:")
        print("  pip:    pip install -r requirements.txt")
        print("  Poetry: poetry install")
        sys.exit(1)


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib  # type: ignore
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    print("")
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(42)
    matrix_data = rng.normal(loc=0.0, scale=1.0, size=1000)

    df = pd.DataFrame({
        "signal": matrix_data,
        "index": np.arange(1000),
    })

    rolling_mean = df["signal"].rolling(window=50).mean()

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    axes[0].plot(df["index"], df["signal"], alpha=0.4, color="green", linewidth=0.8)
    axes[0].plot(df["index"], rolling_mean, color="red", linewidth=1.5)
    axes[0].set_title("Matrix Signal (raw + 50-pt rolling mean)")
    axes[0].set_xlabel("Index")
    axes[0].set_ylabel("Signal")

    axes[1].hist(df["signal"], bins=40, color="green", alpha=0.7, edgecolor="black")
    axes[1].set_title("Signal Distribution")
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")

    plt.tight_layout()
    output_path = "matrix_analysis.png"
    plt.savefig(output_path)
    plt.close()

    print("Generating visualization...")
    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    results = check_dependencies()
    print_dependency_status(results)
    run_analysis()


if __name__ == "__main__":
    main()
