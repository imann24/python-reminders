import os
import subprocess
import re

file_name = "reminders.txt"
prompt_message = "What can I do for you? create(c), print(p), quit(q):\n"
create_reminder_regex = re.compile("c.*|create.*")

def get_file(file_name):
    file_path = os.getcwd() + "/" + file_name
    if not os.path.isfile(file_path):
        subprocess.call(["touch", file_path])
    return open(file_path, "a+")

def create_reminder(reminder_file, user_input):
    split_input = user_input.split(" ")
    if len(split_input) > 1:
        reminder = " ".join(split_input[1:len(split_input)])
    else:
        reminder = raw_input("What's your reminder?\n")
    reminder_file.write(reminder + "\n")
    reminder_file.flush()

def print_reminders(reminder_file):
    reminder_file.seek(0)
    print ""
    print "========="
    print "REMINDERS"
    print "========="
    counter = 1
    for line in reminder_file:
        print ("(" + str(counter) + ") " + line.rstrip())
        counter += 1
    print ""

def main():
    reminder_file = get_file(file_name)
    user_input = raw_input("Welcome to Reminders. " + prompt_message)
    while user_input != "quit" and user_input != "q":
        if create_reminder_regex.match(user_input):
            create_reminder(reminder_file, user_input)
        elif user_input == "print" or user_input == "p":
            print_reminders(reminder_file)
        user_input = raw_input(prompt_message)
    reminder_file.close()
    exit(0)

main()
