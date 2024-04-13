# !todo gives todo list of upcoming for all classes. return it
from blehh import course_list

todo_list = [] # list of dicts

def convertstring(listdict):
    text = ""
    for i, dict in enumerate(listdict):
        for key, value in dict.items():
            text = text + value + " "
        text += "\n"
    return text


def todolist():
    print("---------------------------------")

    for i in range(len(course_list)):
        todo_list.append({"index": str(i), "item": str(course_list[i])})

    # print(convertstring(todo_list))
    return convertstring(todo_list)



def checktodo(num):
    for i in range(len(todo_list)):
        if todo_list[i]["index"] == num:
            del todo_list[i]
            break
