# Project Overview
Two algorithm is implemented to completion of the project.

CSPs(constraint satisfaction problem) are consider a fundamental topic in Aritfical Intelligent(AI) and are essential for solving search, scheduling, planning and resource allocation problems.

CPM(Critical Path Method) Identifies the longest sequence of dependent tasks to determine the shortest possible project duration, allowing for task prioritization and float management.

# Technologies Used

Python

deque (Queue)

# How to Run

Install Python

Run the program: python main.py

# (algorithm used CSPs and CPM method)

Start

Step-1 Data structure initalization

create an impty dictionary self.data

Step-2

check it the data_set(the key) already exists in the dictionary.

if != present.

intialize the key with an empty list.

confirm the addition to the user a print statemtent.

step-3 Function: data_str

search the dictionary for date_str.

handling missing data

conditional check

Output: Return the formatted string of events.

step-4 Function: show month_year

this algorithm leverages an external library for visual output.

call the calendar.month()function using the provided year and month

Output: print the resulting string, which displays a formatted grid of the month

step-5 main progam loop(User interface)

Display menu: print option(view, month, addEvent, Viewday,Exit).

Conditional branching

Enter infinite loop

route choice of if, elif and else statement

step-6 Print the choice and restart the loop

End

visuals of the algorithm implemented

<img width="1910" height="1012" alt="smart calendar" src="https://github.com/user-attachments/assets/4486fbaa-1011-4fb0-88bd-18a4020cf310" />

code of the project 

[smart calendar.py](https://github.com/user-attachments/files/26314716/smart.calendar.py)
import calendar
from datetime import datetime

class SmartCalendar:
    def __init__(self):
        # A dictionary to stock { "YYYY/MM/DD": ["Event 1", "Event 2"] }
        self.data = {}

    def add_event(self, date_set, description):
        """Adds a new event to a specific date."""
        if date_set not in self.data:
            self.data[date_set] = []
        self.data[date_set].append(description)
        print(f"Successfully added: {description}")

    def view_day(self, date_str):
        """Retrieves all events for a specific date."""
        events = self.data.get(date_str, [])
        if not events:
            return "No events scheduled for this day."
        return "\n".join([f"- {e}" for e in events])

    def show_month(self, year, month):
        """Prints a visual calendar for the month."""
        print("\n" + calendar.month(year, month))

# --- Main Program Loop ---
my_cal = SmartCalendar()
current_date = datetime.now()

while True:
    print("\n--- Python Smart Calendar ---")
    print(f"Today is: {current_date.strftime('%Y-%m-%d')}")
    print("1. View Month\n2. Add Event\n3. View Events for a Day\n4. Exit")
    
    choice = input("Select (1-4): ")

    if choice == '1':
        my_cal.show_month(2026, 3) 
    
    elif choice == '2':
        date_input = input("Enter date (YYYY/MM/DD): ")
        event_input = input("What is the event? ")
        my_cal.add_event(date_input, event_input)
    
    elif choice == '3':
        date_input = input("Enter date to check (YYYY/MM/DD): ")
        print(f"\nEvents for {date_input}:")
        print(my_cal.view_day(date_input))
    
    elif choice == '4':
        print("Closing Calendar...")
    break


# Conclusion

This algorithm model problem by defining variables, domains and constraint which are then solved using search techniques like backtracking, rather than

traditional machine learning.
        
