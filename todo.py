# !todo gives todo list of upcoming for all classes. return it
from blehh import course_list

def todolist():
    print("---------------------------------")

    todo_list = ""
    for i in range(len(course_list)):
        todo_list = todo_list + str(i) + " " + str(course_list[i]) + "\n"

    print(todo_list)
    return todo_list
