available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }
 
current_choice = None
computer_parts = []  # create an empty list
computer_parts_dict = {} #create an empty dict
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")

        if current_choice in computer_parts_dict:
          print(f"Removing {chosen_part} from dict computer_parts_dict")
          #del computer_parts_dict[current_choice]
          computer_parts_dict.pop(current_choice, None)
        else:
          print(f"Adding {chosen_part} in computer_parts_dict")
          #computer_parts_dict[current_choice] = available_parts[current_choice]
          computer_parts_dict[current_choice] = chosen_part
        print(f"yor dict contains: {computer_parts_dict}")  
    else:
        print("Please add options from the list:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
 
    current_choice = input("> ")
x = {1:100, 2:200, 3:300}
y = {2:200, 1:100, 3:300}
shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print("equal items: {}, {}".format(shared_items, len(shared_items)))
