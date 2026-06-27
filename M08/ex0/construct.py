import sys
import os
import site


def is_in_venv() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_venv_name() -> str:
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    if venv_path:
        return os.path.basename(venv_path)
    return ""


def show_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("")
    print("To enter the construct, run:")
    print("    python -m venv matrix_env")
    print("    source matrix_env/bin/activate # On Unix")
    print("    matrix_env\\Scripts\\activate # On Windows")
    print("")
    print("Then run this program again.")


def show_inside_venv() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name = get_venv_name()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("")

    packages_path = site.getsitepackages()[0] if site.getsitepackages() else ""
    print("Package installation path:")
    print(f"    {packages_path}")


def main() -> None:
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
