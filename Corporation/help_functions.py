from Corporation import *


def menu(
    redirect: bool = False,
    to: int = None,
    company_name: str = company_name,
    msg: str = "Enter your choice: ",
) -> str:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    main_menu = f"""
     {company_name}
     Main Menu
     1. Add a new project to existing projects.
     2. Remove a completed project from existing projects.
     3. Add new workers to available workers group.
     4. Updates details on ongoing projects.
     5. Project statics.
     6. Exit
    """
    print("Redirecting..." if redirect else main_menu)
    return to if redirect else str(input(msg))
