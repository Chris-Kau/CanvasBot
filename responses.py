from usermethods import userobject
from classassignments import assignment_list, access_ass
import main
import todo
import todolist

def get_response(user_input):
    lowered: str = user_input.lower()
    if "settoken" in user_input.lower()[:9]:
        user = userobject(user_input[9:])
        if user.check_token() == False:
            return "Invalid Access Token"
        f = open("bleh.txt", "w")
        for i in range(len(assignment_list)):
            f.write(f"{str(i)}||{str(assignment_list[i])}\n")
        f.close()
        main.checked = 1
        return "success!"
    if main.checked == 1:
        if "hello" in lowered:
            return "hello there!"
        if "todo" in user_input.lower()[:5]:
            try:
                page = int(user_input[5:])
            except:
                page = 1
            assignment_objects = []
            file = open("bleh.txt", "r").read()
            for line in file.splitlines():
                assid = line.split('||')[2].rsplit(' ', 2)[2][1:-1]
                classid = line.split('||')[1]
                assignment_objects.append(access_ass(classid, assid))
            return todolist.print_todolist(assignment_objects, page)
        if "check" in user_input.lower()[:6]:
            result = todo.checktodo(user_input[6:])
            #tdlist.set_list(result[1])
            return "yppipewidaw"
        
    else:
        return ("Please set your canvas api token using !settoken (your token)")
