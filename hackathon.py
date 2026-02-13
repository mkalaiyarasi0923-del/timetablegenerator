Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... from collections import defaultdict
... 
... # -----------------------------
... # CONFIGURATION
... # -----------------------------
... 
... days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
... periods_per_day = 6
... 
... subjects = {
...     "Math": {"teacher": "Mr. Sharma", "hours_per_week": 5},
...     "Physics": {"teacher": "Ms. Rao", "hours_per_week": 4},
...     "Chemistry": {"teacher": "Dr. Khan", "hours_per_week": 4},
...     "English": {"teacher": "Mrs. Das", "hours_per_week": 5},
...     "Computer": {"teacher": "Mr. Verma", "hours_per_week": 4},
... }
... 
... classrooms = ["Room A", "Room B"]
... 
... # -----------------------------
... # TIMETABLE GENERATOR
... # -----------------------------
... 
... def generate_timetable():
...     timetable = {day: [None]*periods_per_day for day in days}
...     teacher_schedule = defaultdict(lambda: {day: [False]*periods_per_day for day in days})
...     room_schedule = defaultdict(lambda: {day: [False]*periods_per_day for day in days})
... 
...     subject_pool = []
... 
...     # Create subject pool based on required hours
...     for subject, details in subjects.items():
...         subject_pool.extend([subject] * details["hours_per_week"])
... 
    random.shuffle(subject_pool)

    for subject in subject_pool:
        placed = False
        attempts = 0

        while not placed and attempts < 100:
            day = random.choice(days)
            period = random.randint(0, periods_per_day - 1)
            teacher = subjects[subject]["teacher"]

            # Check if slot is free
            if timetable[day][period] is None:
                if not teacher_schedule[teacher][day][period]:

                    # Find available classroom
                    for room in classrooms:
                        if not room_schedule[room][day][period]:

                            # Assign
                            timetable[day][period] = {
                                "subject": subject,
                                "teacher": teacher,
                                "room": room
                            }

                            teacher_schedule[teacher][day][period] = True
                            room_schedule[room][day][period] = True
                            placed = True
                            break
            attempts += 1

        if not placed:
            print(f"⚠ Could not schedule {subject}")

    return timetable

# -----------------------------
# DISPLAY FUNCTION
# -----------------------------

def print_timetable(timetable):
    for day in days:
        print(f"\n📅 {day}")
        for i, period in enumerate(timetable[day]):
            if period:
                print(f"  Period {i+1}: {period['subject']} "
                      f"({period['teacher']}) - {period['room']}")
            else:
                print(f"  Period {i+1}: Free")

# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    timetable = generate_timetable()
    print_timetable(timetable)
import random
from collections import defaultdict

# -----------------------------
# CONFIGURATION
# -----------------------------

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6

subjects = {
    "Math": {"teacher": "Mr. Sharma", "hours_per_week": 5},
    "Physics": {"teacher": "Ms. Rao", "hours_per_week": 4},
    "Chemistry": {"teacher": "Dr. Khan", "hours_per_week": 4},
    "English": {"teacher": "Mrs. Das", "hours_per_week": 5},
    "Computer": {"teacher": "Mr. Verma", "hours_per_week": 4},
}

classrooms = ["Room A", "Room B"]

# -----------------------------
# TIMETABLE GENERATOR
# -----------------------------

def generate_timetable():
    timetable = {day: [None]*periods_per_day for day in days}
    teacher_schedule = defaultdict(lambda: {day: [False]*periods_per_day for day in days})
    room_schedule = defaultdict(lambda: {day: [False]*periods_per_day for day in days})

    subject_pool = []

    # Create subject pool based on required hours
    for subject, details in subjects.items():
        subject_pool.extend([subject] * details["hours_per_week"])

    random.shuffle(subject_pool)

    for subject in subject_pool:
        placed = False
        attempts = 0

        while not placed and attempts < 100:
            day = random.choice(days)
            period = random.randint(0, periods_per_day - 1)
            teacher = subjects[subject]["teacher"]

            # Check if slot is free
            if timetable[day][period] is None:
                if not teacher_schedule[teacher][day][period]:

                    # Find available classroom
                    for room in classrooms:
                        if not room_schedule[room][day][period]:

                            # Assign
                            timetable[day][period] = {
                                "subject": subject,
                                "teacher": teacher,
                                "room": room
                            }

                            teacher_schedule[teacher][day][period] = True
                            room_schedule[room][day][period] = True
                            placed = True
                            break
            attempts += 1

        if not placed:
            print(f"⚠ Could not schedule {subject}")

    return timetable

# -----------------------------
# DISPLAY FUNCTION
# -----------------------------

def print_timetable(timetable):
    for day in days:
        print(f"\n📅 {day}")
        for i, period in enumerate(timetable[day]):
            if period:
                print(f"  Period {i+1}: {period['subject']} "
                      f"({period['teacher']}) - {period['room']}")
            else:
                print(f"  Period {i+1}: Free")

# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    timetable = generate_timetable()
    print_timetable(timetable)
