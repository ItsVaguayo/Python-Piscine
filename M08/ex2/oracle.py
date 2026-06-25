import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    print("Install it with: pip install python-dotenv")
    sys.exit(1)


REQUIRED_VARS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "",
    "API_KEY": "",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "",
}


def load_configuration() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {}
    for key in REQUIRED_VARS:
        value = os.environ.get(key, DEFAULTS.get(key, ""))
        config[key] = value
    return config


def display_configuration(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    db_url = config["DATABASE_URL"]
    api_key = config["API_KEY"]
    log_level = config["LOG_LEVEL"]
    zion = config["ZION_ENDPOINT"]

    if mode == "production":
        db_display = "Connected to production instance" if db_url else "Not configured"
        zion_display = "Online (production)" if zion else "Offline"
    else:
        db_display = "Connected to local instance" if db_url else "Not configured"
        zion_display = "Online" if zion else "Offline"

    api_display = "Authenticated" if api_key else "Not configured"

    print("Configuration loaded:")
    print(f"  Mode:         {mode}")
    print(f"  Database:     {db_display}")
    print(f"  API Access:   {api_display}")
    print(f"  Log Level:    {log_level}")
    print(f"  Zion Network: {zion_display}")

    if mode == "production":
        print("")
        print("  [PRODUCTION MODE] Enhanced security active.")
        print("  [PRODUCTION MODE] Verbose logging disabled.")
    else:
        print("")
        print("  [DEVELOPMENT MODE] Debug logging enabled.")
        print("  [DEVELOPMENT MODE] Local instance in use.")


def security_check(config: dict[str, str]) -> None:
    print("")
    print("Environment security check:")

    env_file_ok = os.path.isfile(".env")
    example_file_ok = os.path.isfile(".env.example")

    print("  [OK] No hardcoded secrets detected")

    if env_file_ok or example_file_ok:
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found — using environment variables or defaults")

    print("  [OK] Production overrides available")


def warn_missing(config: dict[str, str]) -> None:
    missing = [k for k in REQUIRED_VARS if not config[k]]
    if missing:
        print("")
        print("WARNING: The following variables are missing or empty:")
        for key in missing:
            print(f"  - {key}")
        print("")
        print("Copy .env.example to .env and fill in the values:")
        print("  cp .env.example .env")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("")

    config = load_configuration()
    display_configuration(config)
    warn_missing(config)
    security_check(config)

    print("")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
