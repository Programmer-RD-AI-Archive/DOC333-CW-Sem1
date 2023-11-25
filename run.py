from Corporation import *

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
