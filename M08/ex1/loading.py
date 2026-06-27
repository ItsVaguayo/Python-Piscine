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
    print("Generating visualization...")

    rng = np.random.default_rng(42)
    data = rng.normal(size=1000)

    df = pd.DataFrame({"signal": data})
    df["rolling"] = df["signal"].rolling(window=50).mean()

    df.plot(figsize=(10, 4), title="Matrix Signal")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    results = check_dependencies()
    print_dependency_status(results)
    run_analysis()


if __name__ == "__main__":
    main()
