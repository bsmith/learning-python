#!python3

import inspect
import sys
import uuid

prodid = f"-//bsmith/{__file__}//NONSGML v1.0//EN";
print(inspect.cleandoc(f"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:{prodid}
"""))

uid       = uuid.uuid4()
dtstamp   = "20221022T153600Z"
organizer = "CN=Benjamin Smith:MAILTO:bahsmith@gmail.com"
dtstart   = "20221022T153000Z"
dtend     = "20221022T163000Z"
summary   = "Write TimeBlocking script"

print(inspect.cleandoc(f"""
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
ORGANIZER;{organizer}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{summary}
END:VEVENT
"""))

print(inspect.cleandoc(f"""
END:VCALENDAR
"""))

print(__file__ + ": done", file=sys.stderr)