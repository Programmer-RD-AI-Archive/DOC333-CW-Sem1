#initialize the variable
workers = 0
your_choice = 0
all_projects = []
completed_projects = []
execute = True
on_hold_projects = 0
ongoing_projects = 0
completed_projects = 0
project_names = []
menu = """
 XYZ Company
 Main Menu
 1. Add a new project to existing  projects.
 2. Remove a completed project from existing projects.
 3. Add new workers to available workers group.
 4. Updates details on ongoing projects.
 5. Project statics.
 6. Exit
"""


def project_status(project_status, previous_status, project_code):
  pass


while execute:

  print(menu)
  #Check the user choice
  your_choice = int(input("Enter your choice"))

  #When user choice is 1
  if (your_choice == 1):
    print("""
      XYZ Company
      Add a new project
    """)
    project_code = str(input("Project Code - "))
    if project_code == "0":
      continue
    clients_name = str(input("Clients Name - "))
    start_date = str(input("Start Date - "))
    expected_end_date = str(input("Expected end date - "))
    number_of_workers = int(input('Numbers of Workers - '))
    project_status = str(
        input("Project Status (ongoing/completed/on hold) - "))
    save = str(input("Do you want to save the project(Yes/No)? "))
    if (save.lower() == "yes") and (number_of_workers <= workers):
      project_data = [
          project_code, clients_name, start_date, expected_end_date,
          number_of_workers, project_status
      ]
      project_names.append(project_code)
      all_projects.append(project_data)
    else:
      print('The project was *not* saved')

  #When user choice is 2
  elif (your_choice == 2):
    print("""
      XYZ Company
      Remove Completed Project
    """)
    project_code = str(input("Project Code - "))
    save = str(input("Do you want to save the project (Yes/ No)? "))
    if (save.lower() == "yes") and (project_code in index_dictionary.keys()):
      index_of_project = project_names.index(project_code)
      del all_projects[index_of_project]
      del project_names[index_of_project]
    else:
      print("The project was not removed...")

  #When user choice is 3
  elif (your_choice == 3):
    print("""
      XYZ Company
      Add new Workers
    """)
    new_no_of_workers = int(input("Number Workers to Add - "))
    save = str(input("Do you want to add ? (Yes / No) "))
    if save.lower() == 'yes':
      workers += new_no_of_workers
  #When user choise is 4
  elif (your_choice == 4):
    print("""
      XYZ Company
      Update Project Details
    """)
    project_code = str(input("Project Code - "))
    if project_code == "0":
      continue
    clients_name = str(input("Clients Name - "))
    start_date = str(input("Start Date - "))
    expected_end_date = str(input("Expected end date - "))
    number_of_workers = int(input('Numbers of Workers - '))
    project_status = str(
        input("Project Status (ongoing/completed/on hold) - "))
    save = str(input("Do you want  too  update the project details(Yes/No)?"))
    previous_project_status = all_projects[project_names.index(project_code)][5]
    
  #When user choice is 5
  elif (your_choice == 5):
    print("""
      XYZ Company
      Project Statistics
    """)
    print(f"Number of ongoing projects - {ongoing_projects}")
    print(f"Number of completed projects - {completed_projects}")
    print(f"Number of On Hold Projects -  {on_hold_projects}")
    print(f"Number of avilable workers - {workers}")
    add_project = str(input("Do you want to add the project (Yes/No)?"))  #TODO

#When  user choice is 6
  elif (your_choice == 6):
    execute = False

  else:
    print("Please enter a valid choice...")
