import os
import re

file_name = "reminders.txt"
prompt_message = "What can I do for you? create(c), print(p), quit(q):\n"
quit_regex = re.compile("quit|q")
create_regex = re.compile("c.*|create.*")
print_regex = re.compile("print|p")

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
    try:
        reminder_file = open(file_name, "a+")
        user_input = raw_input("Welcome to Reminders. " + prompt_message)
        while not(quit_regex.match(user_input) and quit_regex.match(user_input).group(0) == user_input):
            if create_regex.match(user_input):
                create_reminder(reminder_file, user_input)
            elif print_regex.match(user_input) and print_regex.match(user_input).group(0) == user_input:
                print_reminders(reminder_file)
            user_input = raw_input(prompt_message)
    except KeyboardInterrupt:
        print ""
    finally:
        print "Goodbye!"
        reminder_file.close()
        exit(0)

main()
