# initialize the variable
import datetime

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


def testing():
    print(
        workers,
        all_projects,
        completed_projects,
        variable_of_possible_inputs,
    )


def project_status_func(
    msg: str = "Project Status (ongoing/completed/on hold) - ",
    update_status: bool = False,
) -> tuple:
    project_state = str(input(msg))
    project_state = project_state.replace(" ", "").lower()
    if project_state not in possible_inputs:
        print("The entered project status is incorrect...")
        return project_status_func()
    if update_status:
        variable_of_possible_inputs[possible_inputs.index(project_state)] += 1
    return (
        project_state,
        variable_of_possible_inputs,
        possible_inputs.index(project_state),
    )


while execute:
    print(menu)
    # Check the user choice
    your_choice = int(input("Enter your choice: "))

    # When user choice is 1
    if your_choice == 1:
        testing()
        print(
            """
            XYZ Company
            Add a new project
          """
        )
        project_code = str(input("Project Code - "))
        if project_code == "0":
            continue
        clients_name = str(input("Clients Name - "))
        start_date = str(input("Start Date - "))
        expected_end_date = str(input("Expected end date - "))
        number_of_workers = int(input("Numbers of Workers - "))
        project_status, status_list, index = project_status_func()
        save = str(input("Do you want to save the project(Yes/No)? "))
        if (save.lower() == "yes") and (number_of_workers <= workers):
            status_list[index] += 1
            project_data = [
                project_code,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ]
            project_names.append(project_code)
            all_projects.append(project_data)
            workers -= number_of_workers
            print(project_names, all_projects)
            testing()
        else:
            print("The project was *not* saved")
            testing()

    # When user choice is 2
    elif your_choice == 2:
        testing()
        print(
            """
      XYZ Company
      Remove Completed Project
    """
        )
        project_code = str(input("Project Code - "))
        save = str(input("Do you want to save the project (Yes/ No)? "))
        if (save.lower() == "yes") and (project_code in project_names):
            index_of_project = project_names.index(project_code)
            date_time = datetime.datetime.now()
            actual_end_date = date_time.strftime("%d/%m/%Y")
            (
                project_code,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ) = all_projects[index_of_project]
            completed_project_details = [
                project_code,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                actual_end_date,
            ]
            workers += number_of_workers
            variable_of_possible_inputs[index] -= 1
            variable_of_possible_inputs[1] += 1
            completed_projects.append(completed_project_details)
            del all_projects[index_of_project]
            del project_names[index_of_project]
            testing()
        else:
            print("The project was not removed...")
            testing()

    # When user choice is 3
    elif your_choice == 3:
        testing()
        print(
            """
      XYZ Company
      Add new Workers
    """
        )
        new_no_of_workers = int(input("Number Workers to Add - "))
        save = str(input("Do you want to add ? (Yes / No) "))
        if save.lower() == "yes":
            workers += new_no_of_workers
            testing()
    # When user choice is 4
    elif your_choice == 4:
        testing()
        print(
            """
      XYZ Company
      Update Project Details
    """
        )
        project_code = str(input("Project Code - "))
        if project_code == "0":
            continue
        clients_name = str(input("Clients Name - "))
        start_date = str(input("Start Date - "))
        expected_end_date = str(input("Expected end date - "))
        number_of_workers = int(input("Numbers of Workers - "))
        project_status, status_list, index = project_status_func()
        save = str(input("Do you want  too  update the project details(Yes/No)?"))
        (
            current_workers,
            _,
            previous_index,
        ) = all_projects[
            project_names.index(project_code)
        ][4:]
        if (
            (save.lower() == "yes")
            and (number_of_workers <= (workers + current_workers))
            and project_code in project_names
        ):
            status_list[index] += 1
            status_list[previous_index] -= 1
            project_data = [
                project_code,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ]
            index = project_names.index(project_code)
            all_projects[index] = project_data
            print("Data updated")
            testing()
        else:
            print(
                "There isn't enough workers"
                if number_of_workers > (workers + current_workers)
                else "There isn't a project with the mentioned project code"
            )
            testing()

    # When user choice is 5
    elif your_choice == 5:
        testing()
        print(
            """
      XYZ Company
      Project Statistics
    """
        )
        print(f"Number of ongoing projects - {variable_of_possible_inputs[0]}")
        print(f"Number of completed projects - {variable_of_possible_inputs[1]}")
        print(f"Number of On Hold Projects -  {variable_of_possible_inputs[2]}")
        print(f"Number of available workers - {workers}")
        add_project = str(input("Do you want to add the project (Yes/No)?"))  # TODO

    # When  user choice is 6
    elif your_choice == 6:
        testing()
        execute = False

    else:
        testing()
        print("Please enter a valid choice...")
