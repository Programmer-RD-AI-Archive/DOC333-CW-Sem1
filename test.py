# Intialize the variables
avl_workers = 0
your_choice = 0
Pro_Code = 0
Cli_Name = 0
Str_Date = 0
EX_end_Date = 0
Num_of_workers = 0
Pro_Status = 0
Save = 0
yes = 0
no = 0
Remove = 0
Num_of_workers_add = 0
Add = 0
Update = 0
num_of_onhold_pro = 0
Num_of_completed_pro = 0
num_of_ongoing_pro = 0
Num_of_avl_workers_assign = 0
projects = []
codes_of_pro = []
running = True
while running:
    print(
        """              
               XYZ Company
               Main  Menu
     1. Add a  new  project to existing projects.
     2. Remove a  completed project from existing projects.
     3. Add new workers to available workers group.
     4. Update details on ongoing projects.
     5. Project Statistics
     6. Exit
      """
    )

    # Get the choice
    your_choice = int(input("Enter your choice-"))

    # When the choice is 1
    if your_choice == 1:
        print(
            """                   XYZ Company
                       Add a new project      """
        )
        Pro_Code = str(input("Enter the project code -"))
        Cli_Name = str(input("Enter clients name -"))
        Str_Date = str(input("Enter start date -"))
        EX_end_Date = str(input("Enter Expected end Date -"))
        Num_of_workers = int(input("Enter the number of workers -"))
        Pro_Status = str(input("ongoing or on hold or completed?"))
        Save = (
            input("Do you want to save the project(yes/no)?").lower().replace(" ", "")
        )

        # when the user input 'yes'
        if (
            (Save == "yes")
            and (avl_workers >= Num_of_workers)
            and (Pro_Status in ["ongoing", "completed", "onhold"])
        ):
            project_details = {
                "Project Code": Pro_Code,
                "Client Name": Cli_Name,
                "Start Date": Str_Date,
                "Expected End Date": EX_end_Date,
                "Number of Workers": Num_of_workers,
                "Project Status": Pro_Status,
            }
            if Pro_Status == "ongoing":
                num_of_ongoing_pro = num_of_ongoing_pro + 1
            elif Pro_Status == "completed":
                Num_of_completed_pro = Num_of_completed_pro + 1
                avl_workers = avl_workers - Num_of_workers
            else:
                num_of_onhold_pro = num_of_onhold_pro + 1
            projects.append(project_details)
            codes_of_pro.append(Pro_Code)
            print(projects)
            print(codes_of_pro)
            print("The project was saved.")
        else:
            print(
                "We can not accept your project due to the lack  of available workers..Project was not saved."
            )

    # When the choice is 2
    elif your_choice == 2:
        print(
            """
                         XYZ Company
                   Remove Completed Project
                """
        )
        Pro_Code = str(input("Enter the project code -"))
        Remove = (
            str(input("Do you  want to remove the project(yes/no)?"))
            .lower()
            .replace(" ", "")
        )
        if (Remove == "yes") and (Pro_Code in codes_of_pro):
            idx = codes_of_pro.index(Pro_Code)
            Num_of_workers = projects[idx][4]
            Pro_Status = projects[idx][5]

            if Pro_Status == "ongoing":
                num_of_ongoing_pro = num_of_ongoing_pro - 1
                Num_of_completed_pro = Num_of_completed_pro + 1
                del projects[idx]
                del codes_of_pro[idx]
            elif Pro_Status == "onhold":  # TODO
                num_of_onhold_pro = num_of_onhold_pro - 1
                Num_of_completed_pro = Num_of_completed_pro + 1
                avl_workers = avl_workers + Num_of_workers
                del projects[idx]
                del codes_of_pro[idx]
            else:
                print("Project was not  removed.")

    # When the choice is 3
    elif your_choice == 3:
        print(
            """
                        XYZ Company
                     Add new workers"""
        )
        Num_of_workers_add = int(input("Enter Number of workers to add -"))
        Add = str(input("Do you want to add(yes/no)?")).lower().replace(" ", "")
        if Add == "yes":
            avl_workers = avl_workers + Num_of_workers_add
            print("The new workers was added.")
            print("available workers=", avl_workers)
        else:
            print("The new workers was not added.")
            print(avl_worker)
            print("Available workers=", avl_workers)

    # When the choice is 4
    elif your_choice == 4:
        print(
            """
                            XYZ Company
                      Update Project Details
                      """
        )
        Pro_Code = str(input("Enter the  project code -"))
        Cli_Name = str(input("Enter clients name -"))
        Str_Date = str(input("Enter start date -"))
        EX_end_Date = str(input("Enter Expected end Date -"))
        updated_num_of_workers = int(input("Enter the number of workers -"))
        Updated_Pro_Sts = (
            str(input("ongoing or on hold or completed?")).lower().replace(" ", "")
        )
        Update = (
            str(input("Do you  want to update the project details(yes/no)?"))
            .lower()
            .replace(" ", "")
        )
        idx = codes_of_pro.index(Pro_Code)
        previous_workers = projects[idx]["Number of Workers"]
        previous_status = projects[idx]["Status"]
        projects[idx] = {
            "Project Code": Pro_Code,
            "Client Name": Cli_Name,
            "Start Date": Str_Date,
            "Expected End Date": EX_end_Date,
            "Number of Workers": updated_num_of_workers,
            "Project Status": Pro_Status,
        }
        if previous_workers > updated_num_of_workers:
            avl_workers += previous_workers - updated_num_of_workers

        elif previous_workers < updated_num_of_workers:
            avl_workers -= updated_num_of_workers - Num_of_workers

        if Pro_Status == "ongoing" and Updated_Pro_Sts == "onhold":
            num_of_ongoing_pro = num_of_ongoing_pro - 1
            num_of_onhold_pro = num_of_onhold_pro + 1
            avl_workers += updated_num_of_workers

        elif Pro_Status == "ongoing" and Updated_Pro_Sts == "completed":
            num_of_ongoing_pro -= 1
            num_of_onhold_pro += 1
            avl_workers += updated_num_of_workers

        elif Pro_Status == "onhold" and Updated_Pro_Sts == "ongoing":
            num_of_ongoing_pro += 1
            num_of_onhold_pro -= 1

        elif Pro_Status == "onhold" and Updated_Pro_Sts == "completed":
            Num_of_completed_pro += 1
            num_of_onhold_pro -= 1

        elif Updated_Pro_Sts == previous_status:
            print(f"The project is already {previous_status}")
            print(projects)

    # When the choice is 5
    elif your_choice == 5:
        print(
            """
                           XYZ Company
                      Project Statistics """
        )
        print("\n")
        print("Ongoing projects -", num_of_ongoing_pro)
        print("Completed projects -", Num_of_completed_pro)
        print("Onhold projects -", num_of_onhold_pro)
        print("Number Of Available Workers-", avl_workers)

        # Num_of_completed_pro = int(input("Please enter number of completed projects -"))
        # num_of_onhold_pro = int(input("Please enter the number of  onhold projects -"))
        # num_of_avl_workers_assign = int(
        #     input("Please enter the number of available workers to assign -")
        # )

    # When  the choice is 6
    elif your_choice == 6:
        print("exit")
        running = False
    else:
        print("Please input a valid Choice!")
