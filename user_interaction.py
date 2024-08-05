
def get_user_choice():
    print("Select the metric you want to calculate:")
    print("1. Distance between left eye and right eye")
    print("2. Face length")
    print("3. Forehead size")
    print("4. Size of the mouth")
    print("5. Show face landmarks with connections only (no calculations)")
    
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice in [1, 2, 3, 4, 5]:
            return choice
        else:
            print("Invalid choice. Exiting.")
            return None
    except ValueError:
        print("Invalid input. Exiting.")
        return None
