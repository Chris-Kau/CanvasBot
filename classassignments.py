# pip install canvasapi
from canvasapi import Canvas
from timeconverter import timeconverter
from sortdate import sortdate


def set_user():
    API_URL = "https://csulb.instructure.com/"
    API_KEY = open("user_token.txt").read() # api key / access token

    canvas = Canvas(API_URL, API_KEY) # Initialize a new Canvas object
    user = canvas.get_current_user()
    return [user, canvas]

def get_courses():
    user = set_user()[0]
    courses = user.get_courses(enrollment_status='active')
    course_list = []
    for i in courses:
        try:
            if hasattr(i, 'name') and i.enrollment_term_id == 117: # 117 is spring 2024 term
                course_list.append(i)
        except Exception:
            continue
    return course_list

def get_assignment_list():
    course_list = get_courses()
    assignment_list = []
    for i in range(len(course_list)):
        for j in course_list[i].get_assignments(bucket="future"):
            assignment_list.append(f"{str(course_list[i]).rsplit(' ', 1)[1][1:-1]}|{j}|{timeconverter(j.due_at)}")
    assignment_list.sort(key=sortdate)
    return assignment_list


def get_course_name(id):
    canvas = set_user()[1]
    return canvas.get_course(id).name