# Exercise: 'Pets'
# Ask the user to enter a pet and tell them the price. If an invalid pets is
# picked, tell the user nicely, and let them try again

def pets():

    user_input = input("Select a pet: ")
    
    available_pets = get_available_pets()

    if user_input in available_pets:
        print("One {0} costs {1}".format(user_input, available_pets[user_input]))
    else:
        print("Sorry, we don't have any of those pets.")

def get_available_pets():
    return {"bird": 3.5, "dog": 7.25, "gerbil": 1.5}

if __name__ == "__main__":
    pets()