import json


def load_adventure_file():
    # load the json file and convert it to a python dict
    with open('adventure.json', 'r') as file:
        file_data = file.read()
        loaded_adventure = json.loads(file_data)

    return loaded_adventure


def get_choice(branch_choices):
    # print choices
    choice_str = "( "
    for choice in branch_choices:
        choice_str = choice_str + choice + ", "
    choice_str = choice_str[:-2] + " )"
    print(choice_str)

    # sanitize choices for easier compare
    sanitized_choices = {k.lower(): v for k, v in branch_choices.items()}

    # get choice and sanitize it
    invalid_choice = True
    while invalid_choice:
        choice = input("What do you do: ").lower().strip()

        if choice in sanitized_choices.keys():  # if the choice is in choices
            next_branch = sanitized_choices[choice]
            invalid_choice = False
        elif choice == "quit":  # if the user wants to quit
            next_branch = False
            invalid_choice = False
        else:  # invalid choice, go again
            print("I don't understand.")

    return next_branch  # return the next branch the user chose


def main():
    # load the adventure file
    adventure = load_adventure_file()

    # set the current branch
    current_branch_key = 'start'  # the 'start" branch is the first branch
    print(adventure[current_branch_key]['text'])  # print the text for the 'start' branch

    # loop until break
    while True:
        if 'choices' in adventure[current_branch_key]:  # if there are branch choices
            current_branch_key = get_choice(adventure[current_branch_key]['choices'])
            if current_branch_key:  # if there is a key for this branch
                print(adventure[current_branch_key]['text'])  # print the text for the current branch
            else:
                break
        else:
            break  # time to quit

    # the end
    input("The End.")


if __name__ == "__main__":
    main()

