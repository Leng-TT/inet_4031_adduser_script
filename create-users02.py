#!/usr/bin/python3

# INET4031
# Leng Thao
# 10/29/2025
# By The End of Today

import os
import re
import sys

def main():

# I useed /dev/tty so the script reads Y/N directly from the keyboard
# Because stdin is redirected from the input file (< create-users.input) it means when I tried to do: answer = input("Run in Dry-run mode? Y/N:)
# It wouldn't allow me to type in Y or N but rather just goes for whatever is being read.

    sys.stdout.write("Run in Dry-run mode? Y/N: ")
    sys.stdout.flush()
    with open("/dev/tty") as tty:
        answer = tty.readline().strip().upper()
    # Keeps answer from being case sensitive

    dry_run = (answer == "Y")
    # Makes the answer True or False

    for line in sys.stdin:
        # Skip commented lines that start with '#'
        match = re.match("^#", line)

        # Split fields on colons
        fields = line.strip().split(':')

        # Skip bad or commented lines
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(">> SKIP: Commented line was skipped.")
                else:
                    print(">> ERROR: Line skipped due to missing fields ->", line.strip())
            continue

        # Assign field variables
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups in case there’s more than one group for a user
        groups = fields[4].split(',')

        # Create user account
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        if dry_run:
            print("[DRY-RUN] Would run:", cmd)
        else:
            os.system(cmd)

        # Set password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        if dry_run:
            print("[DRY-RUN] Would run:", cmd)
        else:
            os.system(cmd)

        # Add groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run:
                    print("[DRY-RUN] Would run:", cmd)
                else:
                    os.system(cmd)
            else:
                if dry_run:
                    print(">> SKIP: '-' marker means no group added.")

if __name__ == '__main__':
    main()
