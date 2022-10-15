#!python3
"""Countdown to Liftoff!"""

def do_countdown():
    """Print out the countdown"""
    time_remaining = 10

    while time_remaining >= 0:
        print(str(time_remaining))
        time_remaining = time_remaining - 1

do_countdown()
print("Ignition...")
print("LIFT OFF!!!!!!")
