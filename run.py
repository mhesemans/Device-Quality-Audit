import datetime  # imports datatime module to get current time


def gather_device_info():
    device_log = []  # list for device info

    auditor_name = get_valid_input(  # validates and stores input in variable
        # input for auditor name, validates if alphabetic
        "Enter auditor name (alphabetic only): ", str.isalpha
    )
    # stores current date and time in day/month/year + current time
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    part_no = get_valid_input(  # validates and stores input in variable
        # input for part number, validates if alphanumeric
        "Enter part number (alphanumeric): ", str.isalnum
    )
    so_no = get_valid_input(  # validates and stores input in variable
        # input for sales order number, validates if alphanumeric
        "Enter sales order number (alphanumeric): ", str.isalnum
    )
    device_model = get_valid_input(  # validates and stores input in variable
        # input for device model, validates if alphanumeric
        "Enter device model (alphanumeric): ", str.isalnum
    )
    serial_number = get_valid_input(  # validates and stores input in variable
        # input for serial number, validates if alphanumeric
        "Enter serial number (alphanumeric): ", str.isalnum
    )
    asset_tag = get_valid_input(  # validates and stores input in variable
        # input for asset tag, validates if alphanumeric
        "Enter asset tag (alphanumeric): ", str.isalnum
    )

    device_info = {
        "Auditor Name": auditor_name,
        "Audit Timestamp": timestamp,
        "Part No.": part_no,
        "SO No.": so_no,
        "Device Model": device_model,
        "Serial Number": serial_number,
        "Asset Tag": asset_tag
    }

    device_log.append(device_info)  # appends device_info to device_log
    # calls main_audit function and stores tuples in audit_log
    audit_log = main_audit()
    # appends audit_log to the device_log
    device_log.extend(audit_log)

    with open("audit_log.txt", "w") as f:  # opens audit_log.text in write
        # iterates over all entries in device_log
        for entry in device_log:
            # if the entry is a dictionary entry
            if isinstance(entry, dict):
                # write device information
                f.write("Device Information:\n")
                # writes key/values for each of them in the dictionary
                for key, value in entry.items():
                    f.write(f"{key}: {value}\n")
                    # blank line
                f.write("\n")
                # when the entry is not a dictionary
                # write the question and the answer
            else:
                f.write(f"{entry[0]}: {entry[1]}\n")
            f.write("\n")


def get_valid_input(prompt, validation_func):
    # loops until input is valid
    while True:
        # prompt user with input again
        user_input = input(prompt)
        # if input is valid
        if validation_func(user_input):
            return user_input  # return valid input
        else:
            # if input not valid, display error and prompt for info again
            print(f"Invalid input. Please enter a value that\
                   meets the criteria: {validation_func.__name__}")


def ask_question(question, options):  # prints question and gathers response
    while True:
        print(question)  # prints question
    # assigns numbers to options, starting with 1
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")  # prints options
        # shows option input field to user
        choice = input("Select an option: ")
        # checks if input is a digit and within options range
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            # returns the selected option as the matching integer
            return int(choice)
        else:
            # if validation fails, prints error
            print("Invalid input. Please enter the number for the options.")


def main_audit():
    log = []  # creates empty list to store responses to
    # questions and follow_up_questions

    device_info = gather_device_info()
    log.append(device_info)

    questions = [  # list of main questions
        ("Is the packaging of the laptops and desktops intact/undamaged?", [
         "Yes", "No"]),
        ("Is the device turning on and booting up without issues?", [
         "Yes", "No"]),
        ("Is the screen of the device free from dead pixels and cracks?", [
         "Yes", "No"]),
        ("Do all the ports (USB, HDMI, audio, etc.) function correctly?",
         ["Yes", "No"]),
        ("Are the keyboards and touchpads responsive and free from damage?",
         ["Yes", "No"]),
        ("Is the operating system installed and functioning without errors?",
         ["Yes", "No"]),
        ("Is the pre-installed software functioning correctly and up to date?",
         ["Yes", "No"]),
        ("Does the device meet the specified performance criteria?", [
         "Yes", "No"]),
        ("Are the devices free from overheating during operation?",
         ["Yes", "No"]),
        ("Does the device connect to Wi-Fi and Ethernet without issues?",
         ["Yes", "No"]),
        ("Is Bluetooth and other wireless connectivity options functional?", [
         "Yes", "No"]),
        ("Are all devices free from unauthorized modifications or tampering?",
         ["Yes", "No"])
    ]

    follow_up_questions = {  # dictionary of follow up questions based on main
        # audit responses
        1: [("Is there any visible damage to the devices themselves?",
            ["Yes", "No"]),
            ("Were the devices properly secured within the packaging?",
             ["Yes", "No"]),
            ("Are all the accessories present and undamaged?",
             ["Yes", "No"])],
        2: [("Is the power supply functioning correctly?", ["Yes", "No"]),
            ("Are there any error messages or beeps during the boot process?",
             ["Yes", "No"]),
            ("Is the battery (for laptops) holding a charge?", ["Yes", "No"])],
        3: [("How many dead pixels are there, are they clustered in one area?",
             ["Few", "Many", "Clustered"]),
            ("Is the screen damage affecting the usability of the device?",
             ["Yes", "No"]),
            ("Are there signs of previous repairs or screen replacements?",
             ["Yes", "No"])],
        4: [("Which specific ports are malfunctioning?",
             ["USB", "HDMI", "Audio", "Other"]),
            ("Are the ports physically damaged or loose?",
             ["Yes", "No"]),
            ("Have the drivers for these ports been installed correctly?",
             ["Yes", "No"])],
        5: [("Which keys or areas of the touchpad/mouse are unresponsive?",
             ["Specific keys", "Entire keyboard", "Touchpad", "Mouse"]),
            ("Is there physical damage or wear to the touchpad?",
             ["Yes", "No"]),
            ("Are the issues consistent across multiple devices or isolated?",
             ["Consistent", "Isolated"])],
        6: [("Are there any specific error messages displayed?",
             ["Yes", "No"]),
            ("Is the OS activation completed successfully?",
             ["Yes", "No"]),
            ("Are all necessary drivers and updates installed?",
             ["Yes", "No"])],
        7: [("Which software applications are malfunctioning?",
             ["Specific apps", "All apps"]),
            ("Are there any compatibility issues with the installed software?",
             ["Yes", "No"]),
            ("Are the software licenses valid and correctly assigned?",
             ["Yes", "No"])],
        8: [("Are the deviations from the specifications significant?",
             ["Yes", "No"]),
            ("Is the performance issue consistent across similar models?",
             ["Yes", "No"]),
            ("Are there any background processes impacting performance?",
             ["Yes", "No"])],
        9: [("Is the cooling system (fans, vents) functioning properly?",
             ["Yes", "No"]),
            ("Are there any signs of dust or blockages in the cooling system?",
             ["Yes", "No"]),
            ("Does the overheating occur under specific conditions?",
             ["Yes, on heavy load", "No, cause undetermined"])],
        10: [("Are the network drivers installed and up to date?",
              ["Yes", "No"]),
             ("Is the issue present on all devices or specific ones?",
              ["All devices", "Specific devices"]),
             ("Are there any interference or signal strength issues?",
              ["Yes", "No"])],
        11: [("Which specific wireless features are malfunctioning?",
              ["Bluetooth", "Wi-Fi", "Other"]),
             ("Are the wireless adapters installed/recognized by the system?",
              ["Yes", "No"]),
             ("Are there firmware updates available for the wireless adapter?",
              ["Yes", "No"])],
        12: [("What modifications or tampering have been detected?",
              ["Software", "Hardware"]),
             ("Are there any security risks with these modifications?",
              ["Yes", "No"]),
             ("Can the modifications be traced back to the manufacturer?",
              ["Yes", "No"])]
    }
    # loops through questions
    for idx, (question, options) in enumerate(questions, 1):
        answer = ask_question(question, options)   # ask main question
        log.append((question, options[answer-1]))  # log question and answer
        if answer == 2:  # If answer is no, ask follow up question
            # loops through follow_up_questions
            for sub_question, sub_options in follow_up_questions[idx]:
                # Asks follow-up question
                sub_answer = ask_question(sub_question, sub_options)
                # logs follow-up question and answer
                log.append((sub_question, sub_options[sub_answer-1]))

    return log  # returns log of all questions, follow-up question and answers


if __name__ == "__main__":
    gather_device_info()
