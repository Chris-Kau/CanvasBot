# pip install canvasapi
from canvasapi import Canvas
API_URL = "https://csulb.instructure.com/"
API_KEY = "21139~ubrPGw0IftGsagPaMSinpKvz3AEjonQvU38lYF6UXPXjBsUERLcEZePJ71WMSmin" # api key / access token

canvas = Canvas(API_URL, API_KEY) # Initialize a new Canvas object
user = canvas.get_current_user()


courses = user.get_courses(enrollment_status='active')
course_list = []
for i in courses:
    try:
        if hasattr(i, 'name'):
            course_list.append(i)
    except Exception:
        continue

for i in course_list:
    print(i)

print()

print(course_list[0])
for i in course_list[0].get_assignments(bucket="future"):
    print(i)

# course = canvas.get_course(66891)
# print(course)

# GET /api/v1/courses/:course_id/assignments