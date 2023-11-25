from Corporation import *


class Projects:
    @staticmethod
    def remove_completed_projects(code_of_project: str) -> Tuple[bool, str]:
        """Remove completed projects

        Keyword arguments:
        code_of_project -- description
        Return: Tuple[A boolean which states whether or not the operation was succesful, A string which has an output msg regarding the operation if it was successful or not...]
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
                project_status,
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
            return (True, "Successfully removed completed projects...")
        except Exception as e:
            return (False, e)

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
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
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
            return (True, "Successfully created a new project...", workers)
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
    ) -> Tuple[bool, str]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
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
            return (True, "Project details updated successfully...")
        except Exception as e:
            return (False, e)
