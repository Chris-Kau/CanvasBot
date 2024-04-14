from usermethods import userobject
from classassignments import assignment_list
import main
import todo
import todolist

def get_response(user_input):
    lowered: str = user_input.lower()
    #writes the user's assignments to 2 files, one is use for crossing out an assignment, other is used for storing data
    if "settoken" in user_input.lower()[:9]:
        user = userobject(user_input[9:])
        if user.check_token() == False:
            with open("token_state.txt", "w") as file:
                file.write('0')
            return "Invalid Access Token"

        f = open("bleh.txt", "w")
        f2 = open("bleh2.txt", "w")
        for i in range(len(assignment_list)):
            f.write(f"{str(i)}|{str(assignment_list[i])}\n")
            f2.write(f"{str(i)}|{str(assignment_list[i])}\n")
        f.close()
        f2.close()
        #token_state.txt allows us to check to see if the user has specified a valid key, if so, then we can call other functions
        #if token_state == 1, then the user has a valid key, else it's 0
        with open("token_state.txt", "w") as file:
            file.write('1')
        return "success!"
    if open("token_state.txt").read() == "1":
        if "todo" in user_input.lower()[:5]:
            #page gives us which page we want to view, can be specified with !todo 2
            try:
                page = int(user_input[5:])
            except:
                page = 1
            return todolist.print_todolist(assignment_list, page)
        if "check" in user_input.lower()[:6]:
            if int(user_input[6:]) > len(assignment_list):
                return("Assignment doesnt exist")
            #this function is in charge of crossing out the assignment in bleh2.txt
            todo.checktodo(user_input[6:])
            return f"Successfully checked out assignment {user_input[6:]}"
        
    else:
        return ("Please set a valid canvas api token using !settoken (your token)")
