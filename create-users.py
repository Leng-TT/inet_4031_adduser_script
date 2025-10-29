#!/usr/bin/python3

# INET4031
# Leng Thao
# 10/29/2025
# 10/29/2025 End of Today

# os is used to run the shell commands (adduser, passwd, etc.) or in a way, allow python to execute the commands.
import os
# re is used to detect lines, in this case it's detecting "#" so we can skip them.
import re
# sys is used to read lines from standard input (the .input file via "<").
import sys

def main():
    for line in sys.stdin:

        # Checks if the line starts with "#".
        # Lines that start with '#' are comments (python) or in this case they're "skip this user" markers.
        # Detects this so we can ignore those lines.
        match = re.match("^#",line)
        
        # Removes trailing new lines and split the line into fields via colons.
        # Format Example - user:passwd:last:first:group
        fields = line.strip().split(':')
        
        # Skips lines that have "#" or do not have EXACTLY 5 fields. Prevents crashes/miss inputs from bad lines and ignores skipped lines. 
        if match or len(fields) != 5:
            continue

        # Aligins the data from fields to these variables. GECOS however matches the user info format in /etc/passwd.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Splits the groups list on commas in case there's more than one group for a user.
        groups = fields[4].split(',')

        # Shows/Prints what account is being created.
        print("==> Creating account for %s..." % (username))
        # Creates the user without an initial password, gecos sets the user info field (userame is the new account name).
        # Variable cmd will contain the shell command that the script will run to create a new Linux user account.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)


        # Commented means a dry run, a test run, it'll only print commands first.
        # Uncommented means os.system(cmd) will execute in REAL system command, meaning a user will be created and be on hold.
        #print cmd
        os.system(cmd)

        # Shows/Prints that it's setting a password for a user
        print("==> Setting the password for %s..." % (username))

        # Builds upon cmd and pipes the password twice into "passwd" via sudo.
        # Essentially it stimulates typing the password and confirmation that we would've done otherwise.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        # Again, commented means a dry run, a test run, it'll only print commands first.
        # Uncommented means it will execute in REAL system command, in this case a password would be created and store with the user.
        # Essentially, it creates an actual user
        #print cmd
        os.system(cmd)

        for group in groups:
            # Add the user to each listed group unless the marker is '-' (means no group).
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
