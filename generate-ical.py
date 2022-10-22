#!python3

import inspect
from operator import length_hint
import sys
import uuid
import os.path

def ical_header():
    prodid = f"-//bsmith/{os.path.basename(__file__)}//NONSGML v1.0//EN";
    return inspect.cleandoc(f"""
        BEGIN:VCALENDAR
        VERSION:2.0
        PRODID:{prodid}
    """)

def ical_trailer():
    return inspect.cleandoc(f"""
        END:VCALENDAR
    """)

def ical_event(event):
    if event is None:
        return ""
    return ical_event2(**event)
def ical_event2(dtstamp, organizer, dtstart, dtend, summary):
    uid = uuid.uuid4() # each stanza must have a unique ID
    return inspect.cleandoc(f"""
        BEGIN:VEVENT
        UID:{uid}
        DTSTAMP:{dtstamp}
        ORGANIZER;{organizer}
        DTSTART:{dtstart}
        DTEND:{dtend}
        SUMMARY:{summary}
        END:VEVENT
    """)

#uid       = uuid.uuid4()
dtstamp   = "20221022T153600Z"
organizer = "CN=Benjamin Smith:MAILTO:bahsmith@gmail.com"

days = [
    { "date": "20221024", "start": 8 },
    { "date": "20221025", "start": 8 },
    { "date": "20221026", "start": 8 },
    { "date": "20221027", "start": 8 },
    { "date": "20221028", "start": 8 },
]

blocks = [
    { "summary": "get to codeclan", "length": 1 },
    { "summary": "homework recap", "length": 0.5 },
    { "summary": "stand-up", "length": 0.25 },
    { "summary": "morning lesson", "until": 12 },
    { "summary": "lunch", "length": 1 },
    { "summary": "afternoon lesson", "until": 17 },
]

# events = [
#     {
#         "uid":       uid,
#         "dtstamp":   dtstamp,
#         "organizer": organizer,
#         "dtstart":   "20221022T153000Z",
#         "dtend":     "20221022T163000Z",
#         "summary":   "Write TimeBlocking script",
#     }
# ]

# NB this just subtracts an hour for UTC XXX
def make_timestring(date, time):
    return date + "T" + \
        format(int(time - 1), "02d") + \
        format(int(60*(time - int(time))), "02d") + \
        "00Z"

def make_event_from_block(state, date, block):
    current_time = state["time"]

    dtstart = make_timestring(date, current_time)

    event_length = None
    if "length" in block:
        event_length = block["length"]
    elif "until" in block:
        event_length = block["until"] - current_time

    current_time += event_length
    dtend = make_timestring(date, current_time)

    state["time"] = current_time
    return {
        "dtstamp":   dtstamp,
        "organizer": organizer,
        "dtstart":   dtstart,
        "dtend":     dtend,
        "summary":   block["summary"],
    }

events = []
for day in days:
    state = { "time": day["start"] }
    for block in blocks:
        events.append(make_event_from_block(state, day["date"], block))

print(ical_header())
for event in events:
    print(ical_event(event))
print(ical_trailer())

print(__file__ + ": done", file=sys.stderr)