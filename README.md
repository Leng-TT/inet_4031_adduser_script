# INET4031 Add Users Script and User List
## Program Description

This program automates the process of adding multiple user accounts to a Linux system. Instead of manually typing commands for each user, the script reads a list of users from an input file and performs the same system commands automatically. Normally, a system administrator would have to manually create each user by typing commands such as “sudo adduser username,” “sudo passwd username,” and “sudo adduser username groupname.” Essentially, this script uses those same Linux commands through Python’s os.system() function. It handles account creation, password setup, and group membership in bulk, saving time and reducing the risk of human error. The program (create-users02.py) also includes a dry run mode, which safely shows what commands would run without actually making system changes.

## Program User Operation 

The program reads a colon-delimited input file containing the list of users to add. When the script starts, it prompts the user to choose whether to run in Dry-run mode (Y) or Normal mode (N). In Dry-run mode, the script shows the commands that would run and prints messages about skipped or invalid lines. In Normal mode, it executes the actual system commands to create and configure users.

### Input File Format

Each line in the input file must contain five fields separated by colons. The format is:
username:password:last:first:group1,group2

The fields represent the following:

**Username:** The account name to create

**Password:** The password to assign

**Last:** The user’s last name (used in the GECOS field)

**First:** The user’s first name (used in the GECOS field)

**Groups:** A comma separated list of groups to assign. However, use “-” you don't want a user in a group

To skip a line, start it with a “#”. Any line that begins with “#” is ignored by the script.

### Command Execution

Before running the script, make sure it is executable by using the command “chmod +x create-users02.py.” Then run it with “./create-users02.py < create-users.input”. The input redirection symbol (<) tells the script to read user information from the input file instead of waiting for typed input. When the program starts, it will ask “Run in Dry-run mode? Y/N:”. Type Y to preview what will happen, or N to run the commands for real.

### "Dry Run"

If the user selects "Dry Run" mode by typing Y, the script will print each command that would have been executed and display messages for lines that were skipped or formatted incorrectly. No **ACTUAL** system changes are made during a dry run. This mode allows the user to confirm the script’s behavior safely before running it for real.
