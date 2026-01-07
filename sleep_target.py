def base_sleep_by_age(age):
    """Return base sleep hours based on age"""
    if age<= 25:
        return 8.0
    elif age <= 64:
        return 7.5
    else:
        return 7.0
def adjust_for_activity(base_sleep, activity):
    """Return the extra sleep hours based on activity"""
    if activity == "high":
        return base_sleep + 0.5, "High activity adds 0.5h"
    elif activity == "medium":
        return base_sleep + 0.25, "Medium activity adds 0.25h"
    else:
        return base_sleep, "Low activity adds 0h"
def adjust_for_caffeine(current_sleep, cups):
    """Adjust sleep based on caffeine cups and return (new_sleep, reason_text)."""
    if cups >= 4:
        return current_sleep + 0.75, "High caffeine (4+ cups) adds 0.75h."
    elif cups >= 2:
        return current_sleep + 0.25, "Moderate caffeine (2-3 cups) adds 0.25h."
    else:
        return current_sleep, "Low caffeine (0-1 cup) adds 0h."


def get_sleep_recommendation(age, activity,cups):
    """Return final sleep hours and reason based on age and activity."""
    base = base_sleep_by_age(age)
    after_activity, activity_reason = adjust_for_activity(base, activity)
    final_sleep, caffeine_reason = adjust_for_caffeine(after_activity, cups)
    reason = (f"Based on your age ({age}), your base sleep need is {base} hours. "
              f"{activity_reason} {caffeine_reason}")

    return final_sleep, reason
def get_valid_activity():
    """Ask for activity level until the input is valid."""
    while True:
        activity = input("Activity level (low / medium / high): ").strip().lower()
        if activity in ["low", "medium", "high"]:
            return activity
        print("Invalid input. Please enter low, medium, or high.")
def get_valid_age():
    """Ask for age until a valid positive integer is given."""
    while True:
        user_input = input("Please enter your age: ").strip()
        if user_input.isdigit():
            age = int(user_input)
            if age > 0:
                return age
        print("Invalid age. Please enter a positive number.")
def get_valid_cups():
    """Ask for caffeine cups per day until a valid integer 0-10 is given."""
    while True:
        s = input("Caffeine cups per day (0-10): ").strip()
        if s.isdigit():
            cups = int(s)
            if 0 <= cups <= 10:
                return cups
        print("Invalid input. Please enter an integer between 0 and 10.")



if __name__== "__main__":
    """Main entry point: get user input and print sleep recommendation"""
    activity = get_valid_activity()
    age = get_valid_age()
    cups = get_valid_cups()
    target, reason = get_sleep_recommendation(age, activity, cups)

    print("=== SleepMatch ===")
    print("Recommended sleep hours:", target)
    print("Reason:", reason)
    print("==================")