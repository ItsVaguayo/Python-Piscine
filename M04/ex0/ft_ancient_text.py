def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        with open('ancient_fragment.txt', 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    else:
        print("Connection established...\n")
        for line in data:
            print(line.replace('\n', ''))
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
