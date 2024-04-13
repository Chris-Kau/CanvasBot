import usermethods
import todo

def get_response(user_input):
    lowered: str = user_input.lower()
    if "hello" in lowered:
        return "hello there!"
    if "todo" in lowered:
        return todo.todolist()

    
    if "settoken" in user_input.lower()[:9]:
        usermethods.API_TOKEN = user_input[9:]
        temp = usermethods.API_TOKEN
        return usermethods.create_user_object(temp)