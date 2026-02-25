def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        with open('classified_data.txt', 'a+') as file:
            file.seek(0)
            data = file.readlines()
            # a+ starts at end of file. seek(0) fixes it

            print("Vault connection established with failsafe protocols\n")

            print("SECURE EXTRACTION:")
            for line in data:
                print(line.replace('\n', ""))

            print("\nSECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            file.write("[CLASSIFIED] New security protocols archived\n")
            print("Vault automatically sealed upon completion")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.")

    print("\nAll vault operations completed with maximum security")


if __name__ == "__main__":
    ft_vault_security()
