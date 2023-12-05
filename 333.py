ongoing_projects = {}
onhold_projects = {}
completed_projects = {}

available_workers = []

def print_menu():
    print()
    print("               XYZ Company")
    print("                Main Menu\n")
    print("1. Add a new project to existing projects")
    print("2. Remove a completed project from existing projects")
    print("3. Add new workers to available workers group")
    print("4. Update details on ongoing projects")
    print("5. Project Statistics")
    print("6. Exit")

def add_new_project():
    print("               XYZ Company")
    print("             Add New Project\n")
    project_code = input("Enter project code (0 to exit): ")

    if project_code == "0":
        return

    name = input("Enter client's name: ")
    start_date = input("Enter start date (DD/MM/YYYY): ")
    end_date = input("Enter expected end date (DD/MM/YYYY): ")
    num_workers = int(input("Enter number of workers: "))
    status = ""
    while status not in ["ongoing", "on hold", "completed"]:
        status = input("Enter project status (ongoing/on hold/completed): ")
    preference = input("Do you want to save the project (Yes/No)? ")

    if preference == "Yes":
        new_project = {
            "project_code": project_code,
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "num_workers": num_workers,
            "status": status
        }

        if status == "ongoing":
            ongoing_projects[project_code] = new_project
        elif status == "on hold":
            onhold_projects[project_code] = new_project
        elif status == "completed":
            completed_projects[project_code] = new_project
        print("Project saved successfully!")

    elif preference == "No":
        print("\nProject not saved.")
        return

    else:
        print("\nInvalid choice !!!")
        return

def remove_completed_project():
    print("               XYZ Company")
    print("             Remove Completed Project\n")
    project_code = input("Enter completed project code (0 to exit): ")

    if project_code in ongoing_projects:
        moved_project = ongoing_projects.pop(project_code)
        completed_projects[project_code] = moved_project
        print("\nProject moved to completed successfully!")

    else:
        print("\nInvalid project code")


def add_workers():
    num_workers = int(input("Enter number of workers to add: "))
    available_workers.extend([0] * num_workers)

    print(f"{num_workers} workers added successfully!")

def update_project():
    print("               XYZ Company")
    print("             Update Project Details\n")
    project_code = input("Enter project code to update (0 to exit): ")

    if project_code in ongoing_projects:
        print("Updating: ", ongoing_projects[project_code]["name"])
        name = input("Enter new client name or leave blank: ")
        start_date = input("Enter new start date or leave blank: ")

        if name != "":
            ongoing_projects[project_code]["name"] = name

        if start_date != "":
            ongoing_projects[project_code]["start_date"] = start_date

        print("\nProject updated successfully!")

    else:
        print("\nInvalid project project_code")

def view_statistics():
    print("               XYZ Company")
    print("             Project Statistics\n")
    print("Ongoing Projects:", len(ongoing_projects))
    print("On Hold Projects:", len(onhold_projects))
    print("Completed Projects:", len(completed_projects))
    print("Available Workers:", len(available_workers))

while True:
    print_menu()
    choice = input("\nEnter your choice: ")
    print("")

    if choice == "1":
        add_new_project()

    elif choice == "2":
        remove_completed_project()

    elif choice == "3":
        add_workers()

    elif choice == "4":
        update_project()

    elif choice == "5":
        view_statistics()

    elif choice == "6":
        break

    else:
        print("Invalid Input !!!")