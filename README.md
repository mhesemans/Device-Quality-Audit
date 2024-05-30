# **Device Quality Audit Tool**

![Heroku deployed app](documentation/readme/heroku_deployed.png) 

# Overview
The Device Quality Audit Tool is designed for production quality supervisors and their teams at IT equipment resellers. This tool collects device quality audit reports for laptops and desktops undergoing configuration, modification, and installation processes. The collected data is validated and stored in a Google spreadsheet, ensuring data integrity and facilitating report generation by management. Additionally, the tool allows users to check the quality outcome of previously submitted audit reports based on the serial number of the device.

You can access the tool through the following link: <a href="https://device-quality-audit-3500f8503e72.herokuapp.com/" target="_blank"> Device Quality Audit </a>

The spreadsheet where the data is written into can be access through <a href="https://docs.google.com/spreadsheets/d/142YUxspbdLPVlbAbR9dHFEMEsQg8Ie459hkIRFsqVL8/edit?usp=drive_link" target="_blank"> This google drive link </a>

# Table of Contents


# Objective

This project is intended to replace the current production practise of submitting quality audit data in an unorganized manner where data is directly entered into a spreadsheet without uniform formatting or data validation. It offers the quality team a structured way to provided clear answers through targetted questioning of the device's quality and compliance parameters. This in turn provides a clean and organized data output which can be used for analysis and reporting.

[Back to top](<#contents>)

# Target Audience

The Device Quality Audit Tool is specifically designed for:

- **Production Quality Supervisors:** Overseers of the quality control process who require a reliable method to document and review device audits systematically.
- **Quality Assurance Teams:** Team members responsible for ensuring that laptops and desktops meet the required quality standards before they are distributed.
- **IT Equipment Resellers:** Businesses that modify, configure, and install IT equipment, needing an efficient way to manage and validate audit data.
- **Management:** Decision-makers who utilize audit reports generated from the collected data to assess and improve quality control processes.

[Back to top](<#contents>)

# User Stories
- As a Production Quality Supervisor:

    I want to ensure that all device quality audits are completed accurately and efficiently.
    So that I can maintain high standards and consistency in our quality control processes.

- As a Quality Assurance Team Member:

    I want a user-friendly tool to input audit data with validation checks.
    So that I can reduce the likelihood of errors and streamline the audit process.

- As an IT Equipment Reseller:

    I want a centralized system to store and manage all audit data.
    So that I can easily access and review audit outcomes to ensure compliance with quality standards.

- As a Manager:

    I want to generate comprehensive reports based on the collected audit data.
    So that I can analyze performance and identify areas for improvement.

- As a Staff Member:

    I want to quickly check the quality outcome of a specific device by entering its serial number.
    So that I can provide accurate information to stakeholders and customers promptly.

[Back to top](<#contents>)

# Features

- **Device Quality Audit:** Collects detailed audit information, validates inputs, and stores data in a Google spreadsheet.
- **Quality Outcome Retrieval:** Allows users to check the audit result (passed/failed) for a specific device using its serial number.
- **User-Friendly Interface:** Guides users through the audit process and provides clear feedback on data entry.

# Future features

- **Duplicate Serial Numbers:** Check the spreadsheet to see if an audit was previously submitted for the same serial number, overwrite the previous serial number with the new audit data.
- **Asset Tag for Outcome Retrieval:** Check quality outcome by searching datasheet for asset tag inputs.