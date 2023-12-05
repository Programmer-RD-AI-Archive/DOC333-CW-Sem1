import datetime

# initalization of variables
projects = {}
workers_tracker = 0
completed_projects = {}


def add_project_code_verification(msg):
    project_code = str(input(msg))
    # get the `projects` dictionaries keys and turn it into a list and then use a for loop to go over it...
    if project_code in list(projects.keys()):
        print("Project Code already exists..!")
        # return the same function (recursion)
        return add_project_code_verification(msg)
    return project_code  # return project_code


def add_project(
    project_code,
    client_name,
    start_date,
    expected_end_date,
    num_workers,
    status,
    workers_tracker,
):
    status = status.lower().replace(
        " ", ""
    )  # lower and replace " " with "" of the parameter (status)
    project_details = {
        "Client's Name": client_name,
        "Start Date": start_date,
        "Expected End Date": expected_end_date,
        "Number of Workers": num_workers,
        "Status": status,
    }  # create a dictionary called project_details with the paramaters
    if num_workers > workers_tracker:  # checking if there are enough workers
        print("Not enough workers")
        return workers_tracker
    if status == "ongoing":  # checking if the status is "ongoing"
        workers_tracker = reclaim_workers(
            num_workers, workers_tracker
        )  # claim workers meaning assign the workers to the project by subtracting them from the total worker count
    projects[
        project_code
    ] = project_details  # assigning the project_details to the project_code in the dictionary projects
    return workers_tracker


def remove_project(project_code, project_list, workers_tracker):
    if project_code in list(
        project_list.keys()
    ):  # checking if the project_code is in the list(of the project_codes keys)
        old_status = project_list[project_code][
            "Status"
        ]  # assign the project status before updating it to a varaible called `old_status`
        date_time = datetime.datetime.now()  # getting the current date at this time
        actual_end_date = date_time.strftime(
            "%d/%m/%Y"
        )  # getting the date in a format that we want
        project_details = project_list[
            project_code
        ]  # geting the current project details
        project_details[
            "Actual End Date"
        ] = actual_end_date  # updating the actual end date
        completed_projects[
            project_code
        ] = project_details  # assigning the project code to the project details
        if old_status == "ongoing":  # checking if the old status is ongoing
            workers_tracker = release_workers(
                project_code, workers_tracker
            )  # remove the workers using the `release_workers`
        project_details["Status"] = "completed"  # changing the status to "completed"
        del project_list[
            project_code
        ]  # deleting the project details from the `project_list`
        print("Project removed successfully!")
    else:
        print("Project not found in the list.")
    return (
        workers_tracker,
        project_list,
    )  # retruning the workers_tracker, project_list variables


def add_workers(num_workers, workers_tracker):
    workers_tracker += (
        num_workers  # adding the enterd num_workers to the workers_tracker variable
    )
    print(f"{num_workers} new workers added successfully!")
    return workers_tracker  # return the worker_tracker variable


def update_ongoing_project(project_code, workers_tracker, project_list):
    # printing the possible updating possibilities
    print("1. Update Client's Name")
    print("2. Update Start Date")
    print("3. Update Expected End Date")
    print("4. Update Number of Workers")
    print("5. Update Project Status")
    # inputing the choice between 1 - 5
    update_choice = input("Enter the number corresponding to the detail to update: ")
    if update_choice == "1":  # checking if the choice is "1"
        new_client_name = input("Enter new Client's Name: ")
        projects[project_code]["Client's Name"] = new_client_name
        print("Client's Name updated successfully!")
    elif update_choice == "2":  # checking if the choice is "2"
        new_start_date = input("Enter new Start Date (YYYY-MM-DD): ")
        projects[project_code]["Start Date"] = new_start_date
        print("Start Date updated successfully!")
    elif update_choice == "3":  # checking if the choice is "3"
        new_expected_end_date = input("Enter new Expected End Date (YYYY-MM-DD): ")
        projects[project_code]["Expected End Date"] = new_expected_end_date
        print("Expected End Date updated successfully!")
    elif update_choice == "4":  # checking if the choice is "4"
        new_num_workers = int(input("Enter new Number of Workers: "))
        workers_tracker = (
            workers_tracker
            + projects[project_code]["Number of Workers"]
            - new_num_workers
        )
        projects[project_code]["Number of Workers"] = new_num_workers
        print("Number of Workers updated successfully!")
    elif update_choice == "5":  # checking if the choice is "5"
        new_status = (
            input("Enter new Project Status (ongoing, on hold, completed): ")
            .lower()
            .replace(" ", "")
        )  # asking the user for the new status
        old_status = projects[project_code]["Status"]  # geting the old status
        projects[project_code][
            "Status"
        ] = new_status  # updating the new status to the varaible
        if (
            new_status == "onhold" and old_status != new_status
        ):  # checking if the new status is onhold and the old status is not the same as the old status
            # releasing workers using the `release_workers` method
            workers_tracker = release_workers(
                project_code,
                workers_tracker,
            )
        if (
            new_status == "ongoing"
            and old_status == "onhold"
            and old_status != new_status
        ):  # checking if the new status is ongoing and old status is onhold and that the old status is not the same as the new status
            # reclaiming workers using the the `reclaim_workers` method
            workers_tracker = reclaim_workers(
                projects[project_code]["Number of Workers"], workers_tracker
            )
        if new_status == "completed":  # checking if the new status is completed
            # using the remove project function to remove the project
            workers_tracker, project_list = remove_project(
                project_code, project_list, workers_tracker, old_status
            )
        if old_status == "completed":  # checking if the old status is completed
            # removing the completed project from the completed_projects from the dictionary
            del completed_projects[project_code]
        print("Project Status updated successfully!")
    else:
        print("Invalid update choice.")
    return workers_tracker


def reclaim_workers(num_workers_reclained, workers_tracker):
    workers_tracker -= num_workers_reclained  # remove the num_workers_reclained workers
    return workers_tracker


def release_workers(project_code, workers_tracker):
    num_workers_released = projects[project_code][
        "Number of Workers"
    ]  # getting the number of workers in the project
    workers_tracker += num_workers_released  # adding that workers that are in the project to the worker tracker variable
    return workers_tracker


def project_statistics(workers_tracker):
    num_ongoing = 0
    num_completed = 0
    num_on_hold = 0
    for (
        project
    ) in projects.values():  # going through the values of the `projects` dictionary
        if project["Status"] == "onhold":  # checking if the status is "onhold"
            num_on_hold += 1
        elif project["Status"] == "completed":  # checking if the status is "completed"
            num_completed += 1
        else:  # if the status is neither "onhold" nor "completed"
            num_ongoing += 1
    # printing the statistics
    print(f"\nNumber of Ongoing Projects: {num_ongoing}")
    print(f"Number of Completed Projects: {len(completed_projects) + num_completed}")
    print(f"Number of On Hold Projects: {num_on_hold}")
    print(f"Number of Available Workers to Assign: {workers_tracker}")
    wanna_add_project = str(
        input("Do you want to add a new project (Yes/No)?: ")
    )  # checking if the user wants to add another project
    if (
        wanna_add_project.lower().replace(" ", "") == "yes"
    ):  # checking if the user said that they want to add a new project
        print("XYZ Company".center(100))
        print("Add a new project".center(100))
        project_code = add_project_code_verification("Enter Project Code: ")
        client_name = input("Enter Client's Name: ")
        start_date = input("Enter Start Date (DD/MM/YYYY): ")
        end_date = input("Enter Expected End Date (DD/MM/YYYY): ")
        num_workers = int(input("Enter Number of Workers: "))
        status = input("Enter Project Status (ongoing, onhold, completed): ")
        save = str(input("Do you want to add the project (Yes/No)?: "))
        if save.lower().replace(" ", "") == "yes":
            workers_tracker = add_project(
                project_code,
                client_name,
                start_date,
                end_date,
                num_workers,
                status,
                workers_tracker,
            )


while True:
    # print the menu
    print("XYZ Company".center(100))
    print("Main Menu".center(100))
    print("\n1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project statistics")
    print("6. Exit")

    choice = input("\t \t \t Enter your choice:")  # asking the user for their choice

    if choice == "1":  # checking if the choice is "1"
        print("XYZ Company".center(100))
        print("Add a new project".center(100))
        project_code = add_project_code_verification("Enter Project Code: ")
        if project_code == "0":  # checking if the project code is 0
            continue  # using this we can skip over the loop
        # inputing the required inforamtion
        client_name = input("Enter Client's Name: ")
        start_date = input("Enter Start Date (DD/MM/YYYY): ")
        end_date = input("Enter Expected End Date (DD/MM/YYYY): ")
        num_workers = int(input("Enter Number of Workers: "))
        status = input("Enter Project Status (ongoing, onhold, completed): ")
        save = str(input("Do you want to add the project (Yes/No)?: "))
        if save.lower().replace(" ", "") == "yes":  # checking if the save is the report
            workers_tracker = add_project(
                project_code,
                client_name,
                start_date,
                end_date,
                num_workers,
                status,
                workers_tracker,
            )

    elif choice == "2":  # checking if the choice is "2"
        print("XYZ Company".center(100))
        print("Remove Completed Project".center(100))
        project_code = input(
            "Enter Project Code to remove from ongoing projects: "
        )  # entering the project code
        save = str(
            input("Do you want to remove the project (Yes/No)?: ")
        )  # checking if the user wants to remove the project
        if (
            save.lower().replace(" ", "") == "yes"
        ):  # lowering the `save` varaibel and replacing " " with ""
            workers_tracker, projects = remove_project(
                project_code, projects, workers_tracker
            )  # calling the remove project function to remove the project

    elif choice == "3":  # checking if the choice is "3"
        print("XYZ Company".center(100))
        print("Add workers".center(100))
        num_new_workers = int(
            input("Enter the number of new workers to add: ")
        )  # inputing the number of workers required to add
        save = str(input("Do you want to add the workers (Yes/No)?: "))
        if (
            save.lower().replace(" ", "") == "yes"
        ):  # removing the " " with "" and lowering the `save`
            workers_tracker = add_workers(
                num_new_workers, workers_tracker
            )  # calling the function `add_workers`

    elif choice == "4":  # checking if the choice is "4"
        print("XYZ Company".center(100))
        print("update project".center(100))
        project_code = input(
            "Enter Project Code to update details (Enter '0' to cancel): "
        )  # entering the project code
        save = str(input("Do you want to update the project (Yes/No)?: "))
        if (
            project_code == "0"
            or project_code not in list(projects.keys())
            or save.lower().replace(" ", "") == "no"
        ):  # checking if the project code == "0" or if the project code not in the projecs.keys() list or the save enterd is "no"
            continue  # if the above condtions are true (or even one of em) then the loop is continued
        else:
            workers_tracker = update_ongoing_project(
                project_code, workers_tracker, projects
            )  # calls the `update_ongoing_project` method

    elif choice == "5":  # checking if the choice is "5"
        print("XYZ Company".center(100))
        print("Project Statistics".center(100))
        project_statistics(
            workers_tracker
        )  # calling the `project_statistics` function`

    elif choice == "6":  # checking if the choice is "6"
        print("Exiting...")
        break  # breaking free from the loop

    else:  # checking if the choice is not "1","2","3","4","5","6"
        print("Invalid choice. Please enter a valid option.")
