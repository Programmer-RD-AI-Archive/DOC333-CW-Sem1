from Corporation import *


class Verification:
    @staticmethod
    def date_verification(msg: str) -> str:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        date = input(msg)
        splitted_date = date.split(date[2] if len(date) > 3 else " ")
        if len(splitted_date) != 3:
            print("Enter a valid format of the date..!")
            return date_verification(msg)
        month, date, yr = splitted_date[0], splitted_date[1], splitted_date[2]
        if int(month) > 12:
            print("Enter a valid month..!")
            return date_verification(msg)
        if int(date) > 31:
            print("Enter a valid date..!")
            return date_verification(msg)
        return date

    @staticmethod
    def enter_project_status(
        msg: str = "Project Status (ongoing/completed/on hold) : ",
        update_status: bool = False,
    ) -> Tuple[str, list, int]:
        """An function that uses recursion to make sure that an input is enter as required

        Keyword arguments:
        msg -- The message that should be displayed to the user to get the project status input
        update_status -- Whether to update the status count

        Return: Tuple[The state enter by the user,
                        the statistic list used to track the project status count,
                        the index of the enter state
                    ]
        """
        project_state = str(input(msg)).replace(" ", "").lower()
        if project_state not in possible_inputs:
            print("The entered project status is incorrect...")
            return enter_project_status()
        if update_status:
            statistics_list[possible_inputs.index(project_state)] += 1
        return (
            project_state,
            statistics_list,
            possible_inputs.index(project_state),
        )

    def project_code_verification(self, msg: str, project_codes: list) -> str:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        project_code = str(input(msg))
        if project_code in project_codes:
            print("Project Code already exists..!")
            return self.project_code_verification(msg, project_codes)
        return project_code
