import datetime  # imports datetime module to get current time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('device_quality_audit')

audit = SHEET.worksheet('audit')

data = audit.get_all_values()

"""
Function collects device info, auditor name, time stamp (automatic, not user
input), Part number, Sales Order number, Device model, serial number and asset
tag and stores these variables in the device_info dictionary.
Function then calls main_audit and stores output in audit_log, appends
audit_log to the device_info and appends it as a row to the spreadsheet
"""


def gather_device_info():
    # loop to allow multiple audits to be completed
    while True:
        # validates and stores input in variable
        auditor_name = get_valid_input(
            # input for auditor name, validates if alphabetic
            "Enter auditor name (alphabetic only):\n", str.isalpha
        )
        # stores current date and time in day/month/year + current time
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        part_no = get_valid_input(  # validates and stores input in variable
            # input for part number, validates if alphanumeric
            "Enter part number (alphanumeric):\n", str.isalnum
        )
        # input for sales order number, validates if alphanumeric
        so_no = get_valid_input(  # validates and stores input in variable
            "Enter sales order number (alphanumeric):\n", str.isalnum
        )
        # input for device model, validates if alphanumeric
        # validates and stores input in variable
        device_model = get_valid_input(
            "Enter device model (alphanumeric):\n", str.isalnum
        )
        # input for serial number, validates if alphanumeric
        # validates and stores input in variable
        serial_number = get_valid_input(
            "Enter serial number (alphanumeric):\n", str.isalnum
        )
        # input for asset tag, validates if alphanumeric
        # validates and stores input in variable
        asset_tag = get_valid_input(
            "Enter asset tag (alphanumeric):\n", str.isalnum
        )

        audit_log = main_audit()  # stores main_audit output as audit_log
        # stores device_info inputs in list
        device_info = [auditor_name, timestamp, part_no,
                       so_no, device_model, serial_number, asset_tag]

        # adds audit_log list to device_info list
        row = device_info + audit_log
        # appends row data to the spreadsheet
        audit.append_row(row)

        # Prompt the user to see if they want to complete another audit
        another_audit = ask_question(
            "Do you want to complete another audit?\n",
            ["Yes", "No"]
        )
        if another_audit != 1:
            print("Audit process completed.\n")
            break  # Exit the while loop and end the function


"""
get_valid_input function will validate the input for the device info
the prompt parameter is the input with the validation_func parameter the
validation that applies to the input e.g. str.isalnum, str.isalpha. If
validation fails, a reason will be printed for the user.
"""


def get_valid_input(prompt, validation_func):
    # if validation is true then prompt input will be passed through to the \
    # user_input variable
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        # if false, invalid input message is printed
        else:
            print(
                f"Invalid input. Please enter a value \
that meets the criteria: {validation_func.__name__}\n")


"""
ask_question function will loop through the questions list when a valid
answer is passed through. The options are assigned a number and the input
is checked to make sure the number entered by the user is a digit and in range
"""


def ask_question(question, options):
    while True:
        print(question)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}\n")
        choice = input("Select an option:\n")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid input. Please enter the number for the options.\n")


"""
main_audit function stores the inputs to the questions and follow-up questions
to the log variable as a list. It will loop through the questions list if "yes"
(1) is provided as an input. It will loop through the follow-up questions if
"No" (2) is provided as an input. All answers are stored as a list.
"""


def main_audit():
    # Placeholder list with 48 empty strings for the 48 question columns
    log = [''] * 48

    # list of all questions with answers, stored as question and options tuples
    questions = [
        ("Is the packaging of the laptops and desktops \
intact/undamaged?\n",
         ["Yes", "No"]),
        ("Is the device turning on and booting up without issues?\n",
         ["Yes", "No"]),
        ("Is the screen of the device free from dead pixels and cracks?\n",
         ["Yes", "No"]),
        ("Do all the ports (USB, HDMI, audio, etc.) function correctly?\n",
         ["Yes", "No"]),
        ("Are the keyboards and touchpads responsive and free from damage?\n",
         ["Yes", "No"]),
        ("Is the operating system installed and functioning without errors?\n",
         ["Yes", "No"]),
        ("Is the pre-installed software functioning correctly \
and up to date?\n",
         ["Yes", "No"]),
        ("Does the device meet the specified performance criteria?\n",
         ["Yes", "No"]),
        ("Are the devices free from overheating during operation?\n",
         ["Yes", "No"]),
        ("Does the device connect to Wi-Fi and Ethernet without issues?\n",
         ["Yes", "No"]),
        ("Is Bluetooth and other wireless connectivity options functional?\n",
         ["Yes", "No"]),
        ("Are all devices free from unauthorized modifications \
or tampering?\n",
         ["Yes", "No"])
    ]

    # dictionary of follow-up questions, with lists of questions and options
    # stored as tuples
    follow_up_questions = {
        1: [("Is there any visible damage to the devices themselves?\n",
             ["Yes", "No"]),
            ("Were the devices properly secured within the packaging?\n",
             ["Yes", "No"]),
            ("Are all the accessories present and undamaged?\n",
             ["Yes", "No"])],
        2: [("Is the power supply functioning correctly?\n",
             ["Yes", "No"]),
            ("Are there any error messages or beeps \
during the boot process?\n",
             ["Yes", "No"]),
            ("Is the battery (for laptops) holding a charge?\n",
            ["Yes", "No"])],
        3: [("How many dead pixels are there, \
are they clustered in one area?\n",
             ["Few", "Many", "Clustered"]),
            ("Is the screen damage affecting the usability of the device?\n",
             ["Yes", "No"]),
            ("Are there signs of previous repairs or screen replacements?\n",
            ["Yes", "No"])],
        4: [("Which specific ports are malfunctioning?\n",
             ["USB", "HDMI", "Audio", "Other"]),
            ("Are the ports physically damaged or loose?\n",
             ["Yes", "No"]),
            ("Have the drivers for these ports been installed correctly?\n",
             ["Yes", "No"])],
        5: [("Which keys or areas of the touchpad/mouse are unresponsive?\n",
             ["Specific keys", "Entire keyboard", "Touchpad", "Mouse"]),
            ("Is there physical damage or wear to the touchpad?\n",
             ["Yes", "No"]),
            ("Are the issues consistent across \
multiple devices or isolated?\n",
            ["Consistent", "Isolated"])],
        6: [("Are there any specific error messages displayed?\n",
             ["Yes", "No"]),
            ("Is the OS activation completed successfully?\n",
             ["Yes", "No"]),
            ("Are all necessary drivers and updates installed?\n",
             ["Yes", "No"])],
        7: [("Which software applications are malfunctioning?\n",
             ["Specific apps", "All apps"]),
            ("Are there any compatibility issues\
with the installed software?\n",
             ["Yes", "No"]),
            ("Are the software licenses valid and correctly assigned?\n",
            ["Yes", "No"])],
        8: [("Are the deviations from the specifications significant?\n",
             ["Yes", "No"]),
            ("Is the performance issue consistent across similar models?\n",
             ["Yes", "No"]),
            ("Are there any background processes impacting performance?\n",
             ["Yes", "No"])],
        9: [("Is the cooling system (fans, vents) functioning properly?\n",
             ["Yes", "No"]),
            ("Are there any signs of dust or \
blockages in the cooling system?\n",
             ["Yes", "No"]),
            ("Does the overheating occur under specific conditions?\n",
            ["Yes", "No"])],
        10: [("Are the network drivers installed and up to date?\n",
              ["Yes", "No"]),
             ("Is the issue present on all devices or specific ones?\n",
             ["All devices", "Specific devices"]),
             ("Are there any interference or signal strength issues?\n",
             ["Yes", "No"])],
        11: [("Which specific wireless features are malfunctioning?\n",
              ["Bluetooth", "Wi-Fi", "Other"]),
             ("Are the wireless adapters installed/recognized \
by the system?\n",
             ["Yes", "No"]),
             ("Are there firmware updates available \
for the wireless adapter?\n",
             ["Yes", "No"])],
        12: [("What modifications or tampering have been detected?\n",
              ["Software", "Hardware"]),
             ("Are there any security risks with these modifications?\n",
             ["Yes", "No"]),
             ("Can the modifications be traced back to the manufacturer?\n",
             ["Yes", "No"])]
    }
    # loops through list
    for idx, (question, options) in enumerate(questions, 1):
        # prints question and collects input
        answer = ask_question(question, options)
        # stores the input to log if answer is yes (1)
        log[(idx - 1) * 4] = options[answer - 1]
        # If the answer to the main question is "No"
        if answer == 2:
            # loop through the follow-up questions associated to main question
            for sub_idx, (sub_q, sub_o) in\
                    enumerate(follow_up_questions[idx], 1):
                # Ask the follow-up question and collect input
                sub_answer = ask_question(sub_q, sub_o)
                # Store the input for the follow-up question in the log
                log[(idx - 1) * 4 + sub_idx] = sub_o[sub_answer - 1]

    return log  # Return the log of all questions and answers


if __name__ == "__main__":
    print("Welcome to the Device Quality Audit tool.\n")
    print("Please provide the audit details, after which \
you will be presented with a set of questions to determine \
if the device meets the quality requirements.\n")
    gather_device_info()
