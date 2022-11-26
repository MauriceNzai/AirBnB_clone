AirBnB Clone - The Console

This is the first part of the larger AirBnB Clone project. It is the foundation
for the future aspects of the larger project including HTML/CSS templeting, database storage, API and front-end integration

Each task is linked and aimed towards achieving the following:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
create the first abstracted storage engine of the project:File storage.
create all unittests to validate all classes and storage engine

The console or comand interpreter creates the data model and allows create to, 
update, destroy, store an persist objects to a file.

It has the following specific objectivies:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object


The Overall objectives of this project are as listed below:

How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function


Requirements

The AirBnB Clone-The Console is built and tested in Ubuntu 20.04 LTS via Vagrant in VirtualBox. Programming language: python3


Installation and Execution

First clone the repository at
	git clone https://github.com/MauriceNzai/AirBnB_clone.git
Move into the repository directory
	cd AirBnB_clone
Execute the console program 
	/AirBnB_clone$ ./console.py

The Console Commands
The ommands available for this command interpreter as tabulated below:

Name		Description
create		Creates a new instance of the class passed by argument.
show		Prints the string representation of an instance.
destroy	Deletes an instance that was already created.
all		Prints string representation of all instances or\n
		of all instances of a specified class.
update		Updates an instance attribute if exists otherwise create it.
help		Show all commands or display information about a specific command.
quit		Exit the console.
EOF		Exit the console.


Commands Usage:

create

This command creates a new instance of the specified class. The new instance\n
of the specified class is saved to a JSON file and the id is\n
printed to the standard output.

If the class name is missing, the message
 '** class name missing **' will be printed.
If the class name does not exist, the message
 '** class doesn't exist **' will be printed.

show

Given the class name and id of an instance, this command will print the
string representation of the specified instance.
If the class name is missing, the message
'** class name missing **' will be printed.
If the class name does not exist, the message
'** class doesn't exist **' will be printed.
If the id is missing, the message
'** instance id missing **' will be printed.
If the instance of the class name does not exist for the given id, the message
 '** no instance found **' will be printed.

destroy

Given the class name and id of an instance,
this command will delete the specified instance.
If the class name is missing, the message
'** class name missing **' will be printed.
If the class name does not exist, the message
'** class doesn't exist **' will be printed.
If the id is missing, the message
'** instance id missing **' will be printed.
If the instance of the class name does not exist for the given id, the message
'** no instance found **' will be printed.

all

Given the class name, this command will print the string representation of all
instances under the specified class. If no class name is specified,
all existing objects will be printed.
The printed result will be in a list of strings.
If the class name does not exist, the message
'** class doesn't exist **' will be printed.

update

Given the class name, id, attribute name, and attribute value, this command
will update the attribute value of the specified instance.
If the class name is missing, the message
'** class name missing **' will be printed.
If the class name does not exist, the message
'** class doesn't exist **' will be printed.
If the id is missing, the message
'** instance id missing **' will be printed.
If the instance of the class name does not exist for the given id, the message
'** no instance found **' will be printed.
If the attribute name is missing, the message
'** attribute name missing **' will be printed.
If the value for the attribute is missing, the message
'** value missing **' will be printed.
All arguments after the attribute value will be ignored.
Only attributes with values of a string, integer, or float type can be updated.

count

Given the class name, this command will print out the number
of objects under the specified class.

These commands can be used in the following formarts:

create
create <class name>
show
show <class name> <id>
<class name>.show(<id>)
destroy
destroy <class name> <id>
<class name>.destroy(<id>)
all
all <class name>
<class name>.all()
update
update <class name> <id> <attribute name> <attribute value>
<class name>.update(<id>, <attribute name>, <attribute value>)
count
<class name>.count()


Examples

Once the command ./console.py has been typed into the terminal,
the user will be prompted with (hbnb). The user can proceed to enter the
commands as earlier illustrated. Below are some examples and their output:


Authors
Maurice Haro Software Engineering Student at ALX
Abraham Fatoki
