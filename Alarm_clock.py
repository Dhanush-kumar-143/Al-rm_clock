from datetime import datetime
import time


class AlarmClock:
    def __init__(self):
        self.alarms = []

    def add_alarm(self):
        alarm_time = input("Enter alarm time (HH:MM): ").strip()

        try:
            datetime.strptime(alarm_time, "%H:%M")
            self.alarms.append(alarm_time)
            print(f"Alarm set for {alarm_time}")
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    def list_alarms(self):
        if not self.alarms:
            print("No alarms set.")
            return

        print("\nCurrent Alarms:")
        for index, alarm in enumerate(self.alarms, start=1):
            print(f"{index}. {alarm}")

    def delete_alarm(self):
        if not self.alarms:
            print("No alarms to delete.")
            return

        self.list_alarms()

        try:
            choice = int(input("Enter alarm number to delete: "))
            removed_alarm = self.alarms.pop(choice - 1)
            print(f"Removed alarm: {removed_alarm}")
        except (ValueError, IndexError):
            print("Invalid selection.")

    def start_alarm_monitor(self):
        if not self.alarms:
            print("No alarms set.")
            return

        print("\nAlarm monitor started.")
        print("Press Ctrl+C to stop.\n")

        try:
            while True:
                current_time = datetime.now().strftime("%H:%M")

                triggered = [
                    alarm for alarm in self.alarms
                    if alarm == current_time
                ]

                for alarm in triggered:
                    print("\n" + "=" * 30)
                    print(f"⏰ ALARM! Time: {alarm}")
                    print("=" * 30)

                    self.alarms.remove(alarm)

                time.sleep(30)

        except KeyboardInterrupt:
            print("\nAlarm monitor stopped.")


def main():
    clock = AlarmClock()

    while True:
        print("\n===== Alarm Clock =====")
        print("1. Add Alarm")
        print("2. View Alarms")
        print("3. Delete Alarm")
        print("4. Start Alarm Monitor")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clock.add_alarm()

        elif choice == "2":
            clock.list_alarms()

        elif choice == "3":
            clock.delete_alarm()

        elif choice == "4":
            clock.start_alarm_monitor()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()