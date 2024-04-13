# !todo gives todo list of upcoming for all classes. return it
from blehh import course_list

def convertlist(listdict):
    for dict in listdict:
        print(*(f'{k}: {v}' for k, v in dict.items()), sep='', end='\n')


# def todolist():
print("---------------------------------")

todo_list = [] # list of dicts
for i in range(len(course_list)):
    todo_list.append({"index": str(i), "item": str(course_list[i])})
    # todo_list = todo_list + str(i) + " " + str(course_list[i]) + "\n"

print(convertlist(todo_list))
# return todo_list




def checktodo(num):
    for i in range(len(course_list)):
        if i == 0:
            return 0
            # bruh
    return 0
