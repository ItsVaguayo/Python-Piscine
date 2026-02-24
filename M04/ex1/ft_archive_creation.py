def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", 'w') as file:
            print("Storage unit created successfully...\n")
            data = [
                "[ENTRY 001] New quantum algorithm discovered\n",
                "[ENTRY 002] Efficiency increased by 347%\n",
                "[ENTRY 003] Archived by Data Archivist trainee"]
            print("Inscribing preservation data...")
            for line in data:
                print(line.replace('\n', ''))
                file.write(line)
            print("\nData inscription complete. Storage unit sealed")
            print(f"Archive {file.name} ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        return


if __name__ == "__main__":
    ft_archive_creation()
