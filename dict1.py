# User profile management using a dictionary

# Initialize an empty dictionary for user profiles.
# Keys are user IDs and values are user names.
user_profiles = {}


def add_user(user_id, name):
    """Add a new user profile to the dictionary."""
    if user_id in user_profiles:
        print(f"User ID {user_id} already exists. Use update_user to change the name.")
        return False

    user_profiles[user_id] = name
    return True


def get_user_name(user_id):
    """Retrieve a user's name by their ID, returning None if not found."""
    return user_profiles.get(user_id)


def update_user(user_id, new_name):
    """Update an existing user's name by ID."""
    if user_id not in user_profiles:
        print(f"User ID {user_id} not found. Cannot update.")
        return False

    user_profiles[user_id] = new_name
    return True


def remove_user(user_id):
    """Remove a user profile by ID, handling missing IDs."""
    if user_id not in user_profiles:
        print(f"User ID {user_id} not found. Cannot remove.")
        return False

    del user_profiles[user_id]
    return True


if __name__ == "__main__":
    # Test adding users
    print("Adding users:")
    add_user(1, "Alice")
    add_user(2, "Bob")
    add_user(3, "Charlie")
    print(user_profiles)
    print()

    # Test retrieving users
    print("Retrieving user names:")
    print("ID 2:", get_user_name(2))
    print("ID 4:", get_user_name(4))
    print()

    # Test updating a user
    print("Updating user 3:")
    update_user(3, "Charlotte")
    print(user_profiles)
    print()

    # Test removing a user
    print("Removing user 1:")
    remove_user(1)
    print(user_profiles)
    print()

    # Test handling missing entries
    print("Handling missing IDs:")
    update_user(4, "Diana")
    remove_user(4)
    print(user_profiles)
