from Corporation import *


class Project_Management:
    def __init__(
        self,
        all_projects: list = [],
        completed_projects: list = [],
        project_names: list = [],
        possible_inputs: list = ["ongoing", "completed", "onhold"],
    ):
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
        raise NotImplementedError()

    def remove_completed_projects(self, project_code):
        raise NotImplementedError()

    def update_projects(
        self,
        project_code,
        clients_name,
        start_date,
        expected_end_date,
        no_of_workers,
        project_status,
    ):
        raise NotImplementedError()

    def project_existention(self, project_code):
        raise NotImplementedError()
