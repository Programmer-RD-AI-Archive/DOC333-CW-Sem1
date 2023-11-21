import datetime
from typing import Tuple

company_name = "XYZ Company"
workers = 0
choice = 0
all_projects = []
completed_projects = []
execute = True
project_names = []
possible_inputs = ["ongoing", "completed", "onhold"]
statistics_list = [0] * len(possible_inputs)


class Projects:
    @staticmethod
    def remove_completed_projects(code_of_project: str) -> Tuple[bool, str]:
        try:
            index_of_project = project_names.index(code_of_project)
            date_time = datetime.datetime.now()
            actual_end_date = date_time.strftime("%m/%d/%Y")
            (
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ) = all_projects[index_of_project]
            completed_project_details = [
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                actual_end_date,
            ]
            workers += number_of_workers
            statistics_list[index] -= 1
            statistics_list[1] += 1
            completed_projects.append(completed_project_details)
            del all_projects[index_of_project]
            del project_names[index_of_project]
            return (True, "Successfully removed completed projects...")
        except Exception as e:
            return (False, e)

    @staticmethod
    def create_project(
        status_list: list,
        index: int,
        code_of_project: str,
        clients_name: str,
        start_date: str,
        expected_end_date: str,
        number_of_workers: str,
        project_status: str,
    ) -> Tuple[bool, str]:
        try:
            status_list[index] += 1
            project_data = [
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ]
            project_names.append(code_of_project)
            all_projects.append(project_data)
            workers -= number_of_workers
            return (True, "Successfully created a new project...")
        except Exception as e:
            return (False, e)

    @staticmethod
    def update_project_details(
        status_list: list,
        index: int,
        previous_index: int,
        code_of_project: str,
        clients_name: str,
        start_date: str,
        expected_end_date: str,
        number_of_workers: str,
        project_status: str,
    ) -> Tuple[bool, str]:
        try:
            status_list[index] += 1
            status_list[previous_index] -= 1
            project_data = [
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                index,
            ]
            index = project_names.index(code_of_project)
            all_projects[index] = project_data
            return (True, "Project details updated successfully...")
        except Exception as e:
            return (False, e)


def menu(company_name: str = company_name, msg: str = "Enter your choice: ") -> str:
    menu = f"""
     {company_name}
     Main Menu
     1. Add a new project to existing projects.
     2. Remove a completed project from existing projects.
     3. Add new workers to available workers group.
     4. Updates details on ongoing projects.
     5. Project statics.
     6. Exit
    """
    print(menu)
    choice = str(input(msg))
    return choice


def enter_project_status(
    msg: str = "Project Status (ongoing/completed/on hold) : ",
    update_status: bool = False,
) -> Tuple[str, list, int]:
    """An function that uses recursion to make sure that an input is enter as required

    Keyword arguments:
    msg -- The message that should be displayed to the user to get the project status input
    update_status -- Whether to update the status count

    Return: Tuple[The state enter by the user,
                    the statistic list used to track the project status count,
                    the index of the enter state
                ]
    """
    project_state = str(input(msg)).replace(" ", "").lower()
    if project_state not in possible_inputs:
        print("The entered project status is incorrect...")
        return enter_project_status()
    if update_status:
        statistics_list[possible_inputs.index(project_state)] += 1
    return (
        project_state,
        statistics_list,
        possible_inputs.index(project_state),
    )


while execute:
    choice = menu()
    if choice == "1":
        print(
            f"""
            {company_name}
            Add a new project
          """
        )
        code_of_project = str(input("Project Code : "))
        if code_of_project == "0":
            continue
        clients_name = str(input("Clients Name : "))
        start_date = str(input("Start Date : "))
        expected_end_date = str(input("Expected end date : "))
        number_of_workers = int(input("Numbers of Workers : "))
        project_status, status_list, index = enter_project_status()
        save = str(input("Do you want to save the project(Yes/No)? "))
        if (number_of_workers <= workers) and (save.upper() == "YES"):
            execution_status, response_msg = Projects().create_project(
                status_list,
                index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
            )
            print(f"{response_msg} ({execution_status})")
        else:
            print(
                "The project was *not* saved ..!"
                if save.upper() != "YES"
                else "There isnt enough workers available..!"
            )

    elif choice == "2":
        print(
            f"""
      {company_name}
      Remove Completed Project
    """
        )
        code_of_project = str(input("Project Code : "))
        save = str(input("Do you want to save the project (Yes/ No)? "))
        if (code_of_project in project_names) and (save.upper() == "YES"):
            execution_status, response_msg = Projects().remove_completed_projects(
                code_of_project
            )
            print(f"{response_msg} ({execution_status})")
        else:
            print(
                "The project was not removed..!"
                if save.upper() != "YES"
                else "The project does not exist..!"
            )

    elif choice == "3":
        print(
            f"""
      {company_name}
      Add new Workers
    """
        )
        new_no_of_workers = int(input("Number Workers to Add : "))
        save = str(input("Do you want to add ? (Yes / No) "))
        if save.upper() == "YES":
            workers += new_no_of_workers
            print("Workers added successfully..!")
        else:
            print("Workers were not added..!")

    elif choice == "4":
        print(
            f"""
      {company_name}
      Update Project Details
    """
        )
        code_of_project = str(input("Project Code : "))
        if code_of_project == "0":
            continue
        clients_name = str(input("Clients Name : "))
        start_date = str(input("Start Date : "))
        expected_end_date = str(input("Expected end date : "))
        number_of_workers = int(input("Numbers of Workers : "))
        project_status, status_list, index = enter_project_status()
        save = str(input("Do you want to update the project details (Yes/No)?"))
        (
            current_workers,
            _,
            previous_index,
        ) = all_projects[
            project_names.index(code_of_project)
        ][4:]
        if (
            (number_of_workers <= (workers + current_workers))
            and save.upper() == "YES"
            and code_of_project in project_names
        ):
            execution_status, response_msg = Projects().update_project_details(
                status_list,
                index,
                previous_index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
            )
            print(f"{response_msg} ({execution_status})")
        else:
            print(
                "There isn't enough workers..!"
                if number_of_workers > (workers + current_workers)
                else "There isn't a project with the mentioned project code..!"
            )

    # When user choice is 5
    elif choice == "5":
        print(
            f"""
      {company_name}
      Project Statistics
    """
        )
        for idx, item in enumerate(possible_inputs):
            print(f"Number of {item} projects : {statistics_list[idx]}")
        print(f"Number of available workers : {workers}")
        add_project = str(input("Do you want to add the project (Yes/No)?"))  # TODO

    elif choice == "6":
        execute = False

    else:
        print("Please enter a valid choice..!")
