# 0x15. API

## Resources

#### Read or watch:

* [Friends don't let friends program in shell script](https://intranet.alxswe.com/rltoken/KMFzqRAqedMf7AHHBD_43g)
* [What is an API](https://intranet.alxswe.com/rltoken/zeBO6_RNTlwaotyRRNAzoQ)
* [What is an API? In English, please](https://intranet.alxswe.com/rltoken/bf09Qp6QY44CANLzxxRbPA)
* [What is a REST API](https://intranet.alxswe.com/rltoken/fA164QWEnZxaSngBD3EPRQ)
* [What are microservices](https://intranet.alxswe.com/rltoken/n4h77IbBuDxTE3bhes_AyQ)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.alxswe.com/rltoken/b7V1ROY6kSRxDDKnsJoqxg)

## Learning Objectives

### General

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

## Tasks

## 0. Gather data from an API

- Write a Python script that, using this REST API, for a given employee ID,
	returns information about his/her TODO list progress.

### Requirements:

You must use <code>urllib</code> or <code>requests</code> module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress
in this exact format:

First line: Employee EMPLOYEE_NAME is done with tasks(
NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and
non-completed tasks

Second and N next lines display the title of completed tasks: TASK_TITLE (with 1
tabulation and 1 space before the TASK_TITLE)

First line: Employee EMPLOYEE_NAME is done with tasks(
NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and
non-completed tasks

<code>EMPLOYEE_NAME</code>: name of the employee
<code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks
<code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of
completed and non-completed tasks
Second and N next lines display the title of completed tasks: <code>
TASK_TITLE</code> (with 1 tabulation and 1 space before the <code>
TASK_TITLE</code>)

Mode: mandatory

File/s: [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)
<hr>

## 1. Export to CSV

- Using what you did in the task #0, extend your Python script to export data in
	the CSV format.

### Requirements:

Records all tasks that are owned by this employee
Format must be: <code>"USER_ID","USERNAME","TASK_COMPLETED_STATUS","
TASK_TITLE"</code>
File name must be: <code>USER_ID.csv</code>

Mode: mandatory

File/s: [1-export_to_CSV.py](./1-export_to_CSV.py)
<hr>

## 2. Export to JSON

- Using what you did in the task #0, extend your Python script to export data in
	the JSON format.

### Requirements:

Records all tasks that are owned by this employee
Format must be: <code>{ "
USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}</code>
File name must be: <code>USER_ID.json</code>

Mode: mandatory

File/s: [2-export_to_JSON.py](./2-export_to_JSON.py)
<hr>

## 3. Dictionary of list of dictionaries

- Using what you did in the task #0, extend your Python script to export data in
	the JSON format.

### Requirements:

Records all tasks from all employees
Format must be: <code>{ "
USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "
USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}</code>
File name must be: <code>todo_all_employees.json</code>

Mode: mandatory

File/s: [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py)
<hr>
