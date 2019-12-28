import os
import re

file_name = "reminders.txt"
prompt_message = "What can I do for you? create(c), delete(d), print(p), quit(q):\n"
quit_regex = re.compile("quit|q")
create_regex = re.compile("c.*|create.*")
print_regex = re.compile("print|p")
del_regex = re.compile("d.*|delete.*")

def create_reminder(reminder_file, user_input):
    split_input = user_input.split(" ")
    if len(split_input) > 1:
        reminder = " ".join(split_input[1:len(split_input)])
    else:
        reminder = raw_input("What's your reminder?\n")
    reminder_file.write(reminder + "\n")
    reminder_file.flush()

def invalid_index(idx, line_count):
    return (type(idx) != type(int()) or
            idx > line_count or
            idx < 1)

def delete_reminder(reminder_file, user_input):
    reminder_file.seek(0)
    lines = reminder_file.readlines()
    line_count = len(lines)
    if line_count == 0:
        print "There are no reminders to delete"
        return
    split_input = user_input.split(" ", 1)
    del_index = None
    if len(split_input) > 1:
        try:
            del_index = int(split_input[1])
        except ValueError:
            for i in range(0, line_count):
                if split_input[1] == lines[i].rstrip():
                    del_index = i + 1
            if not del_index:
                print("Couldn't find reminder '" + split_input[1] + "'")
    prompt = "What's index of the reminder you want to delete? ('c' to cancel)\n"
    if invalid_index(del_index, line_count):
        print_reminders(reminder_file)
        print
    while invalid_index(del_index, line_count):
        user_input = raw_input(prompt)
        if user_input == "c":
            return
        try:
            del_index = int(user_input)
            assert del_index <= line_count
            assert del_index > 0
        except ValueError:
            prompt = "Please enter a valid number ('c' to cancel)\n"
        except AssertionError:
            prompt = "Please enter an index between 1 and {} ('c' to cancel)\n".format(line_count)
    del_line = lines.pop(del_index - 1).rstrip()
    print "Deleting reminder '{}'".format(del_line)
    reminder_file.truncate(0)
    reminder_file.write("".join(lines))

def print_reminders(reminder_file):
    print
    reminder_file.seek(0)
    line_count = len(reminder_file.readlines())
    if line_count == 0:
        print "You have no reminders :)"
        return
    reminder_file.seek(0)
    print "========="
    print "REMINDERS"
    print "========="
    counter = 1
    for line in reminder_file:
        print ("(" + str(counter) + ") " + line.rstrip())
        counter += 1

def main():
    try:
        reminder_file = open(file_name, "a+")
        user_input = raw_input("Welcome to Reminders. " + prompt_message)
        while not(quit_regex.match(user_input) and quit_regex.match(user_input).group(0) == user_input):
            if create_regex.match(user_input):
                create_reminder(reminder_file, user_input)
            elif del_regex.match(user_input) and del_regex.match(user_input).group(0) == user_input:
                delete_reminder(reminder_file, user_input)
            elif print_regex.match(user_input) and print_regex.match(user_input).group(0) == user_input:
                print_reminders(reminder_file)
            print
            user_input = raw_input(prompt_message)
    except KeyboardInterrupt:
        print
    finally:
        print "Goodbye!"
        reminder_file.close()
        exit(0)

main()
