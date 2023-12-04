pro_code = 0
cli_Name = 0
str_date = 0
exp_end_date = 0
num_of_workers = 0
pro_status = 0
pro_save = []
project_details = []
projects = []
codes_of_projects = []
avl_workers_list = []
remove = 0
add_workers = 0
total_workers = 0
avl_workers = 0
update = 0
num_of_ongoing_pro = 0
num_of_com_pro = 0
num_of_onnhold_pro = 0


while True:
    print(
        """
            
                           XYZ Company
                            Main Menu
          
    1. Add a new project to existing projects.
    2. Remove a completed project from existing projects.
    3. Add new workers to available workers group.
    4. Update details on ongoing projects.
    5. Project Statistics
    6. Exit
            """
    )

    # Get the choice

    your_choice = str(input("Enter Your Choice - "))

    # If the choice is 1

    if your_choice == "1":
        print(
            """            XYZ Company
                         Add A New Project     """
        )

        pro_code = str(input("enter the project code - "))
        cli_Name = str(input("enter the client name - "))
        str_date = str(input("enter the start date - "))
        exp_end_date = input("enter the expected end date - ")
        num_of_workers = int(input("enter the number of workers - "))
        pro_status = (
            input("enter the project status(ongoing / completed / hold) ")
            .lower()
            .replace(" ", "")
        )
        pro_save = (
            input("Do you want to save the project? (yes/no) ").lower().replace(" ", "")
        )

        # if the user enter 'yes'

        if (pro_save == "yes") and int(avl_workers >= num_of_workers):
            print("we can accept your project")
            project_details = [
                pro_code,
                cli_Name,
                str_date,
                exp_end_date,
                num_of_workers,
                pro_status,
            ]
            if pro_status == "ongoing":
                num_of_ongoing_pro = num_of_ongoing_pro + 1
            if pro_status == "onhold":
                num_of_onnhold_pro = num_of_onnhold_pro + 1
            if pro_status == "completed":
                num_of_com_pro = num_of_com_pro + 1

            avl_workers = avl_workers - num_of_workers
            projects.append(project_details)
            codes_of_projects.append(pro_code)
            print(projects)
            print(codes_of_projects)
            print("The Project Was Saved.")
        else:
            print("Not Enough Workers. Project NOT Saved!")

    # check the project can accept or can not acceept

    # when the choice is 2

    elif your_choice == "2":
        print(
            """ 
                        XYZ Company
                Remove Completed Project
            """
        )
        pro_code = str(input("Enter The Project Code - "))
        remove = (
            str(input("Do You Want To Remove The Project(yes/no)?"))
            .lower()
            .replace(" ", "")
        )
        if (remove == "yes") and (pro_code in codes_of_projects):
            idx = codes_of_projects.index(pro_code)
            num_of_workers = projects[idx][4]
            pro_status = projects[idx][5]

            if pro_status == "ongoing":
                num_of_ongoing_pro = num_of_ongoing_pro - 1
                num_of_com_pro = num_of_com_pro + 1
            elif pro_status == "onhold":
                num_of_onnhold_pro = num_of_onnhold_pro - 1
                num_of_com_pro = num_of_com_pro + 1

            avl_workers = avl_workers + num_of_workers
            del projects[idx]
            del codes_of_projects[idx]
        else:
            print("Project Was NOT Removed")

    # when the choice is 3

    elif your_choice == "3":
        print(
            """
                        XYZ Company
                        Add New Workers """
        )

        add_workers = int(input("Enter number workers to add - "))
        add_workers_choice = (
            input("Do you want to add (yes/no)? ").lower().replace(" ", "")
        )
        if add_workers_choice == "yes":
            avl_workers = avl_workers + add_workers
            print("The New Workers Added.")
            print("Available Workers = ", avl_workers)
        else:
            print("The New Workers Are NOT Added")
            print(avl_workers)
            print("Available Workers = ", avl_workers)

    # When the choice is 4

    elif your_choice == "4":
        print(
            """
                            XYZ Company
                    Upadate Project Details
                    """
        )

        pro_code = str(input("Enter the  project code - "))
        cli_Name = str(input("Enter clients name - "))
        str_date = str(input("Enter start date - "))
        exp_end_date = str(input("Enter Expencted end Date - "))
        updated_num_of_workers = int(input("Enter the number of workers - "))
        updated_pro_status = (
            str(input("ongoing or on hold or completed? ")).lower().replace(" ", "")
        )
        update = (
            str(input("Do you  want to update the project details(yes/no)? "))
            .lower()
            .replace(" ", "")
        )
        idx = codes_of_projects.index(pro_code)

        projects[idx] = [
            pro_code,
            cli_Name,
            str_date,
            exp_end_date,
            num_of_workers,
            updated_pro_status,
        ]

        if pro_status == "ongoing" and updated_pro_status == "onhold":
            num_of_ongoing_pro = num_of_ongoing_pro - 1
            num_of_onnhold_pro = num_of_onnhold_pro + 1
            num_of_workers = num_of_workers + updated_num_of_workers

        elif pro_status == "ongoing" and updated_pro_status == "completed":
            num_of_ongoing_pro = num_of_ongoing_pro - 1
            num_of_com_pro = num_of_com_pro + 1
            num_of_workers = num_of_workers + updated_num_of_workers

        elif pro_status == "onhold" and updated_pro_status == "ongoing":
            num_of_ongoing_pro = num_of_ongoing_pro + 1
            num_of_onnhold_pro = num_of_onnhold_pro - 1

        elif pro_status == "onhold" and updated_pro_status == "completed":
            num_of_com_pro = num_of_com_pro + 1
            num_of_onnhold_pro = num_of_onnhold_pro - 1

        elif pro_status == "ongoing" and updated_pro_status == "ongoing":
            if num_of_workers > updated_num_of_workers:
                avl_workers = avl_workers - (num_of_workers - updated_num_of_workers)

            if num_of_workers < updated_num_of_workers:
                avl_workers = avl_workers + (updated_num_of_workers - num_of_workers)

        elif updated_pro_status == "completed":
            print("The project is already completed")

        print(projects)

    # When the choice is 5

    elif your_choice == "5":
        print(
            """
                        XYZ Company
                    Project Statistics """
        )
        print("\n")
        print("Ongoing projects - ", num_of_ongoing_pro)
        print("Completed projects - ", num_of_com_pro)
        print("Onhold projects - ", num_of_onnhold_pro)
        print("Number o available workers - ", avl_workers)

        # num_of_com_pro = int(input("Enter the number of completed projects - "))
        # num_of_onnhold_pro=int(input("Enter the number of on hold projects - "))
        # num_of_avl_workers_assign=int(input("Enter the number of available workers to assign - "))

    # When The Choice is 6

    elif your_choice == "6":
        print("Exiting")
        False
    else:
        print("Enter A Valid Choice")
