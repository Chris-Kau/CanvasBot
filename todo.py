# !todo gives todo list of upcoming for all classes. return it
from classassignments import course_list

#todo_list = [] # list of dicts

def convertstring(listdict):
    text = ""
    for i, dict in enumerate(listdict): # for dict in list of dicts
        for key, value in dict.items(): # for pairs in dict. find a way to strikethorough? 
            text = text + str(value) + " "
        text += "\n"
    return text


def todolist(todo_list):
    print("---------------------------------")
    for i in range(len(course_list)):
        dicttemp = {"index": str(i), "item": str(course_list[i]), "isChecked": "False"}
        if todo_list[i] != dicttemp:
            todo_list.insert(i, dicttemp)
            # todo_list.append(dicttemp) # appends every time u look at todo list :( fixed?
        
    #print(convertstring(todo_list))
    return convertstring(todo_list)

# have isChecked be a thing
# have todolist func check if item is already there or not, if not then add it
# print todolist with isChecked being strikethroughed

def checktodo(num): # isnt removing the item properly :/
    for i in range(len(todo_list)):
        if todo_list[i]["index"] == num:
            todo_list[i].isChecked = True
            break

    # for i, d in enumerate(todo_list):
    #     if d['index'] == num:
    #         id = i
    #         break
    # if id is not None:
    #     todo_list.pop(id)
    return convertstring(todo_list)

