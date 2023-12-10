# Variable initialization
# Main loop repeater
loop = True

# Main menu variables
your_choice = 0
proj_code = 0
client_name = ""
start_date = 0
end_date = 0
num_of_workers = 0
proj_stat = ""
save = ""

new_workers = 0
avail_workers = 0

# arrays
ProjCode = []
ClientName = []
StartDate = []
EndDate = []
NumofWorkers = []
ProjectStatus = []

# Variables in updating an existing project
new_proj_code = 0
new_client_name = ""
new_start_date = 0
new_end_date = 0
new_proj_stat = ""
updated_workers = 0

ProjectStatRepeater = True
OnGoing = 0
OnHold = 0
Completed = 0
false_save = False  # Used in the remove completed project loop

ProjFound = True
remove_repeater = True


while loop == True:  # Main loop
    print("-------------------------------")
    print("    XYZ Company")
    print("    Main Menu")
    print("")  # to get extra space in between

    print("1. Add a new project to existing projects")
    print("2. Remove a completed project")
    print("3. Add new workers to available workers group")
    print("4. Update details on ongoing projects")
    print("5. Project statistics")
    print("6. Exit")
    print("")  # to get extra space in between

    your_choice = int(input("   Your choice: "))
    print("-------------------------------")

    while 1 <= your_choice <= 6:
        if your_choice == 1:  # First choice
            # Collecting details of the new project
            print("    XYZ Company")
            print("    Add a new project")
            print("")  # to get extra space in between

            proj_code = str(
                input("1. Project code (Enter 0 to go back to the main menu): ")
            )

            # Redirecting to the main menu if the user input is 0
            if proj_code == "0":
                loop = True
                print("Going back to the main menu...")
                break

            # Collecting other details
            client_name = str(input("2. Client's name: "))
            start_date = str(input("3. Start date: "))
            end_date = str(input("4. Expect end date: "))
            num_of_workers = int(input("5. Number of workers: "))
            proj_stat = str(
                input("6. Project status (Ongoing / On hold / Completed): ")
            )

            ProjectStatRepeater = True
            while ProjectStatRepeater:
                if proj_stat == "on going" or proj_stat == "ongoing":
                    OnGoing = OnGoing + 1
                    ProjectStatRepeater = False
                elif proj_stat == "on hold":
                    OnHold = OnHold + 1
                    ProjectStatRepeater = False
                elif proj_stat == "completed":
                    Completed = Completed + 1
                    ProjectStatRepeater = False
                else:
                    proj_stat = str(input("Please enter a valid project status - "))
                    ProjectStatRepeater = True
            print("")  # to get extra space in between

            # Saving the project
            false_save = False
            while not false_save:
                # Displaying what user just entered (To make sure the entered data is correct)
                print("1. Project code: ", proj_code)
                print("2. Client's name: ", client_name)
                print("3. Start date: ", start_date)
                print("4. End date: ", end_date)
                print("5. Number of workers: ", num_of_workers)
                print("6. Project satatus: ", proj_stat)
                print("")  # to get extra space in between
                save = input(
                    "Do you want to save the project (Yes/No)? - "
                ).lower()  # checks for the lower case answer of the boolean yes or no
                false_save = True
                if save == "no":
                    print("Project was not saved")
                elif save == "yes":
                    print("Project saved successfully")
                    # Append values to respective lists
                    ProjCode.append(proj_code)
                    ClientName.append(client_name)
                    StartDate.append(start_date)
                    EndDate.append(end_date)
                    ProjectStatus.append(proj_stat)
                    NumofWorkers.append(num_of_workers)
                else:
                    # if the answer is not yes or no loop should repeat
                    print("Invalid input. Please enter 'Yes' or 'No'.")
                    false_save = False
                    print("-------------------------------")
            break
        elif your_choice == 2:  # Second choice
            # Remove completed project
            print("    XYZ Company")
            print("    Remove completed project")
            print("")  # to get extra space in between

            proj_code = str(input("Project code: "))
            while proj_code not in ProjCode:
                print(
                    "the entered project code doesnt appear to be in the stored values"
                )
                proj_code = str(input("Project code: "))
            print("project preset in the stored values")
            index_value = ProjCode.index(proj_code)
            print("")  # to get extra space in between

            # Saving the project
            false_save = False
            while not false_save:
                save = input(
                    "Do you want to remove the project (Yes/No)? - "
                ).lower()  # checks for the lower case answer of the boolean yes or no
                false_save = True
                if save == "no":
                    print("Project was not removed")
                elif save == "yes":
                    print("Project removed successfully")
                    # Append values to respective lists
                    ProjCode.pop(index_value)
                    ClientName.pop(index_value)
                    StartDate.pop(index_value)
                    EndDate.pop(index_value)
                    ProjectStatus.pop(index_value)
                    NumofWorkers.pop(index_value)
                else:
                    # if the answer is not yes or no loop should repeat
                    print("Invalid input. Please enter 'Yes' or 'No'.")
                    false_save = False
                    print("-------------------------------")
            break

        elif your_choice == 3:  # Third choice
            # Add new workers
            print("    XYZ Company")
            print("    Add new workers")
            print("")  # to get extra space in between

            new_workers = int(input("New workers to add: "))
            print("")  # to get extra space in between

            if new_workers <= 0:
                new_workers = int(input("Please enter a positive value: "))
            avail_workers = avail_workers + new_workers

            save = str(
                input("Do you want to add (Yes / No)? ")
            ).lower()  # Checks for lowercase 'yes' and 'no'
            false_save = True
            if save == "yes":
                print("Succesfully added new workers")
                print("Number of available workers- ", avail_workers)
                break
            elif save == "no":
                print("Failed to add new workers ")
                break
            print("-------------------------------")

        elif your_choice == 4:  # Forth choice
            # Update project details
            print("    XYZ Company")
            print("    Update project details")
            print("")  # to get extra space in between

            ProjFound = False
            while ProjFound is False:
                proj_code = str(
                    input("1. Project code (Enter 0 to go back to the main menu): ")
                )

                # Redirecting to the main menu if the user input is 0
                if proj_code == "0":
                    ProjFound = True
                    your_choice = 9
                    false_save = True
                    print("Going back to the main menu...")
                    break
                elif proj_code not in ProjCode:
                    # If the given project code does not exist
                    print(
                        "The entered project code does not exist. Please enter a valid code"
                    )
                elif proj_code in ProjCode:
                    # If the given project code exist
                    ProjFound = True
                    index_value = ProjCode.index(proj_code)
                    print("")

                    # Collecting other information
                    new_client_name = str(input("2. Client's name: "))
                    new_start_date = str(input("3. Start date: "))
                    new_end_date = str(input("4. Expect end date: "))
                    new_num_of_workers = int(input("5. Number of workers: "))
                    new_proj_stat = str(
                        input("6. Project status (Ongoing / On hold / Completed): ")
                    )

                    # Updating project status by removing the project from the relevant project status
                    if ProjectStatus == "On going":
                        OnGoing = OnGoing - 1
                    elif ProjectStatus == "Completed":
                        Completed = Completed - 1
                    elif ProjectStatus == "On hold":
                        OnHold = OnHold - 1

                    # Updating the project status by adding one to the relavant project status (According to the user input)
                    if new_proj_stat == "On going":
                        OnGoing = OnGoing + 1
                    elif new_proj_stat == "Completed":
                        Completed = Completed + 1
                    elif new_proj_stat == "On hold":
                        OnHold = OnHold + 1

                    updated_workers = int(input("New number of workers: "))
            print("")  # to get extra space in between

            while false_save is False:
                # Displaying what user just entered (To make sure the entered data is correct)
                print("1. Project code: ", new_proj_code)
                print("2. Client's name: ", new_client_name)
                print("3. Start date: ", new_start_date)
                print("4. End date: ", new_end_date)
                print("5. Number of workers: ", new_num_of_workers)
                print("6. Project satatus: ", new_proj_stat)
                print("")  # to get extra space in between
                save = input(
                    "Do you want to update the project details (Yes / No)? "
                ).lower()  # Checks for lowercase words too
                false_save = True
                if save == "yes":
                    # Updating existing info with collected info
                    ProjCode[index_value] = new_proj_code
                    ClientName[index_value] = new_client_name
                    StartDate[index_value] = new_statr_date
                    EndDate[index_value] = new_end_date
                    NumofWorkers[index_value] = updated_workers
                    ProjectStatus[index_value] = new_proj_stat
                    print("Project updated succesfully")
                elif save == "no":
                    print("Project was not updated.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'")
                    false_save = False
            print("-------------------------------")

        elif your_choice == 5:  # Fifth choice
            # Project statistics
            print("    XYZ Company")
            print("    Project statistics")
            print("")  # To get extra space in between
            print("Number of ongoing projects: ", OnGoing)
            print("Number of completed projects: ", Completed)
            print("Number of on hold projects: ", OnHold)
            print("Number of available workers to assign: ", avail_workers)

            while false_save == False:
                save = input("Do you want to add the project (Yes / No)? ").lower()
                false_save = True
                if save == "yes":
                    print("Redirecting to 'Add a new project'...")
                    print("")  # to get extra space in between

                    print("    XYZ Company")
                    print("    Add a new project")
                    print("")  # to get extra space in between

                    proj_code = str(
                        input("1. Project code (Enter 0 to go back to the main menu): ")
                    )

                    # Redirecting to the main menu if the user input is 0
                    if proj_code == "0":
                        loop = True
                        print("Going back to the main menu...")
                        break

                    # Collecting other details
                    client_name = str(input("2. Client's name: "))
                    start_date = str(input("3. Start date: "))
                    end_date = str(input("4. Expect end date: "))
                    num_of_workers = int(input("5. Number of workers: "))
                    proj_stat = str(
                        input("6. Project status (Ongoing / On hold / Completed): ")
                    )

                    ProjectStatRepeater = True
                    while ProjectStatRepeater:
                        if proj_stat == "on going" or proj_stat == "ongoing":
                            OnGoing = OnGoing + 1
                            ProjectStatRepeater = False
                        elif proj_stat == "on hold":
                            OnHold = OnHold + 1
                            ProjectStatRepeater = False
                        elif proj_stat == "completed":
                            Completed = Completed + 1
                            ProjectStatRepeater = False
                        else:
                            proj_stat = str(
                                input("Please enter a valid project status - ")
                            )
                            ProjectStatRepeater = True
                    print("")  # to get extra space in between

                    # Saving the project
                    false_save = False
                    while not false_save:
                        # Displaying what user just entered (To make sure the entered data is correct)
                        print("1. Project code: ", proj_code)
                        print("2. Client's name: ", client_name)
                        print("3. Start date: ", start_date)
                        print("4. End date: ", end_date)
                        print("5. Number of workers: ", num_of_workers)
                        print("6. Project satatus: ", proj_stat)
                        print("")  # to get extra space in between
                        save = input(
                            "Do you want to save the project (Yes/No)? - "
                        ).lower()  # checks for the lower case answer of the boolean yes or no
                        false_save = True
                        if save == "no":
                            print("Project was not saved")
                        elif save == "yes":
                            print("Project saved successfully")
                            # Append values to respective lists
                            ProjCode.append(proj_code)
                            ClientName.append(client_name)
                            StartDate.append(start_date)
                            EndDate.append(end_date)
                            ProjectStatus.append(proj_stat)
                            NumofWorkers.append(num_of_workers)
                        else:
                            # if the answer is not yes or no loop should repeat
                            print("Invalid input. Please enter 'Yes' or 'No'.")
                            false_save = False
            print("-------------------------------")

        elif your_choice == 6:  # Sixth choice
            print("Exiting the program...")
            loop = False
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6")
