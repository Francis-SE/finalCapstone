"""
   This Task Management system designed to help users manage task
   efficiently. It allows users to register, add tasks, view tasks,
   generate reports and display statistics. 
   
   - Register new users
   - Add tasks
   - View tasks
   - Generate reports
   - Display statistics

   Upon running the program, users are prompted to log in. Then, user
   can select various option from the main menu to perform different 
   actions.
   """
# importing libraries
    
import os
from datetime import datetime, date

# Stores date format
DATETIME_STRING_FORMAT = "%Y-%m-%d" 

username_password = {}

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Reads in tasks.txts
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.readlines()
    task_data = [t for t in task_data if t != ""] 

# Iterates over a range of values based on the length of task_data per
# task which consists of 8 lines
task_list = []

for i in range(0, len(task_data), 8):  
    task_temp_data = {}
    curr_t = {}
    
    for j in range(i, i + 7):
        line = task_data[j]
        
        try:
            if j % 8 == 2:  # Merge index 2 and 3
                key = task_data[j].strip(":\n ")
                value = task_data[j+1].strip("\n  ")
                task_temp_data[key] = value
            else:
                key, value = line.strip("\n").split(': ')
                task_temp_data[key] = value
        except ValueError:
            pass  # Skip lines without a colon
    
# Converts to a list and assigns each element to corresponding keys
# in dictionary 'curr_t' and then adds to task_list. 
        
    clean_data = list(task_temp_data.values())
    print(clean_data)
    curr_t['username'] = clean_data[0]
    curr_t['title'] = clean_data[1]
    curr_t['description'] = clean_data[2]
    curr_t['due_date'] = datetime.strptime(
        clean_data[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        clean_data[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if clean_data[5] == "Yes" else False

    task_list.append(curr_t)


def clear_scr():
    """Clears the terminal screen."""


    os.system("cls||clear")


def get_input(prompt):
    """Prompts the user for input and ensures that the input is not
    empty before returning it.
    """ 


    while True:
        user_input = input(prompt)
        if user_input == '':
            print("You cannot add an empty task! Please enter again.")
        else:
            return user_input


def print_custom_title(title):
    """Generates a custom title with the current date and padding using
    equal signs.
    """


    formatted_date = date.today()
    title_with_date = f"{title} as of {formatted_date} "
    padding_length = max(0, 40 - len(title_with_date) // 2)
    line = "=" * padding_length + title_with_date + "=" * padding_length
    print(line)


def add_new_user():
    """Only admin user can add a new user to the user.txt file"""


    # Read existing usernames and passwords from the file
    with open("user.txt", "r") as in_file:
        for line in in_file:
            username, password = line.strip().split(";")
            username_password[username] = password

    # Request input of a new username
    new_username = input("New Username: ")
    while not new_username.isalnum():
        print("Invalid input! Please enter a username.")
        new_username = input("New Username: ")

    # Check if the new username already exists
    while new_username in username_password:
        print("Username already exists. Please choose a different one.")
        new_username = input("New Username: ")

    # Request input of a new password
    new_password = input("New Password: ")
    while not new_password.isalnum():
        print("Invalid input! Please enter a password.")
        new_password = input("New Password: ")

    # Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file,
        print("\nNew user added!")
        input("\nPress Enter to return to the main menu.")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    else:
        print("\nPasswords do not match")
        input("\nPress Enter to return to the main menu.")


def add_task():
    """Allow a user to add a new task to task.txt file
       Prompt a user for the following: 
       - A username of the person whom the task is assigned to,
       - A title of a task,
       - A description of the task and 
       - the due date of the task.
    """


    # Get the current date.
    curr_date = date.today()
        
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else: 
            break
            
    task_title = get_input("Title of Task: ")
    task_description = get_input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)

            if due_date_time.date() < curr_date:
                print("Due date can't be in the past")            
            else:                
                break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Add the data to the file task.txt and Include 'No' 
    # to indicate if the task is not yet complete.
    
    task_list.append(new_task)
    with open("tasks.txt", "a") as task_file:
        line = '-' * 80
        for task in task_list:
            task_list_to_write = (
                "Assigned to: {}\n".format(task['username'])
            )
            task_list_to_write += (
                "Task: {}\n".format(task['title'])
            )
            task_list_to_write += (
                "Task Description:\n {}\n".format(task['description'])
            )
            task_list_to_write += (
                "Due Date: {}\n".format(
                    task['due_date'].strftime(DATETIME_STRING_FORMAT))
            )
            task_list_to_write += (
                "Date Assigned: {}\n".format(
                    task['assigned_date'].strftime(DATETIME_STRING_FORMAT))
            )
            task_list_to_write += (
                "Task Complete: {}\n".format(
                    "Yes" if task['completed'] else "No")
            )
            task_list_to_write += ("{}\n".format(line))
    
        task_file.write(task_list_to_write)
    print("Task successfully added.")
    input("\nPress Enter to return to the main menu.")


def write_tasks_to_file():
    """Write the tasks to the tasks.txt file"""


    with open("tasks.txt", "w") as task_file:
        line = '-' * 80
        for task in task_list:
            task_file.write(
                "Assigned to: {}\n".format(task['username'])
            )
            task_file.write(
                "Task: {}\n".format(task['title'])
            )
            task_file.write(
                "Task Description:\n {}\n".format(task['description'])
            )
            task_file.write(
                "Due Date: {}\n".format(
                    task['due_date'].strftime(DATETIME_STRING_FORMAT))
            )
            task_file.write(
                "Date Assigned: {}\n".format(
                    task['assigned_date'].strftime(DATETIME_STRING_FORMAT))
            )
            task_file.write(
                "Task Complete: {}\n".format(
                    "Yes" if task['completed'] else "No")
            )
            task_file.write(
                "{}\n".format(line))


def view_all_task():
    """Reads the task from task.txt file and prints to the console in
    the readable format 
    """


    line2 = '-' * 80
    print_custom_title(" LIST OF ALL TASK ")
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
        disp_str += f"{line2}"
        print(disp_str)

    input("\nPress Enter to return to the main menu.")


def view_my_task():
    """Reads the task from the task.txt file and prints only the user's
    tasks who is currently logged in with the corresponding number.
    """


    curr_date = date.today()

    user_tasks = [t for t in task_list if t['username'] == curr_user]
    if not user_tasks:
        print("You don't have any tasks assigned.")
        input("\n\nPress Enter to return to the main menu.")
        return
    
    line2 = '-' * 80
    print_custom_title(" YOUR TASK ")
    task_numbers = []
    for i, t in enumerate(user_tasks, 1):
        disp_str = f"Task Number: {i}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
        disp_str += f"{line2}"
        print(disp_str)
        task_numbers.append(i)

    while True:
        task_choice = input(
            "Enter the number of the task you want to edit or mark as"
            " complete (-1 to return to the main menu): ")
        if task_choice == '-1':
            break
        elif not task_choice.isdigit() or int(task_choice) not in task_numbers:
            print("Invalid task number. Please enter a valid task number.")
            continue
        else:
            task_index = int(task_choice) - 1
            selected_task = user_tasks[task_index]
            if selected_task['completed']:
                print("This task is already completed. You can't edit it.")
            else:
                action = input(
                    "Do you want to mark this task as complete (enter 'c')"
                    " or edit this task (enter 'e')? ").lower()
                if action == 'c':
                    selected_task['completed'] = True
                    print("Task marked as complete.")
                    # Write the updated tasks to the file
                    write_tasks_to_file()
                elif action == 'e':
                    while True:
                        new_due_date = input(
                            "Enter new due date (YYYY-MM-DD format, leave"
                            " blank to keep the current one): ")
                        if new_due_date:
                            try:
                                due_date_time = datetime.strptime(
                                    new_due_date, DATETIME_STRING_FORMAT)
                                selected_task['due_date'] = due_date_time
                                
                                if due_date_time.date() < curr_date:
                                    print("Due date can't be in the past")            
                                else:                
                                    print("Task edited successfully.")
                                    break
                                
                                # Write the updated tasks to the file
                                write_tasks_to_file()
                            except ValueError:
                                print("Invalid datetime format."
                                      " Task due date remains unchanged.")
                else:
                    print("Invalid action. Please enter 'c' to"
                          " mark as complete or 'e' to edit.")


def generate_reports():
    '''If the user is an admin, they can generate reports like
    task_overview and user_overview in text file.
    '''


    # Convert date.today() to a datetime object
    today_datetime = datetime.combine(date.today(), datetime.min.time())

    # Generate task_overview.txt
    total_tasks = len(task_list)
    completed_tasks = sum(task['completed'] for task in task_list)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(
        1 for task in task_list 
        if not task['completed'] and task['due_date'] < today_datetime
    )
    incomplete_percentage = (
        (uncompleted_tasks / total_tasks) * 100 
    ) if total_tasks > 0 else 0
    overdue_percentage = (
        (overdue_tasks / total_tasks) * 100 
    ) if total_tasks > 0 else 0

    with open("task_overview.txt", "w") as task_overview_file:
        title = f" TASK OVERVIEW - PREPARED DATE: {date.today()} "
        padding_length = max(0, 40 - len(title) // 2)
        line = "=" * padding_length + title + "=" * padding_length
        task_overview_file.write(line)
        task_overview_file.write(f"\n\nTotal Tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed Tasks: {completed_tasks}\n")
        task_overview_file.write(f"Uncompleted Tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Overdue Tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of Incomplete Tasks:"
                                 f" {incomplete_percentage:.2f}%\n")
        task_overview_file.write(f"Percentage of Overdue Tasks:"
                                 f" {overdue_percentage:.2f}%\n\n")
        task_overview_file.write("=" * 80)

    # Generate user_overview.txt
    total_users = len(username_password)
    user_task_counts = {
        username: sum(1 for task in task_list if task['username'] == username) 
        for username in username_password.keys()
    }
    with open("user_overview.txt", "w") as user_overview_file:
        title = f" USER OVERVIEW - PREPARED DATE: {date.today()} "
        padding_length = max(0, 40 - len(title) // 2)
        line = "=" * padding_length + title + "=" * padding_length
        user_overview_file.write(line)
        user_overview_file.write(f"\n\nTotal Users: \t{total_users}\n")
        user_overview_file.write(f"Total Tasks: \t{total_tasks}\n\n")
        for username, task_count in user_task_counts.items():
            user_percentage = (
                (task_count / total_tasks) * 100 
            ) if total_tasks > 0 else 0
            completed_user_tasks = sum(
                1 for task in task_list 
                if task['username'] == username and task['completed']
            )
            incomplete_user_tasks = task_count - completed_user_tasks
            overdue_user_tasks = sum(
                1 for task in task_list 
                if task['username'] == username 
                and not task['completed'] 
                and task['due_date'] < today_datetime
            )
            user_completed_percentage = (
                (completed_user_tasks / task_count) * 100 
            ) if task_count > 0 else 0
            user_incomplete_percentage = (
                (incomplete_user_tasks / task_count) * 100 
            ) if task_count > 0 else 0
            
            try:
                user_overdue_tasks_percentage = (
                    (overdue_user_tasks / task_count) * 100)
            except ZeroDivisionError:
                pass
            
            if task_count == 0:
                title = f" Overview for user {username} "
                padding_length = max(0, 40 - len(title) // 2)
                line = "-" * padding_length + title + "-" * padding_length
                user_overview_file.write(line)
                user_overview_file.write(f"\n\nTotal Tasks Assigned:"
                                         f" {task_count}\n\n")
            else:
                title = f" Overview for user {username} "
                padding_length = max(0, 40 - len(title) // 2)
                line = "-" * padding_length + title + "-" * padding_length
                user_overview_file.write(line)
                user_overview_file.write(f"\n\nTotal Tasks Assigned:"
                                         f" {task_count}\n")
                user_overview_file.write(f"Percentage of Total Tasks:"
                                         f" {user_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of Completed Tasks:"
                                         f" {user_completed_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of Incomplete Tasks:"
                                         f" {user_incomplete_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of Overdue Tasks:"
                                         f" {user_overdue_tasks_percentage:.2f}%\n\n")
               
    
def display_stats():
    """
    If the user is an admin, the `display_stats` function calculates and displays 
    statistics about the number of users and tasks in the system, with the option 
    to add a new user and task if the corresponding files do not exist.
    """


    if not os.path.exists("user.txt") or not os.path.exists("tasks.txt"):
        print("There is no file found, Please create one first\n")
        
        # Generate the required files if they don't exist
        add_new_user()
        add_task()

    # Read data from user.txt
    with open("user.txt", "r") as user_file:
        user_data = user_file.readlines()

    num_users = len(user_data)

    # Read data from tasks.txt
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.readlines()

    num_tasks = len(task_data) // 8

    # Display statistics
    clear_scr()
    print_custom_title(" USERS AND TASKS STATISTICS ")
    print("\n------------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("------------------------------------")


def main():


    # Declares global variable for the use of other function.
    global curr_user  
   
    #Login Section
    '''
    This code reads usernames and password from the user.txt file to 
    allow a user to login.
    '''
    clear_scr()

    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    # Reads in user.txt
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    logged_in = False
    while not logged_in:

        clear_scr()
        title = " LOGIN "
        print("="*(15-(len(title)//2)), title, "="*(15-(len(title)//2)))
        curr_user = input("\nUsername: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            input("\nPress Enter to continue.")            
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            input("\nPress Enter to continue.")
            continue
        else:
            print("Login Successful!")
            logged_in = True

    
    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
       
        clear_scr()
        print()
        title = " TASK MANAGER "
        print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
        print("\n")
        menu = input('''Select one of the following Options below:
   
    r - \tRegistering a user
    a - \tAdding a task
    va - \tView all tasks
    vm - \tView my task
    gr - \tGenerate reports
    ds - \tDisplay statistics
    e - \tExit
                     
    Enter your choice: ''').lower()
        
        # It checks the value of the `menu` variable and executes different 
        # actions based on the input provided by the user. 

        if menu == 'r':
            if curr_user == 'admin':
                clear_scr()
                add_new_user()
            else:
                clear_scr()
                print("You don't have access to this page!")
                input("\nPress Enter to return to the main menu.")
                continue

        elif menu == 'a':
            clear_scr()
            add_task()

        elif menu == 'va':
            clear_scr()
            view_all_task()

        elif menu == 'vm':
            clear_scr()
            view_my_task()

        elif menu == 'gr':
            if curr_user == 'admin':
                clear_scr()
                print("\nYou have generated reports! Please refer to the"
                      " text file to view")
                input("\nPress Enter to return to the main menu.")
                generate_reports()
               
            else:
                clear_scr()
                print("You don't have access to this page!")
                input("\nPress Enter to return to the main menu.")
                
        elif menu == 'ds':
            if curr_user == 'admin':
                clear_scr()
                display_stats()
                input("\n\nPress Enter to return to the main menu.")
            else:
                clear_scr()
                print("You don't have access to this page!")
                input("\nPress Enter to return to the main menu.")
                
        elif menu == 'e':
            print("\nGoodbye!!!")
            exit()

        else:
            clear_scr()
            print("\nYou have made a wrong choice, Please Try again")
            input("\nPress Enter to return to the main menu.")

      
if __name__ == "__main__":
    main()