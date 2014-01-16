from sys import argv
import datetime
# from os.path import exists

script, filename = argv

mylist = [] 
today = str(datetime.date.today())
mylist.append(today) 

print "======================================================="
print "* Welcome to the Command Line To-Do List Vault (beta) *"
print "======================================================="
print "The vault is: %s (where the to-do's you type in will be stored) " % filename
print "Today is %s" % mylist
print "=========================================================================="

# print "Does the idea database file exists? " % exists(filename)

target = open(filename, 'a')

to_do = raw_input("Write your to-do task: ")

print "Hit ENTER to save the idea, or CTRL + C to cancel."
raw_input('> ')

target.write('\n')
target.write("===================================================")
target.write('\n')
target.write(to_do)
target.write('\n')
target.write("===================================================")
target.write('\n')

print "Done! it's saved."
print "The actual file %s is %d bytes long." % (filename, len(filename))

read_list = raw_input("Do you want to read your to-do list? (yes/no) ")
if read_list == "yes":
	target.close()
	open_doc = open(filename, 'r')
	read_doc = open_doc.read()
	print read_doc
	erase_to_do = raw_input("Do you want to erase a to-do? (yes/no) ")
	if erase_to_do == "yes":
		# do something
		# google 'how to erase something of a file' (need to store the to-do's in variables that automatically sum + 1 number with a for statement in order to create dynamically automated different name variables)
		print "do something"
		# open_doc.close() ???
	else:
		print "Ok! see you later!"

	open_doc.close()
else:
	print "Ok! see you later!"
	target.close()
	open_doc.close()



# despues agregar date and time (datetime())
