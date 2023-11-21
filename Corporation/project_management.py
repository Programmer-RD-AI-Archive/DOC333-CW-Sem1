from Corporation import *


class Project_Management:
    def __init__(
        self,
        all_projects: list = None,
        completed_projects: list = None,
        project_names: list = None,
        possible_inputs: list = None,
    ):
        if all_projects is None:
            all_projects = []
        if completed_projects is None:
            completed_projects = []
        if project_names is None:
            project_names = []
        if possible_inputs is None:
            possible_inputs = ["ongoing", "completed", "onhold"]
        self.worker = Worker_Management()
        self.all_projects = all_projects
        self.completed_projects = completed_projects
        self.project_names = project_names
        self.possible_inputs = possible_inputs
        self.variable_of_possible_inputs = [0] * len(possible_inputs)

    def add_project(
        self,
        project_code,
        clients_name,
        start_date,
        expected_end_date,
        no_of_workers,
        project_status,
    ):
        pass

    def remove_completed_projects(self, project_code):
        pass

    def update_projects(
        self,
        project_code,
        clients_name,
        start_date,
        expected_end_date,
        no_of_workers,
        project_status,
    ):
        pass

    def project_existention(self, project_code):
        pass
