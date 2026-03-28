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