# !todo gives todo list of upcoming for all classes. return it
import classassignments


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
    for i in range(len(classassignments.get_assignment_list())):
        dicttemp = {"index": str(i), "item": str(classassignments.get_assignment_list()[i]), "isChecked": "False"}
        if todo_list[i] != dicttemp:
            todo_list.insert(i, dicttemp)        
    return convertstring(todo_list)


def checktodo(num):
    temp = []
    file = open("bleh2.txt", "r").read()
    for line in file.split("\n"):
        temp.append(line)
    for idx in range(len(temp)):
        if idx == int(num) - 1:
            temp[idx] = "~~" + temp[idx]
            break
    file = open("bleh2.txt", "w")
    for line in temp:
        file.write(f"{line}\n")
    file.close()

    return (f"Assignment {num} has been marked completed :D")


