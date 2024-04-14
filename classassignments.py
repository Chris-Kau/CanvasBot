# pip install canvasapi
from canvasapi import Canvas
from timeconverter import timeconverter
from sortdate import sortdate
API_URL = "https://csulb.instructure.com/"
API_KEY = "21139~ubrPGw0IftGsagPaMSinpKvz3AEjonQvU38lYF6UXPXjBsUERLcEZePJ71WMSmin" # api key / access token

canvas = Canvas(API_URL, API_KEY) # Initialize a new Canvas object
user = canvas.get_current_user()


courses = user.get_courses(enrollment_status='active')
course_list = []
for i in courses:
    try:
        # print(i.enrollment_term_id)
        if hasattr(i, 'name') and i.enrollment_term_id == 117: # 117 is spring 2024 term
            course_list.append(i)
    except Exception:
        continue


# for i in course_list:
#     print(i)


# print(course_list[0])
# for i in course_list[0].get_assignments(bucket="future"):
#     print(i)
#     print(timeconverter(i.due_at))

assignment_list = []
for i in range(len(course_list)):
    for j in course_list[i].get_assignments(bucket="future"):
        assignment_list.append(f"{j} {timeconverter(j.due_at)}")
        # print(j)
        # print(timeconverter(j.due_at))
assignment_list.sort(key=sortdate)
print(assignment_list)

# course = canvas.get_course(66891)
# print(course)

# GET /api/v1/courses/:course_id/assignments