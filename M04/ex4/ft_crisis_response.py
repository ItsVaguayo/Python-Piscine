def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open('lost_archive.txt', 'r') as file:
            print(file)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
    try:
        with open('classified_data.txt', 'r') as file:
            print(file)
    except (PermissionError, FileNotFoundError):
        print("STATUS: Crisis handled, security maintained")
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open('standard_archive.txt', 'r') as file:
            data: str = file.readline()
            print(f"SUCCESS: Archive recovered - ``{data}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")


if __name__ == "__main__":
    ft_crisis_response()
