workers = 0
your_choice = 0
all_projects = []
completed_projects = []
execute = True
project_names = []
possible_inputs = ["ongoing", "completed", "onhold"]
variable_of_possible_inputs = [0] * len(possible_inputs)
menu = """
 XYZ Company
 Main Menu
 1. Add a new project to existing projects.
 2. Remove a completed project from existing projects.
 3. Add new workers to available workers group.
 4. Updates details on ongoing projects.
 5. Project statics.
 6. Exit
"""


while execute:
    print(menu)
    # Check the user choice
    your_choice = int(input("Enter your choice: "))

    # When user choice is 1
    if your_choice == 1:
        pass

    # When user choice is 2
    elif your_choice == 2:
        pass

    # When user choice is 3
    elif your_choice == 3:
        pass
    # When user choice is 4
    elif your_choice == 4:
        pass

    # When user choice is 5
    elif your_choice == 5:
        pass

    # When  user choice is 6
    elif your_choice == 6:
        execute = False

    else:
        print("Please enter a valid choice...")
