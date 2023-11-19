from Corporation import *


class Display:
    def __init__(self, company_name: str = "XYZ Company"):
        self.company_name = company_name
        self.menu = """
                     XYZ Company
                     Main Menu
                     1. Add a new project to existing projects.
                     2. Remove a completed project from existing projects.
                     3. Add new workers to available workers group.
                     4. Updates details on ongoing projects.
                     5. Project statics.
                     6. Exit
                    """

    def menu(self, choice_msg: str = "Enter your choice: "):
        print(self.menu)
        choice = str(input(choice_msg))
        return choice

    def add_new_project(self):
        print(
            """
            XYZ Company
            Add a new project
          """
        )

    def remove_completed_project(self):
        print(
            """
      XYZ Company
      Remove Completed Project
    """
        )

    def add_new_workers(self):
        print(
            """
      XYZ Company
      Add new Workers
    """
        )

    def update_project_details(self):
        print(
            """
      XYZ Company
      Update Project Details
    """
        )

    def project_statistics(self):
        print(
            """
      XYZ Company
      Project Statistics
    """
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
