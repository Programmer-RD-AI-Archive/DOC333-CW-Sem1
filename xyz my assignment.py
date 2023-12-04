# initialize the variables
available_workers = 200
new_projects = []
ongoing_projects = []
completed_projects = []
on_hold_projects = []
project = []
inputs = ["ongoing", "completed", "on hold"]

# creating main menu
while True:
    print("XYZ Company  \nmain menu")
    print("1. Add a new project to existing new projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add a new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project statistics")
    print("6. Exit")

    your_choice = int(input("enter your choice :"))

    # process

    # when user choice is 1
    if your_choice == 1:
        print(
            "                                                XYZ Company \n                                             Add a New Project"
        )
        project_code = input("Project code(Enter '0' to exit) - ")

        if project_code == "0":
            continue

        client_name = input("Client name - ")
        start_date = input("Start date - ")
        end_date = input("Expected end date - ")
        number_of_workers = int(input("Number of workers - "))
        if number_of_workers > available_workers:
            print("Not Enough workers to assigne")
        elif number_of_workers < available_workers:
            available_workers = available_workers - number_of_workers
        project_status = input("Project status(ongoing/on hold/completed) - ")

        save = str(input("do you want to save the project(Yes/No)?")).lower()
        if save == "yes":
            # new_projects.append(project_code)
            # new_projects.append(client_name)
            # new_projects.append(start_date)
            # new_projects.append(end_date)
            # new_projects.append(number_of_workers)
            # new_projects.append(project_status)
            new_projects = [
                project_code,
                client_name,
                start_date,
                end_date,
                number_of_workers,
                project_status,
            ]
            if project_status.lower().replace(" ", "") == "ongoing":
                ongoing_projects.append(new_projects)
            elif project_status.lower().replace(" ", "") == "completed":
                completed_projects.append(new_projects)
            else:
                ongoing_projects.append(new_projects)
                on_hold_projects.append(new_projects)
            print("Project saved successfully!")
            print(new_projects)
        else:
            print("Project not saved.")

    # when user choice is 2

    elif your_choice == 2:
        print(
            "                                         XYZ Company \n                                      Remove Completed Project"
        )
        project_code_to_remove = input("project code - ")
        remove_project = str(
            input("Do you want to remove the project (Yes/No)?")
        ).lower()
        if remove_project == "yes":
            for project in ongoing_projects:
                if project[0] == project_code_to_remove:
                    completed_projects.append(project)
                    available_workers = available_workers + project[4]
                    ongoing_projects.remove(project)
                    print("Project removed successfully!")
                    break
            else:
                print("Project not found in ongoing projects.")
        else:
            print("Project not removed.")

    # when user choice is 3

    elif your_choice == 3:
        print(
            "                                  XYZ Company\n                                Add new workers"
        )
        workers_to_add = int(input("Number of workers to add - "))
        add_workers = input("Do you want to add (Yes/No)?").lower()
        if add_workers == "yes":
            available_workers = available_workers + workers_to_add
            print("workers added successfully!")
        else:
            print("Workers not added.")

    # when user choice is 4
    elif your_choice == 4:
        print(
            "                                         XYZ Company\n                                    Update Project Details"
        )
        project_code = int(input("enter the project code(Enter '0' to exit) - "))
        # Exit the loop if '0' is entered
        if project_code == 0:
            continue
        if not project_code.isdigit():
            print("Please enter the integer for the project code.")
            continue

        for project in ongoing_projects:
            if project == project_code:
                print("Current Details - ")
                print(project)
                clients_name = input("Clients Name - ")
                start_date = input("start date - ")
                end_date = input("Expected end date - ")
                number_of_workers = int(input("Number of workers - "))
                project_status = input("Project status(ongoing/on hold/completed) - ")
                update_project = input(
                    "Do you want to update the project details (Yes/No)? "
                ).lower()
                if update_project == "yes":
                    available_workers = available_workers + workers_to_add
                    print("Project details updated successfully.")
                break
        else:
            print("Project not found in ongoing projects.")

    # when user choice is 5
    elif your_choice == 5:
        print(
            "                                XYZ Company \n                              Project Statistics"
        )
        print("Number of ongoing projects:", len(ongoing_projects))
        print("Number of completed projects:", len(completed_projects))
        print("Number of on hold projects:", len(on_hold_projects))
        print("Number of available workers to assign:", available_workers)

        add_project = input("Do you want to add a project (Yes/No)? ").lower()
        if add_project == "yes":
            project_code = input("Project code - ")
            client_name = input("Client's Name - ")
            start_date = input("Start Date - ")
            end_date = input("Expected End Date - ")
            number_of_workers = int(input("Number of Workers - "))
            actual_end_date = input("Actual End Date - ")
            new_projects = [
                project_code,
                client_name,
                start_date,
                end_date,
                number_of_workers,
                actual_end_date,
            ]
            completed_projects.append(new_projects)

    elif your_choice == 6:
        exit()  # exit the loop

    else:
        print("Please enter a valid choice...")
        continue
