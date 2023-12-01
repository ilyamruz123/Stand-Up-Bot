import datetime

class StandupBot:
    def __init__(self):
        self.meeting_schedule = {}

    def schedule_meeting(self, team_member, date, time):
        meeting_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        if team_member in self.meeting_schedule:
            self.meeting_schedule[team_member].append(meeting_datetime)
        else:
            self.meeting_schedule[team_member] = [meeting_datetime]

    def display_schedule(self):
        for team_member, meetings in self.meeting_schedule.items():
            print(f"{team_member}'s Meetings:")
            for meeting in meetings:
                print(f"- {meeting.strftime('%Y-%m-%d %H:%M')}")
            print()

def main():
    standup_bot = StandupBot()

    while True:
        print("1. Schedule a meeting")
        print("2. Display schedule")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            team_member = input("Enter team member's name: ")
            date = input("Enter meeting date (YYYY-MM-DD): ")
            time = input("Enter meeting time (HH:MM): ")
            standup_bot.schedule_meeting(team_member, date, time)
            print("Meeting scheduled successfully!\n")
        elif choice == "2":
            standup_bot.display_schedule()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
