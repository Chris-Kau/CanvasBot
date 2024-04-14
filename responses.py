from usermethods import userobject
from classassignments import course_list, assignment_list
import main
import todo
import math
import discord

def get_response(user_input):
    lowered: str = user_input.lower()
    print("CHECKED", main.checked)
    if "settoken" in user_input.lower()[:9]:
        user = userobject(user_input[9:])
        if user.check_token() == False:
            return "Invalid Access Token"
        main.todo_list = []
        for i in range(len(assignment_list)):
            main.todo_list.append({"index": str(i), "item": str(assignment_list[i]), "isChecked": "False"})
        main.checked = 1
        return "success!"
    if main.checked == 1:
        if "hello" in lowered:
            return "hello there!"
        if "todo" in user_input.lower()[:5]:
            #try/except checks to see if a user specified a page number, if not, it defaults to first page
            try:
                page = int(user_input[5:])
            except:
                page = 1
            temp = (todo.todolist(main.todo_list)).split('\n')
            #checks to see if the user tries to access a non-existing page
            if (page-1)*10 > len(temp):
                return("Such page does not exist within your to-do list", 'sowwy :(')
            else:
                temp_str = ''
                for i in temp[(page-1)*10:(page*10)]:
                    temp_str += f"{i}\n"
                max_pages = math.ceil(len(temp) / 10)
                footer = f"Page {page} of {max_pages}"
            return (temp_str, footer)
        if "check" in user_input.lower()[:6]:
            return todo.checktodo(user_input[6:])
    else:
        return ("Please set your canvas api token using !settoken (your token)")
