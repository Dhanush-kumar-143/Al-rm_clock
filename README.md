# Alarm Clock

A simple command-line alarm clock in Python. Set multiple alarms, view or delete them, and run a background monitor that alerts you when the current time matches an alarm.

## Features

- **Add alarms** — Enter times in 24-hour `HH:MM` format (e.g. `07:30`, `14:00`).
- **View alarms** — List all active alarms with numbered entries.
- **Delete alarms** — Remove an alarm by its list number.
- **Alarm monitor** — Polls the clock every 30 seconds; prints an alert when an alarm fires, then removes that alarm from the list.
- **Interactive menu** — Looping CLI with options 1–5 until you exit.

## Requirements

- Python 3.6+
- No third-party packages (uses only the standard library: `datetime`, `time`)

## Project files

| File | Description |
|------|-------------|
| `Alarm_clock.py` | Main program: `AlarmClock` class and menu-driven `main()` |

## How to run

From this folder:

```bash
python Alarm_clock.py
```

### Menu options

```
===== Alarm Clock =====
1. Add Alarm
2. View Alarms
3. Delete Alarm
4. Start Alarm Monitor
5. Exit
```

1. **Add Alarm** — Prompts for `HH:MM`. Invalid format shows: `Invalid time format. Please use HH:MM.`
2. **View Alarms** — Shows `No alarms set.` or a numbered list under `Current Alarms:`.
3. **Delete Alarm** — Lists alarms, then asks for a number. Handles invalid input with `Invalid selection.`
4. **Start Alarm Monitor** — Requires at least one alarm. Checks time every **30 seconds**. On match, prints a bordered alert and removes that alarm. Stop with **Ctrl+C** (`Alarm monitor stopped.`).
5. **Exit** — Prints `Goodbye!` and quits.

## Code structure

### `AlarmClock` class

| Method | Behavior |
|--------|----------|
| `__init__` | Initializes empty list `self.alarms` |
| `add_alarm()` | Reads time from input, validates with `datetime.strptime(..., "%H:%M")`, appends on success |
| `list_alarms()` | Prints all alarms or `No alarms set.` |
| `delete_alarm()` | `pop(choice - 1)` after user picks index; handles `ValueError` / `IndexError` |
| `start_alarm_monitor()` | Infinite loop: compares `datetime.now().strftime("%H:%M")` to each alarm; triggers matching alarms; `time.sleep(30)`; `KeyboardInterrupt` exits cleanly |

### Entry point

```python
if __name__ == "__main__":
    main()
```

`main()` creates one `AlarmClock` instance and drives the menu until option `5`.

## Example session

```
Choose an option: 1
Enter alarm time (HH:MM): 09:00
Alarm set for 09:00

Choose an option: 4

Alarm monitor started.
Press Ctrl+C to stop.

==============================
⏰ ALARM! Time: 09:00
==============================
```

## Notes

- Times use the system’s local clock (`datetime.now()`).
- The monitor checks every 30 seconds, so an alarm may fire up to ~30 seconds after the exact minute.
- Each alarm fires once; it is removed from the list after triggering.

## License

Free to use and modify for personal or learning projects.
