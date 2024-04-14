import math
from timeconverter import timeconverter
def print_todolist(list, page):
    #try/except checks to see if a user specified a page number, if not, it defaults to first page
    #checks to see if the user tries to access a non-existing page
    if (page-1)*10 > len(list):
        return("Such page does not exist within your to-do list", 'sowwy :(')
    else:
        temp_str = ''
        for i in list[(page-1)*10:(page*10)]:
            temp_str += f"{i} {timeconverter(i.due_at)}\n"
        max_pages = math.ceil(len(list) / 10)
        footer = f"Page {page} of {max_pages}"
    return (temp_str, footer)
