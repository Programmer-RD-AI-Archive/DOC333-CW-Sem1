# Variable Initialization.

Users_choice = 0
Workers = 10000
# list initialization.
projects_L = [0]
clients_name_L = [0]
start_date_L = [0]
expected_end_date_L = [0]
number_of_workers_needed_L = [0]
project_status_L = [0]
completed_project_code = [0]
actual_end_day = [0]
redirect = False
redirect_choice = None
completed_number_of_workers_needed = []
# Main Menu Construction.

while True:
    if redirect:
        Users_choice = redirect_choice
        redirect = False
    else:
        print("XYZ COMPANY")
        print("Main Menu")
        print("")
        print("1. Add a new project to existing projects.")
        print("2. Remove a completed project from existing projects.")
        print("3. Add new workers to available workers group.")
        print("4. Update details on ongoing Projects.")
        print("5. Project statistics.")
        print("6. Exist.")
        print("")
        Users_choice = int(input("Enter your choice:"))

    # Add a new project.(OPTION 1).

    if Users_choice == 1:
        print("XYZ COMPANY")
        print("Add a New Project.")
        print("")
        print("Complete the Required Information in order to save.")
        print("Enter Project Code : 0 to go back.")

        # Asking for Details.

        project_code = int(input("Project Code:"))
        while project_code in projects_L:
            print("Already existing project code")
            project_code = int(input("Project Code:"))
        # Redireting back to main menu if project code = 0.
        if project_code == 0:
            print("Redirecting to Main Menu...")
            continue
        clients_name = str(input("Clients Name:"))
        start_date = str(input("Start Date:"))
        expected_end_date = str(input("Expected End Date"))
        number_of_workers_needed = int(input("Number of Workers Involved"))
        project_status = (
            str(input("Project Status (ongoing/onhold/completed):"))
            .lower()
            .replace(" ", "")
        )
        while project_status not in ["completed", "onhold", "ongoing"]:
            print("Invalid project status...")
            project_status = (
                str(input("Project Status (ongoing/onhold/completed):"))
                .lower()
                .replace(" ", "")
            )

        # Asking if project neededs to be saved.
        # PLACE 3
        saving_project = (
            str(input("Do you want to save project (yes/no):")).lower().replace(" ", "")
        )
        while saving_project not in ["yes", "no"]:
            print("Invalid choice..!")
            saving_project = (
                str(input("Do you want to save project (yes/no):"))
                .lower()
                .replace(" ", "")
            )
        # if project does not need to be saved.
        if saving_project == "no":
            print("Project was not saved")
            print("Redirecting to Main Menu...")
        # if project needs to be saved.
        if saving_project == "yes":
            # assinging each information to needed lists.
            projects_L.append(project_code)
            clients_name_L.append(clients_name)
            start_date_L.append(start_date)
            expected_end_date_L.append(expected_end_date)
            number_of_workers_needed_L.append(number_of_workers_needed)
            project_status_L.append(project_status)
            print("project has been saved")
        # if response is not valid.
        else:
            print("response is not valid, please enter again.")
            redirect = True
            redirect_choice = 1

        # Asked to be redirected.

    # Remove completed project.(OPTION 2).

    elif Users_choice == 2:
        print("XYZ COMPANY")
        print("Remove Completed Project.")
        print("")

        # Asking which project is completed.
        project_code = int(input("please enter project code:"))
        while project_code not in projects_L:
            print("Invalid project code")
            project_code = int(input("please enter project code:"))
        print("")

        # Asking if project needs to be removed.
        removal = str(input("Do you wish to remove Project(yes/no)"))
        while removal not in ["yes", "no"]:
            print("Invalid choice..!")
            removal = (
                str(input("Do you wish to remove Project(yes/no)"))
                .lower()
                .replace(" ", "")
            )
        # if yes
        if removal == "yes":
            # ask for end date.
            end_date = float(input("Please enter actual end date:"))

            # put information to proper completed list.
            completed_project_code.append(projects_L[project_code])
            completed_clients_name.append(clients_name_L[project_code])
            completed_start_date.append(start_date_L[project_code])
            completed_start_date.append(expected_end_date_L[project_code])
            completed_number_of_workers_needed.append(
                number_of_workers_needed_L[project_code]
            )
            actual_end_day.append(end_date)
            project_status_L[project_code] = "completed"
            # tell that completed project was removed
            print("removal of completed project was succesfull")

        # if no
        elif removal == "no":
            print("completed project removal failed")

        # if no valid response is given
        else:
            print("please enter a valid response")
            redirect = True
            redirect_choice = 2

    # Adding New Workers.(OPTION 3).

    elif Users_choice == 3:
        print("XYZ COMPANY")
        print("Adding New Workers")
        print("")

        # adding workers to the variable
        added_workers = int(input("Enter the number of workers joining the company:"))

        # confirmation process
        conformation_workers = str(
            input("Do you want to add these workers to the work force(yes/no):")
        )
        while conformation_workers not in ["yes", "no"]:
            print("Invalid choice..")
            conformation_workers = (
                str(
                    input("Do you want to add these workers to the work force(yes/no):")
                )
                .lower()
                .replace(" ", "")
            )
        # if yes.
        if conformation_workers == "yes":
            # calculation.
            Workers = Workers + added_workers
            # display answer.
            print("the total number of workers in the task force is ", Workers)

        # if no.
        elif conformation_workers == "no":
            print("the workers have not been added to the task force")

        # if no proper response is given.
        else:
            print("given answer is not valid")
            redirect = True
            redirect_choice = 3

    # Update Project Details.(OPTION 4).

    elif Users_choice == 4:
        print("XYZ COMPANY")
        print("Update Project Details")
        print("")

        # Ask for which project needs to be updated.
        project_code = int(
            input("Please enter the projects code that needs to be updated")
        )
        while project_code not in projects_L:
            print("Invalid project code")
            project_code = int(
                input("Please enter the projects code that needs to be updated")
            )
        print("")
        # ask for other details thats need to be replaced.
        client_names = str(input("Clients Name:"))
        Start_date = str(input("Start Date:"))
        expected_end_date = str(input("Expected End Day:"))
        num_of_workers_needed = int(input("Number of workers:"))
        project_status = (
            str(input("Project Status (ongoing/onhold/completed):"))
            .lower()
            .replace(" ", "")
        )
        while project_status not in ["completed", "onhold", "ongoing"]:
            print("Invalid project status...")
            project_status = (
                str(input("Project Status (ongoing/onhold/completed):"))
                .lower()
                .replace(" ", "")
            )
        print("")

        # conformation to update project.
        # PLACE 9
        conformation_update = str(input("Do you want to update the project(yes/no):"))
        while conformation_update not in ["yes", "no"]:
            print("Invalid choice..!")
            conformation_update = (
                str(input("Do you want to update the project(yes/no):"))
                .lower()
                .replace(" ", "")
            )
        # if yes
        if conformation_update == "yes":
            clients_name_L[project_code] = client_names
            start_date_L[project_code] = Start_date
            expected_end_date_L[project_code] = expected_end_date
            number_of_workers_needed_L[project_code] = num_of_workers_needed
            project_status_L[project_code] = project_status
            # displaying that it has been done.
            print("project has been updated")

        # if no
        elif conformation_update == "no":
            print("project has not been updated")

        # if no valid response is given
        else:
            print("no valid response is given")
            redirect = True
            redirect_choice = 4

    # Display project statistics.(OPTION 5).

    elif Users_choice == 5:
        print("XYZ COMPANY")
        print("Project Statistics")
        print("")

        # initialization fo calculation
        place = 0
        ongoing_num = 0
        # calculation for ongoing projects.
        while place < len(project_status_L):
            if project_status_L[place] == "ongoing":
                ongoing_num += 1
            place += 1

        # initialization fo calculation
        place = 0
        onhold_num = 0
        # calculation for ongoing projects.
        while place < len(project_status_L):
            if project_status_L[place] == "onhold":
                onhold_num += 1
            place += 1

        # initialization fo calculation
        place = 0
        completed_num = 0
        # calculation for ongoing projects.
        while place < len(project_status_L):
            if project_status_L[place] == "completed":
                completed_num += 1
            place += 1

        # print output
        print("Number of onoing projects:", ongoing_num)
        print("Number of completed projects:", onhold_num)
        print("Number of on hold projects:", completed_num)

        # find the number of employees not available
        # num of worrker needed List - num of workers used list
        # initialization for calculation
        place = 0
        num_of_workers_needed_thru_time = 0
        place_w = 0
        while place_w < len(number_of_workers_needed_L):
            if number_of_workers_needed_L[place_w] > 0:
                num_of_workers_needed_thru_time = (
                    num_of_workers_needed_thru_time + number_of_workers_needed_L[place]
                )
            place_w += 1
        place = place + 1.0

        place_w
        num_of_workers_used = 0
        while place_w < len(completed_number_of_workers_needed):
            if completed_number_of_workers_needed[place_w] > 0:
                num_of_workers_used = (
                    num_of_workers_used + completed_number_of_workers_needed[place]
                )
            place_w += 1
        place = place + 1.0

        assinged_workers = num_of_workers_needed_thru_time - num_of_workers_used

        # substract from total workforce
        available_workers = Workers - assinged_workers

        print("Number of available workers to assign:", available_workers)

    # if user decides to exit program.(OPTION 6).

    elif Users_choice == 6:
        print("XYZ COMPANY")
        print("")
        print("Have a Nice Day...")

    # if users input is not valid.

    else:
        print("Entered choice dose not eist")
        print("Please renter your choice")
        break
