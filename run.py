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
redirect_choice = False
redirect_to = None


def menu(
    redirect: bool = False,
    to: int = None,
    name_of_the_company: str = company_name,
    msg: str = "Enter your choice: ",
) -> str:
    """This function finds the choice that should be displayed to the user next...

    Keyword arguments:
    redirect (bool) -- A boolean to know whether or not the user will be redirected
    to (int) -- The choice that user will be redirected to
    name_of_the_company (str) -- The companies name that will be displayed
    msg (str) -- The message that will be displayed to the user asking their next choice

    Return: (str) the next choice which the user has chosen...
    """
    main_menu = f"""
     {name_of_the_company}
     Main Menu
     1. Add a new project to existing projects.
     2. Remove a completed project from existing projects.
     3. Add new workers to available workers group.
     4. Updates details on ongoing projects.
     5. Project statics.
     6. Exit
    """
    print("Redirecting..." if redirect else main_menu)
    return to if redirect else str(input(msg))


class Projects:
    @staticmethod
    def remove_completed_projects(
        code_of_project: str,
        every_project: list,
        workers_tot: int,
        stats_list: list,
        complete_projects: list,
        possible_stats: list,
    ) -> Tuple[bool, str]:
        """Remove completed projects

        Keyword arguments:
        code_of_project (str) -- The code of the project that will be removed
        every_project (list) -- A list which contains all the projects which haven't been removed
        workers_tot (int) -- The number of workers
        stats_list (list) -- The list that tracks the statistics for choice (5)
        complete_projects (list) -- The list which contains all removed completed projects
        possible_stats (list) -- All the possible status

        Return: Tuple[A boolean which states whether or not the operation was successful, A string which has an output msg regarding the operation if it was successful or not.]
        """
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
                _,
                index,
            ) = every_project[index_of_project]
            completed_project_details = [
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                actual_end_date,
            ]
            workers_tot += number_of_workers
            stats_list[index] -= 1
            stats_list[possible_stats.index("completed")] += 1
            complete_projects.append(completed_project_details)
            del every_project[index_of_project]
            del project_names[index_of_project]
            return (True, "Successfully removed completed projects.", workers_tot)
        except Exception as e:
            return (False, e, workers_tot)

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
        workers_tot: int,
        every_project: list,
        stats_list: list,
        possible_stats: list,
    ) -> Tuple[bool, str]:
        """This function creates a new project

        Keyword arguments:
        status_list (list) -- The list that is used for project statistics
        index (index) -- The index of the project status in the status list
        code_of_project (str) -- The code of the project
        clients_name (str) -- The project's clients name
        start_date (str) -- The start date of the project
        expected_end_date (str) -- The expected end date of the project
        number_of_workers (str) -- The number of workers required for the project
        project_status (str) -- The status of the project out of (ongoing,on hold, completed)
        workers_tot (int) -- total number of workers in the organization
        every_project (list) -- A list which contains all the projects which haven't been removed
        stats_list (list) -- The list that tracks the statistics for choice (5)
        possible_stats (list) -- All the possible status

        Return: Tuple[
            A boolean which shows if the function successfully executed or not,
            The message which will be displayed to the user
        ]
        """
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
            return (True, "Successfully created a new project", workers_tot)
        except Exception as e:
            return (False, e, workers_tot)

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
        current_workers: int,
        workers_tot: int,
    ) -> Tuple[bool, str]:
        """An function that updates the project details

        Keyword arguments:
        status_list (list) -- The list that is used for project statistics
        index (int) -- The index of the new project status in the status_list
        previous_index (int) -- The index of the previous project status in the status_list
        code_of_project (str) -- The project code of the project
        clients_name (str) -- The (updated / usual) client name
        start_date (str) -- The (updated / usual) start date
        expected_end_date (str) -- The (updated / usual) end date
        number_of_workers (str) -- The (updated / usual) number of workers
        project_status (str) -- The (updated / usual) project status
        current_workers (int) -- The number of workers before the project was updated
        workers_tot (int) -- The total number of workers

        Return: Tuple[
            A boolean which shows if the function successfully executed or not,
            The message which will be displayed to the user
        ]
        """
        try:
            workers_tot += current_workers
            workers_tot -= number_of_workers
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
            return (True, "Project details updated successfully", workers_tot)
        except Exception as e:
            return (False, e, workers_tot)


class Verification:
    def date_verification(self, msg: str) -> str:
        """A function that uses recursion to make sure that the entered date is in a correct format...

        Keyword arguments:
        msg (str) -- the message that should be displayed...
        Return: A string which contains a correct date format...
        """
        date = input(msg)
        splitted_date = date.split(date[2] if len(date) > 3 else " ")
        if len(splitted_date) != 3:
            print("Enter a valid format of the date..!")
            return self.date_verification(msg)
        month, date, _ = splitted_date[0], splitted_date[1], splitted_date[2]
        if int(month) > 12:
            print("Enter a valid month..!")
            return self.date_verification(msg)
        if int(date) > 31:
            print("Enter a valid date..!")
            return self.date_verification(msg)
        return date

    def project_status_verification(
        self,
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
            return self.project_status_verification()
        if update_status:
            statistics_list[possible_inputs.index(project_state)] += 1
        return (
            project_state,
            statistics_list,
            possible_inputs.index(project_state),
        )

    def project_code_verification(self, msg: str, project_codes: list) -> str:
        """Project Code Verification function with the use of recursion...

        Keyword arguments:
        msg (str) -- The message that is displayed and ask the user to enter the project code
        project_codes (list) -- The list of project codes that already exists

        Return: (str) of a project code that doesnt already exist...
        """
        project_code = str(input(msg))
        if project_code in project_codes:
            print("Project Code already exists..!")
            return self.project_code_verification(msg, project_codes)
        return project_code


while execute:
    choice = menu(redirect=redirect_choice, to=redirect_to)
    redirect_choice, redirect_to = False, None
    if choice == "1":
        print(
            f"""
            {company_name}
            Add a new project
          """
        )
        code_of_project = Verification().project_code_verification(
            "Project Code : ", project_names
        )
        if code_of_project == "0":
            continue
        clients_name = str(input("Clients Name : "))
        start_date = Verification().date_verification("Start Date (MM/DD/YYYY) : ")
        expected_end_date = Verification().date_verification(
            "Expected end date (MM/DD/YYYY) : "
        )
        number_of_workers = int(input("Numbers of Workers : "))
        (
            project_status,
            status_list,
            index,
        ) = Verification().project_status_verification()
        save = str(input("Do you want to save the project(Yes/No)? "))
        if (number_of_workers <= workers) and (save.upper() == "YES"):
            execution_status, response_msg, workers = Projects().create_project(
                status_list,
                index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                workers,
                all_projects,
                statistics_list,
                possible_inputs,
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
            (
                execution_status,
                response_msg,
                workers,
            ) = Projects().remove_completed_projects(
                code_of_project,
                all_projects,
                workers,
                statistics_list,
                completed_projects,
                possible_inputs,
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
        if save.upper() == "YES" and new_no_of_workers > 0:
            workers += new_no_of_workers
            print("Workers added successfully..!")
        else:
            print(
                "Workers must be more than 0..!"
                if workers <= 0
                else "Workers were not added..!"
            )

    elif choice == "4":
        print(
            f"""
      {company_name}
      Update Project Details
    """
        )
        code_of_project = str(input("Project Code : "))
        if code_of_project.replace(" ", "") == "0":
            continue
        clients_name = str(input("Clients Name : "))
        start_date = Verification().date_verification("Start Date (MM/DD/YYYY) : ")
        expected_end_date = Verification().date_verification(
            "Expected end date (MM/DD/YYYY) : "
        )
        number_of_workers = int(input("Numbers of Workers : "))
        (
            project_status,
            status_list,
            index,
        ) = Verification().project_status_verification()
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
            execution_status, response_msg, workers = Projects().update_project_details(
                status_list,
                index,
                previous_index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                current_workers,
                workers,
                possible_inputs,
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
        add_project = str(input("Do you want to add the project (Yes/No)?"))
        if add_project.upper() == "YES":
            redirect_choice, redirect_to = True, "1"

    elif choice == "6":
        execute = False

    else:
        print("Please enter a valid choice..!")
