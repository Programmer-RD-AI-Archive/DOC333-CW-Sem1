from Corporation import *


class Projects:
    @staticmethod
    def remove_completed_projects(
        code_of_project: str,
        all_projects: list,
        workers: int,
        statistics_list: list,
        completed_projects: list,
    ) -> Tuple[bool, str]:
        """Remove completed projects

        Keyword arguments:
        code_of_project (str) -- The code of the project that will be removed
        all_projects (list) -- A list which contains all the projects which haven't been removed
        workers (int) -- The number of workers
        statistics_list (list) -- The list that tracks the statistics for choice (5)
        completed_projects (list) -- The list which contains all removed completed projects

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
            return (True, "Successfully removed completed projects.", workers)
        except Exception as e:
            return (False, e, workers)

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
        workers: int,
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
        workers (int) -- total number of workers in the organization

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
            workers -= number_of_workers
            return (True, "Successfully created a new project", workers)
        except Exception as e:
            return (False, e, workers)

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
        workers: int,
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

        Return: Tuple[
            A boolean which shows if the function successfully executed or not,
            The message which will be displayed to the user
        ]
        """
        try:
            workers += current_workers
            workers -= number_of_workers
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
            return (True, "Project details updated successfully", workers)
        except Exception as e:
            return (False, e, workers)
