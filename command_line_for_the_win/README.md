Command line for the win
Bash
Scripting
 By: Sylvain Kalache, co-founder at Holberton School
 Weight: 1
 Project will start Jul 10, 2023 4:00 AM, must end by Jul 24, 2023 4:00 AM
 Manual QA review must be done (request it when you are done with the project)

Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
This project will be manually reviewed.
As each task is completed, the name of that task will turn green
Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

Specific
In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

--------------------------------------------

for satisfying the "sprecific" requirements here the steps i followed to use the SFTP command-line tool:

in the local terminal:

sftp username@hostname  """here username, hostname and then enter the password of the sandbox"""

put PATH/TO/THE/SCREENSHOTS.jpeg /root/alx-system_engineering-devops/command_line_for_the_win

Then exit to quit the SFTP command-line tool
