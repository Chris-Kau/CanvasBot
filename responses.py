from usermethods import userobject
#from classassignments import assignment_list
import classassignments
import todo
import todolist
import copy

def get_response(user_input):
    lowered: str = user_input.lower()
    if "help" in lowered:
        #returns a list of commands
        return(f"**!guide** -> shows you how to get your Canvas API Token\n**!settoken (token)** -> sets your Canvas API token so we can access your classes and assignments\n**!todo** -> returns a list of assignments; you can swap pages using !todo (page number)\n**!check (assignment num)** -> crosses off the chosen assignment to mark that you've completed it\n**!reminder** -> DM's the user all the assignments that are due within 3 days every 6 hours\n**!cats** -> erm.. cats?!")
    elif "guide" in lowered:
        return(f"Head over to https://csulb.instructure.com/profile/settings and scroll down until you see New Access Token")
    else:
        #writes the user's assignments to 2 files, one is use for crossing out an assignment, other is used for storing data
        if "settoken" in user_input.lower()[:9]:
            with open("user_token.txt", "w") as file:
                file.write(user_input[9:])
            user = userobject(open("user_token.txt").read())
            if user.check_token() == False:
                with open("token_state.txt", "w") as file:
                    file.write('0')
                return "Invalid Access Token"
            f = open("bleh.txt", "w")
            f2 = open("bleh2.txt", "w")
            global assignments
            assignments = copy.copy(list(classassignments.get_assignment_list()))
            for i in range(len(assignments)):
                temp_string = f"{str(i)}|{str(assignments[i])}\n"
                f.write(temp_string)
                f2.write(temp_string)
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
                return todolist.print_todolist(assignments, page)
            elif "check" in user_input.lower()[:6]:
                if int(user_input[6:]) > len(assignments):
                    return("Assignment doesnt exist")
                #this function is in charge of crossing out the assignment in bleh2.txt
                todo.checktodo(user_input[6:])
                return f"Successfully checked out assignment {user_input[6:]}"
            else:
                return("Please use a valid command.")
        else:
            return ("Please set a valid canvas api token using !settoken (your token)")
