import math
from timeconverter import time_to_word
from classassignments import get_course_name
def print_todolist(list, page):
    #try/except checks to see if a user specified a page number, if not, it defaults to first page
    #checks to see if the user tries to access a non-existing page
    if (page-1)*10 > len(list):
        return("Such page does not exist within your to-do list", 'sowwy :(')
    else:
        temp_str = ''
        file = open("bleh2.txt").read().split("\n")
        for idx, i in enumerate(list[(page-1)*10:(page*10)]):
            course_id = int(i.split('|')[0])
            #course_name[0] = CECS, course_name[1] = 229
            course_name = get_course_name(course_id).split(' ', 2)
            time_split = i.replace('|', ' ')[5:].rsplit(' ', 2)
            #gets time, and is then put into a readable format using time_to_word()
            get_time = (time_split[1] + ' ' + time_split[2])
            #ass_name[0][6:] is assingment name. We start at 6 to get rid of ugly course number
            ass_name = i.replace('|', ' ').rsplit(' ', 3)
            #~~ indicates that that assignemnt has been crossed out
            if "~~" in file[idx + (page-1)*10]:
                temp_str += f"~~**({(idx + (page-1)*10) + 1})** *{time_to_word(get_time)}* - {course_name[0]} {course_name[1]} {ass_name[0][6:]} ~~\n"
            else:
                temp_str += f"**({(idx + (page-1)*10) + 1})** *{time_to_word(get_time)}* - {course_name[0]} {course_name[1]} {ass_name[0][6:]} \n"
        #temp_str holds all of the assignments
        max_pages = math.ceil(len(list) / 10)
        footer = f"Page {page} of {max_pages}"
    return (temp_str, footer)