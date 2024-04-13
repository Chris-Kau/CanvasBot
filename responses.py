from usermethods import userobject
from classassignments import course_list
import main
import todo

def get_response(user_input):
    lowered: str = user_input.lower()
    print("CHECKED", main.checked)
    if main.checked == 1:
        if "hello" in lowered:
            return "hello there!"
        if "todo" in lowered:
            print("YPI GPTPO INNN")
            return todo.todolist(main.todo_list)
        if "check" in user_input.lower()[:6]:
            return todo.checktodo(user_input[6:])
    else:
        if "settoken" in user_input.lower()[:9]:
            user = userobject(user_input[9:])
            if user.check_token() == False:
                return "Invalid Access Token"
            main.todo_list = []
            for i in range(len(course_list)):
                main.todo_list.append({"index": str(i), "item": str(course_list[i]), "isChecked": "False"})
            main.checked = 1
            return "success!"