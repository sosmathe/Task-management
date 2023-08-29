# capstone_project_III
# sibabalwe_mathe

from datetime import datetime
import os.path

def reg_user():
    # checking if the user is an admin
    if username_input == "admin":
        new_username = input("Please enter the new username: \n")
        # checking if the new username already exists in the user.txt file
        existing_usernames = []
        try:
            with open('user.txt', 'r') as f:
                for line in f:
                    existing_usernames.append(line.split(", ")[0].rstrip())
        except FileNotFoundError:
            print("textfile user.txt not found. Please make sure the textfile exists.")
            return

        # if the new username does not exist, ask the user to confirm the password.
        while new_username in existing_usernames:
            print("Username already exists. Please choose a different username.")
            new_username = input("Please enter the new username: \n")

        new_password = input("Please enter your new password: \n")
        confirm_password = input("Please enter the password again: \n")

        while new_password != confirm_password:
            print("Your passwords do not match. Please re-enter your password.")
            new_password = input("Please enter your new password: \n")
            confirm_password = input("Please re-enter the password again: \n")

        # adding to the textfile
        try:
            with open('user.txt', 'a') as f:
                f.write("\n" + new_username + ", " + new_password)
        except FileNotFoundError:
            print("textfile user.txt not found. Please make sure the textfile exists.")
            return

        print("You have successfully registered a new user :)")
    else:
        print("Only the admin can register new users")

def add_task():
     # getting user-input
    username = input("Please enter the username of the person assigned to the task:\n")

    # check if the assigned user is registered
    registered_users = []
    try:
        with open('user.txt', 'r') as f:
            for line in f:
                registered_users.append(line.split(", ")[0].strip())
    except FileNotFoundError:
        print("User file not found. Please make sure the file exists.")
        return

    if username not in registered_users:
        print("The assigned user is not registered. Please assign the task to a registered user.")
        return
    
    title_task = input("Please enter the title of the task:\n")
    task_description = input("Please enter the task description:\n")
    due_date = input("Please enter the due date (dd MMM yyyy, e.g., 20 Jul 2023):\n")
    # validate the  due date format
    if not validate_date(due_date):
        print("Invalid date format. Please enter the date in the format: dd MMM yyyy (e.g., 20 Jul 2023)")
        return
    
    date_time = datetime.now()
    current_date = date_time.strftime("%d %b, %Y")
    task_complete = "No"

    # adding the task to the tasks.txt textfile.
    try:
        with open('tasks.txt', 'a') as f:
            f.write(
                "\n" + username + ", " + title_task + ", " + task_description + ", " + current_date.replace(', ',
                                                                                                              " ") +
                ", " + due_date + ", " + task_complete)

    except FileNotFoundError:
        print("Textfile tasks.txt not found. Please make sure the file exists.")
        return

    print("New task has been successfully loaded into the system")

def view_all():
    # create lists
    task_list = []
    assigned_to_list = []
    date_assigned_list = []
    due_date_list = []
    task_complete_list = []
    task_description_list = []

    # opening the textfile
    try:
        with open('tasks.txt', 'r') as f:
            icount = 0
            for line in f:
                # getting data from the lines and storing them in the declared lists
                i = line.rstrip().split(", ")
                task_list.append(i[1])
                assigned_to_list.append(i[0])
                date_assigned_list.append(i[3])
                due_date_list.append(i[4])
                task_complete_list.append(i[5])
                task_description_list.append(i[2])
                icount = icount + 1
    except FileNotFoundError:
        print("textfile tasks.txt not found. Please make sure the textfile exists.")
        return

    # printing the data in the specified format
    for x in range(icount):
        print("Task:\t\t\t" + task_list[x])
        print("assigned to:\t\t" + assigned_to_list[x])
        print("Date Assigned:\t\t" + date_assigned_list[x])
        print("Due date:\t\t" + due_date_list[x])
        print("Task Complete?\t\t" + task_complete_list[x])
        print("Task description:\n" + " " + task_description_list[x])
        print("")
        
def view_mine():
    # create lists
    task_list = []
    assigned_to_list = []
    date_assigned_list = []
    due_date_list = []
    task_complete_list = []
    task_description_list = []
    icount = 0

    # opening the "tasks.txt" textfile and reading the task information into the created lists
    try:
        with open('tasks.txt', 'r') as f:
            for line in f:
                i = line.rstrip().split(", ")

                if len(i) >= 6:
                    task_list.append(i[1])
                    assigned_to_list.append(i[0])
                    date_assigned_list.append(i[3])
                    due_date_list.append(i[4])
                    task_complete_list.append(i[5])
                    task_description_list.append(i[2])
                    icount += 1
    except FileNotFoundError:
        print("textfile tasks.txt not found. Please make sure the textfile exists.")
        return

    # looping through the tasks and print the task details for the tasks assigned to the current user
    for x in range(icount):

        if username_input == assigned_to_list[x]:
            print("Task " + str(x + 1) + ":")
            print("Task:\t\t\t" + task_list[x])
            print("assigned to:\t\t" + assigned_to_list[x])
            print("Date Assigned:\t\t" + date_assigned_list[x])
            print("Due date:\t\t" + due_date_list[x])
            print("Task Complete?\t\t" + task_complete_list[x])
            print("Task description:\n" + " " + task_description_list[x])
            print("")

    # getting the task number from the user and adjust for 0-based indexing
    try:
        task_choice = int(input("Enter the number of the task you want to modify or enter -1 to return to the main menu: "))

        if task_choice == -1:
            return

        # adjusting for 0-based indexing
        task_index = task_choice - 1

        # checking if the task number is valid
        if task_index < 0 or task_index >= icount:
            print("Invalid task number.")
            return

        # checking if the task is already complete and can't be edited
        if task_complete_list[task_index].strip().lower() == "yes":
            print("This task has already been completed and cannot be edited.")
            return

        # getting the modify choice from the user
        modify_choice = input("Choose an option:\n1. Mark task as complete\n2. Edit task\nEnter your choice: ")

        # mark the task as complete if the user chooses option 1
        if modify_choice == "1":
            task_complete_list[task_index] = "Yes"
            print("Task marked as complete.")

        # modify the task details if the user chooses option 2
        elif modify_choice == "2":
            new_username = input("Enter the new username for the task: ")
            new_due_date = input("Enter the new due date for the task (dd:first three letters of the month:yyyy): ")

            # update the fields if the input is not empty
            if new_username.strip():
                assigned_to_list[task_index] = new_username

            if new_due_date.strip():
                # validate the new due date format
                if not validate_date(new_due_date):
                    print("Invalid date format. Please enter the date in the format: dd MMM yyyy (e.g., 20 Jul 2023)")
                    return
                due_date_list[task_index] = new_due_date

        # save the modified task list back to the file
        try:
            with open('tasks.txt', 'w') as f:
                for x in range(icount):
                    f.write(assigned_to_list[x] + ", " + task_list[x] + ", " + task_description_list[x] + ", " +
                            date_assigned_list[x] + ", " + due_date_list[x] + ", " + task_complete_list[x] + "\n")
        except FileNotFoundError:
            print("textfile tasks.txt not found. Please make sure the textfile exists.")

        print("Task modification completed.")

    except ValueError:
        print("Invalid input. Task number must be a numeric value.")
        return

# function to generate the task overview report
def generate_task_overview():
    # creating and initializing variables
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    # count the total number of tasks and categorize them
    try:
        with open('tasks.txt', 'r') as f:
            lines = f.read().splitlines()
            current_line = ""
            for line in lines:
                current_line += line

                # the task description in the textfile can be long enough to make each assigned task to a user
                # take up to two lines
                # to separate each task, we know that each assignment ends with a yes or no in the textfile
                # here we checking if the line ends with a "Yes" or "No" indicator
                if line.strip().lower().endswith("yes") or line.strip().lower().endswith("no"):
                    total_tasks += 1
                    task_info = current_line.split(", ")

                    # checking if the task has all the required fields
                    if len(task_info) < 6:
                        print("Incomplete task information: {}".format(current_line))
                        current_line = ""
                        continue

                    
                    # checking if the task is completed or not
                    if task_info[-1].strip().lower() == 'yes':
                        completed_tasks += 1
                    else:
                        uncompleted_tasks += 1
                        due_date = datetime.strptime(task_info[4], "%d %b %Y")

                        # check if the task is overdue
                        if due_date < datetime.now():
                            overdue_tasks += 1

                    current_line = ""

    except FileNotFoundError:
        print("textfile tasks.txt not found. Please make sure the textfile exists.")
        return

    # calculate percentages based on the total number of tasks
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    # write the task overview report to a file
    try:
        with open('task_overview.txt', 'w') as f:
            f.write("Task Overview\n")
            f.write("Total tasks: {}\n".format(total_tasks))
            f.write("Completed tasks: {}\n".format(completed_tasks))
            f.write("Uncompleted tasks: {}\n".format(uncompleted_tasks))
            f.write("Overdue tasks: {}\n".format(overdue_tasks))
            f.write("Percentage of incomplete tasks: {:.2f}%\n".format(incomplete_percentage))
            f.write("Percentage of overdue tasks: {:.2f}%\n".format(overdue_percentage))
    except FileNotFoundError:
        print("textfile task_overview.txt not found. Please make sure the textfile exists.")

    print("Task overview report generated.")

# function to generate the user overview report
def generate_user_overview():
    # creating and initializing variables
    total_users = 0
    total_tasks = 0
    user_tasks = {}

    # counting the total number of users
    try:
        with open('user.txt', 'r') as f:
            for line in f:
                total_users += 1
    except FileNotFoundError:
        print("textfile user.txt not found. Please make sure the textfile exists.")
        return

    # counting the total number of tasks assigned to each user
    try:
        with open('tasks.txt', 'r') as f:
            current_line = ""
            for line in f:
                current_line += line

                # checking if the line ends with a "Yes" or "No" indicator
                if line.strip().lower().endswith("yes") or line.strip().lower().endswith("no"):
                    total_tasks += 1
                    task_info = current_line.split(", ")
                    assigned_user = task_info[0]

                    # updating the task count for each user
                    if assigned_user not in user_tasks:
                        user_tasks[assigned_user] = 1
                    else:
                        user_tasks[assigned_user] += 1

                    current_line = ""

    except FileNotFoundError:
        print("textfile tasks.txt not found. Please make sure the textfile exists.")
        return

    # write the user overview report to the textfile
    try:
        with open('user_overview.txt', 'w') as f:
            f.write("User Overview\n")
            f.write("Total users: {}\n".format(total_users))
            f.write("Total tasks: {}\n".format(total_tasks))

            for user, tasks in user_tasks.items():
                tasks_percentage = (tasks / total_tasks) * 100
                completed_tasks_percentage = 0
                uncompleted_tasks_percentage = 0
                overdue_tasks_percentage = 0

                # calculating percentages for completed, uncompleted, and overdue tasks for each user
                try:
                    with open('tasks.txt', 'r') as x:
                        user_completed_tasks = 0
                        user_uncompleted_tasks = 0
                        user_overdue_tasks = 0

                        for line in x:
                            task_info = line.rstrip().split(", ")

                            # checking if the task is assigned to the current user
                            if task_info[0] == user:
                                if len(task_info) >= 5 and task_info[5].strip().lower() == 'yes':
                                    user_completed_tasks += 1

                                elif len(task_info) >= 4:
                                    user_uncompleted_tasks += 1
                                    due_date = datetime.strptime(task_info[3], "%d %b %Y")

                                    # checking if the task is overdue
                                    if due_date < datetime.now():
                                        user_overdue_tasks += 1

                        completed_tasks_percentage = (user_completed_tasks / tasks) * 100
                        uncompleted_tasks_percentage = (user_uncompleted_tasks / tasks) * 100
                        overdue_tasks_percentage = (user_overdue_tasks / tasks) * 100

                except FileNotFoundError:
                    print("textfile task.txt not found. Please make sure the textfile exists.")
                    return

                # write the user-specific information to the report
                f.write("\nUser: {}\n".format(user))
                f.write("Total tasks assigned: {}\n".format(tasks))
                f.write("Percentage of tasks assigned: {:.2f}%\n".format(tasks_percentage))
                f.write("Percentage of completed tasks: {:.2f}%\n".format(completed_tasks_percentage))
                f.write("Percentage of tasks to be completed: {:.2f}%\n".format(uncompleted_tasks_percentage))
                f.write("Percentage of overdue tasks: {:.2f}%\n".format(overdue_tasks_percentage))

    except FileNotFoundError:
        print("textfile user_overview.txt not found. Please make sure the textfile exists.")

    print("User overview report generated.")
    
# function to validate date input
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d %b %Y")
        return True
    except ValueError:
        return False

# function to validate user-input
def validate(username, password):
    # create lists
    username_list = []
    password_list = []

    # opening user.txt textfile and reading the username and password into the created list
    try:
        with open('user.txt', 'r') as f:
            for line in f:
                i = line.rstrip().split(", ")
                username_list.append(i[0])
                password_list.append(i[1])
    except FileNotFoundError:
        print("textfile not found. Please make sure the textfile exists.")
        return False

    # if the username and password exist then the user will be able to log in
    if username in username_list and password in password_list:
        # get the index of the username and validate the password
        index = username_list.index(username)
        if password_list[index] == password:
            return True
    print("Your credentials are invalid")
    return False


# getting user input
username_input = input("Please enter your username: \n")
password_input = input("Please enter your password: \n")

# calling the validate function to validate the user input
while not validate(username_input, password_input):
    print("Please try again")
    username_input = input("Please enter your username: \n")
    password_input = input("Please enter your password: \n")

print("Welcome " + username_input)
menu = ""
while menu != 'e':

    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    # the menu for the admin differs from that of any other user
    # the admin has more options to the menu. It can request stats from
    # the data we are working with, such as the total number of users and the total numbers of tasks
    if username_input == "admin":
        menu = input('''Select one of the following options below:
            r - Register a user
            a - Add a task
            va - View all tasks
            vm - View my tasks
            gr - Generate reports
            ds - Display statistics
            tt - Total number of tasks
            tu - Total number of users
            e - Exit
            : ''').lower()
    else:
        menu = input('''Select one of the following options below:
            a - Add a task
            va - View all tasks
            vm - View my tasks
            e - Exit
            : ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_task_overview()
        generate_user_overview()

    elif menu == 'ds':
        if not os.path.exists('task_overview.txt') or not os.path.exists('user_overview.txt'):
            generate_task_overview()
            generate_user_overview()

        try:
            with open('task_overview.txt', 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("Task overview report has not been generated.")

        try:
            with open('user_overview.txt', 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("User overview report has not been generated.")

    elif menu == 'tt':
        # counting the total number of tasks in the textfile task.txt
        try:
            with open('tasks.txt', 'r') as f:
                total_tasks = 0
                for line in f:

                    # checking if the line ends with a "Yes" or "No" indicator
                    if line.strip().lower().endswith("yes") or line.strip().lower().endswith("no"):
                        total_tasks += 1

                print("The total number of tasks: " + str(total_tasks))
        except FileNotFoundError:
            print("Tasks file not found. Please make sure the file exists.")

    elif menu == 'tu':
        # counting the total number of user in the textfile user.txt
        try:
            count_users = 0
            with open('user.txt', 'r') as f:
                for line in f:
                    count_users += 1
            print("The total number of users: " + str(count_users))
        except FileNotFoundError:
            print("User file not found. Please make sure the file exists.")

    elif menu == 'e':
        print('Goodbye!!!')

    else:
        print("You have made a wrong choice. Please try again")

'''
links I used to complete this task

https://www.tutorialsteacher.com/python/string-endswith
https://railsware.com/blog/indexing-and-slicing-for-lists-tuples-strings-sequential-types/#:~:text=Python%20uses%20zero%2Dbased%20indexing,index%201%2C%20and%20so%20on.
https://www.w3schools.com/python/python_dictionaries.asp
https://www.geeksforgeeks.org/python-string-rstrip/
https://www.geeksforgeeks.org/python-os-path-exists-method/

'''
