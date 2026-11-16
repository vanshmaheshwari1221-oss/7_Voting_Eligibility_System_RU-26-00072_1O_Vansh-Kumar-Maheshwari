"""PS 7 - Voting Eligibility System
Checks whether a person can vote (age >= 18 and Indian citizen).
"""

MIN_VOTING_AGE = 18
MAX_AGE = 120


def get_name():
    """Ask for a name until a non-empty one is entered."""
    while True:
        name = input("Name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def get_age():
    """Ask for age until a valid whole number from 0 to 120 is entered."""
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue
        if 0 <= age <= MAX_AGE:
            return age
        print(f"Invalid age. Age must be between 0 and {MAX_AGE}.")


def get_yes_no(prompt):
    """Ask a y/n question until the answer is 'y' or 'n'."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("Please enter y or n.")


def check_eligibility(age, citizen):
    """Return (eligible, list_of_reason_lines)."""
    years_left = MIN_VOTING_AGE - age
    if age >= MIN_VOTING_AGE and citizen == "y":
        return True, []
    elif age < MIN_VOTING_AGE and citizen == "n":
        return False, [
            "Reason: Not an Indian citizen.",
            f"Years left to become eligible: {years_left}",
        ]
    elif age < MIN_VOTING_AGE:
        return False, [f"Years left to become eligible: {years_left}"]
    else:
        return False, ["Reason: Not an Indian citizen."]


def main():
    checked = eligible_count = not_eligible_count = 0

    while True:
        name = get_name()
        age = get_age()
        citizen = get_yes_no("Indian citizen (y/n): ")

        eligible, reasons = check_eligibility(age, citizen)
        checked += 1

        if eligible:
            eligible_count += 1
            print(f"{name} is eligible to vote.")
        else:
            not_eligible_count += 1
            print(f"{name} is not eligible to vote.")
            for line in reasons:
                print(line)

        if get_yes_no("Check another voter? (y/n): ") == "n":
            break
        print()

    print(f"Voters checked: {checked} | Eligible: {eligible_count} "
          f"| Not eligible: {not_eligible_count}")


if __name__ == "__main__":
    main()
