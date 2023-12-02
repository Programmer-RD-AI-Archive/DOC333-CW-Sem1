import datetime

projects = {}
workers_tracker = 0
completed_projects = {}


def add_project_code_verification(msg: str) -> str:  # TODO
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    project_code = str(input(msg))
    # get the `projects` dictionaries keys and turn it into a list and then use a for loop to go over it...
    if project_code in list(projects.keys()):
        print("Project Code already exists..!")
        # return the same function (recursion)
        return add_project_code_verification(msg)
    return project_code  # return project_code


def add_project(
    project_code: str,
    client_name: str,
    start_date: str,
    expected_end_date: str,
    num_workers: int,
    status: str,
    workers_tracker: int,
) -> int:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    status = status.lower().replace(" ", "")
    project_details = {
        "Client's Name": client_name,
        "Start Date": start_date,
        "Expected End Date": expected_end_date,
        "Number of Workers": num_workers,
        "Status": status,
    }
    if num_workers > workers_tracker:
        print("Not enough workers")
        return workers_tracker
    if status == "ongoing":
        workers_tracker = reclaim_workers(num_workers, workers_tracker)
    projects[project_code] = project_details
    return workers_tracker


def remove_project(project_code, project_list, workers_tracker):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if project_code in list(project_list.keys()):
        old_status = project_list[project_code]["Status"]
        date_time = datetime.datetime.now()
        actual_end_date = date_time.strftime("%d/%m/%Y")
        project_details = project_list[project_code]
        project_details["Actual End Date"] = actual_end_date
        completed_projects[project_code] = project_details
        if old_status == "ongoing":
            workers_tracker = release_workers(project_code, workers_tracker)
        project_details["Status"] = "completed"
        del project_list[project_code]
        print("Project removed successfully!")
    else:
        print("Project not found in the list.")
    return workers_tracker, project_list


def add_workers(num_workers, workers_tracker):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    workers_tracker += num_workers
    print(f"{num_workers} new workers added successfully!")
    return workers_tracker


def update_ongoing_project(project_code, workers_tracker, project_list):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print("1. Update Client's Name")
    print("2. Update Start Date")
    print("3. Update Expected End Date")
    print("4. Update Number of Workers")
    print("5. Update Project Status")
    update_choice = input("Enter the number corresponding to the detail to update: ")
    if update_choice == "1":
        new_client_name = input("Enter new Client's Name: ")
        projects[project_code]["Client's Name"] = new_client_name
        print("Client's Name updated successfully!")
    elif update_choice == "2":
        new_start_date = input("Enter new Start Date (YYYY-MM-DD): ")
        projects[project_code]["Start Date"] = new_start_date
        print("Start Date updated successfully!")
    elif update_choice == "3":
        new_expected_end_date = input("Enter new Expected End Date (YYYY-MM-DD): ")
        projects[project_code]["Expected End Date"] = new_expected_end_date
        print("Expected End Date updated successfully!")
    elif update_choice == "4":
        new_num_workers = int(input("Enter new Number of Workers: "))
        workers_tracker = (
            workers_tracker
            + projects[project_code]["Number of Workers"]
            - new_num_workers
        )
        projects[project_code]["Number of Workers"] = new_num_workers
        print("Number of Workers updated successfully!")
    elif update_choice == "5":
        new_status = (
            input("Enter new Project Status (ongoing, on hold, completed): ")
            .lower()
            .replace(" ", "")
        )
        old_status = projects[project_code]["Status"]
        projects[project_code]["Status"] = new_status
        if new_status == "onhold" and old_status != new_status:
            workers_tracker = release_workers(
                project_code,
                workers_tracker,
            )
        if (
            new_status == "ongoing"
            and old_status == "onhold"
            and old_status != new_status
        ):
            workers_tracker = reclaim_workers(
                projects[project_code]["Number of Workers"], workers_tracker
            )
        if new_status == "completed":
            workers_tracker, project_list = remove_project(
                project_code, project_list, workers_tracker, old_status
            )
        if old_status == "completed":
            del completed_projects[project_code]
        print("Project Status updated successfully!")
    else:
        print("Invalid update choice.")
    return workers_tracker


def reclaim_workers(num_workers_reclained, workers_tracker):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    workers_tracker -= num_workers_reclained
    return workers_tracker


def release_workers(project_code, workers_tracker):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    num_workers_released = projects[project_code]["Number of Workers"]
    workers_tracker += num_workers_released
    return workers_tracker


def project_statistics(workers_tracker):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    num_ongoing = 0
    num_completed = 0
    num_on_hold = 0
    for project in projects.values():
        if project["Status"] == "onhold":
            num_on_hold += 1
        elif project["Status"] == "completed":
            num_completed += 1
        else:
            num_ongoing += 1
    print(f"\nNumber of Ongoing Projects: {num_ongoing}")
    print(f"Number of Completed Projects: {len(completed_projects) + num_completed}")
    print(f"Number of On Hold Projects: {num_on_hold}")
    print(f"Number of Available Workers to Assign: {workers_tracker}")
    wanna_add_project = str(input("Do you want to add a new project (Yes/No)?: "))
    if wanna_add_project.lower().replace(" ", "") == "yes":
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
    print("XYZ Company".center(100))
    print("Main Menu".center(100))
    print("\n1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project statistics")
    print("6. Exit")

    choice = input("\t \t \t Enter your choice:")

    if choice == "1":
        print("XYZ Company".center(100))
        print("Add a new project".center(100))
        project_code = add_project_code_verification("Enter Project Code: ")
        if project_code == "0":
            continue
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

    elif choice == "2":
        print("XYZ Company".center(100))
        print("Remove Completed Project".center(100))
        project_code = input("Enter Project Code to remove from ongoing projects: ")
        save = str(input("Do you want to remove the project (Yes/No)?: "))
        if save.lower().replace(" ", "") == "yes":
            workers_tracker, projects = remove_project(
                project_code, projects, workers_tracker
            )

    elif choice == "3":
        print("XYZ Company".center(100))
        print("Add workers".center(100))
        num_new_workers = int(input("Enter the number of new workers to add: "))
        save = str(input("Do you want to add the workers (Yes/No)?: "))
        if save.lower().replace(" ", "") == "yes":
            workers_tracker = add_workers(num_new_workers, workers_tracker)

    elif choice == "4":
        print("XYZ Company".center(100))
        print("update project".center(100))
        project_code = input(
            "Enter Project Code to update details (Enter '0' to cancel): "
        )
        save = str(input("Do you want to update the project (Yes/No)?: "))
        if (
            project_code == "0"
            or project_code not in list(projects.keys())
            or save.lower().replace(" ", "") == "no"
        ):
            continue
        else:
            workers_tracker = update_ongoing_project(
                project_code, workers_tracker, projects
            )

    elif choice == "5":
        print("XYZ Company".center(100))
        print("Project Statistics".center(100))
        project_statistics(workers_tracker)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
