import math
from timeconverter import timeconverter, time_to_word
from classassignments import get_course_name
def print_todolist(list, page):
    #try/except checks to see if a user specified a page number, if not, it defaults to first page
    #checks to see if the user tries to access a non-existing page
    if (page-1)*10 > len(list):
        return("Such page does not exist within your to-do list", 'sowwy :(')
    else:
        temp_str = ''
        for idx, i in enumerate(list[(page-1)*10:(page*10)]):
            course_id = int(i.split('|')[0])
            course_name = get_course_name(course_id).split(' ', 2)
            time_split = i.replace('|', ' ')[5:].rsplit(' ', 2)
            get_time = (time_split[1] + ' ' + time_split[2])
            ass_name = i.replace('|', ' ').rsplit(' ', 3)
            if "~~" in open("bleh2.txt").read().split("\n")[idx + (page-1)*10]:
                temp_str += f"~~**({(idx + (page-1)*10) + 1})** *{time_to_word(get_time)}* - {course_name[0]} {course_name[1]} {ass_name[0][6:]} ~~\n"
            else:
                temp_str += f"**({(idx + (page-1)*10) + 1})** *{time_to_word(get_time)}* - {course_name[0]} {course_name[1]} {ass_name[0][6:]} \n"

        max_pages = math.ceil(len(list) / 10)
        footer = f"Page {page} of {max_pages}"
        #formatted = format()
    return (temp_str, footer)

def format():
    temp = ""
    file2 = open("bleh2.txt", "r").read()
    for line in file2.split('\n'):
        if "~~" in line:
            temp += "~~" + line + "~~" + "\n"
        else:
            temp += line + "\n"
    return temp
