# !todo gives todo list of upcoming for all classes. return it
from classassignments import course_list, assignment_list
import responses
import copy

#todo_list = [] # list of dicts

def convertstring(listdict):
    text = ""
    for i, dict in enumerate(listdict): # for dict in list of dicts
        for key, value in dict.items(): # for pairs in dict. find a way to strikethorough?
            if key == "index":
                text = text + str(int(value) + 1) + " "
            else:
                text = text + str(value) + " "
        text += "\n"
    return text


def todolist(todo_list):
    #print("---------------------------------")
    for i in range(len(assignment_list)):
        dicttemp = {"index": str(i), "item": str(assignment_list[i]), "isChecked": "False"}
        if todo_list[i] != dicttemp:
            todo_list.insert(i, dicttemp)
            # todo_list.append(dicttemp) # appends every time u look at todo list :( fixed?
        
    # print(convertstring(todo_list))
    return convertstring(todo_list)

# have isChecked be a thing
# have todolist func check if item is already there or not, if not then add it
# print todolist with isChecked being strikethroughed

def checktodo(num): # isnt removing the item properly :/
    temp = []
    file = open("bleh.txt", "r").read()
    for line in file.split("\n"):
        temp.append(line)
    for idx in range(len(temp)):
        if idx == int(num) - 1:
            temp[idx] = "~~" + temp[idx]
            break
    file = open("bleh.txt", "w")
    for line in temp:
        file.write(f"{line}\n")
    file.close()
    # for i in range(len(temp)):
    #     if int(temp[i]["index"]) == int(num) - 1:
    #         temp[i]["item"] = "~~"+temp[i]["item"]+"~~"
    #         break
    return (f"Assignment {num} has been marked completed :D")

    # for i, d in enumerate(todo_list):
    #     if d['index'] == num:
    #         id = i
    #         break
    # if id is not None:
    #     todo_list.pop(id)
    return convertstring(todo_list)

