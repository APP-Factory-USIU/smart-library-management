import sys


def main():
    while True:
        user = input("Name: ")
        app_name = input("Enter appliance Name: ")
        power = int(input("Power: "))
        hours = int(input("Hrs: "))
        days = int(input("Days: "))

        choices = input(
            "Enter a choice: \n1. Calculate total energy and cost \n2. Show table \n3. Exit"
        )
        if choices == "1":
            ans = PowerSoln(power, hours, days, user)
            print(ans)
        elif choices == "2":
            show_table(user, power, hours, days, formula, total_cost)
        elif choices == "3":
            sys.exit("Thanks for using this program!")
        else:
            return "INvalid choice"

        # Invoke the func


def PowerSoln(watts, hours, days, user):
    # Calculate the total energy
    global formula
    global total_cost

    formula = (watts * hours * days) / 1000
    total_cost = 25 * formula
    global contents
    contents = []

    local_storage_and_display(user, watts, hours, days, formula, total_cost)

    return f"Total energy is {formula} Kwh at a total cost of {total_cost} KES"


def local_storage_and_display(user, watts, hours, days, formula, total_cost):
    # Initialize the storage

    new_user = {
        "user": {
            user: [
                {"watts": watts},
                {"hours": hours},
                {"days": days},
                {"formula": formula},
                {"total_cost": total_cost},
            ]
        }
    }

    # global single_user
    # single_user = []
    # single_user.append(user.copy())
    # print(single_user)

    print(f"User {user} added.")

    contents.append(new_user.copy())

    for i in range(len(contents)):
        print(i, contents[i])


def show_table(user, watts, hours, days, formula, total_cost):
    # Displays the summary
    local_storage_and_display(user, watts, hours, days, formula, total_cost)
    header = f"| {'User':<10} | {'Power':<7} | {'Hours':<7} | {'Days':<7} | {'Total Power':<7} | {'Total Cost':<12} |"
    print(header)
    ln_break = len(header)
    print("-" * ln_break)

    # {
    #     "user": {
    #         "rew": [
    #             {"watts": 5},
    #             {"hours": 7},
    #             {"days": 8},
    #             {"formula": 0.28},
    #             {"total_cost": 7.000000000000001},
    #         ]
    #     }
    # }

    for i in range(len(contents)):
        # print(i, contents[i])
        keys = list(contents[i]["user"].keys())
        for key in keys:
            # print(key)
            for i in range(len(key)):
                watts1 = key[i]
                print(watts)
                # hrs = key[i]['hours']
                # form = key[i]['formula']
                # ts = key[i]['total_cost']
                body = f"| {key:<10} | {watts1:<7} |" # {hrs:<7} | {days:<7} | {form:<12} | {ts:<12} |"
                print(body)

    # for i, name in enumerate(single_user, 1):
    #     print(i, name)


if __name__ == "__main__":
    main()
