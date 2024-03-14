# 0x0F. Python - Object-relational mapping

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Tasks :

## 0. Get all states
a script that lists all states from the database hbtn_0e_0_usa

## 1. Filter states
a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

## 2. Filter states by user input
a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument


## 3. SQL Injection...
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

## 4. Cities by states
a script that lists all cities from the database hbtn_0e_4_usa

## 5. All cities by state
a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

## 6. First state model
a python file that contains the class definition of a State and an instance Base = declarative_base()

## 7. All states via SQLAlchemy
a script that lists all State objects from the database hbtn_0e_6_usa

## 8. First state
a script that prints the first State object from the database hbtn_0e_6_usa

## 9. Contains `a`
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

## 10. Get a state
a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

## 11. Add a new state
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

## 12. Update a state
a script that changes the name of a State object from the database hbtn_0e_6_usa

## 13. Delete states
a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

## 14. Cities in state
a Python file similar to model_state.py named model_city.py that contains the class definition of a City


