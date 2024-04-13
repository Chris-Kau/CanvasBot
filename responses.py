from usermethods import userobject
import todo

def get_response(user_input):
    lowered: str = user_input.lower()
    if "hello" in lowered:
        return "hello there!"
    if "todo" in lowered:
        return todo.todolist()
    if "check" in user_input.lower()[:6]:
        return todo.checktodo(user_input[6:])

    
    if "settoken" in user_input.lower()[:9]:
        user = userobject(user_input[9:])
        if user.check_token() == False:
            return "Invalid Access Token"
        return "success!"