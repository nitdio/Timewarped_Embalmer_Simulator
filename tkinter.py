import tkinter as tk
from tkinter import ttk
import random
import copy
import matplotlib.pyplot as plt

# ----------------------------
# INITIAL DATA
# ----------------------------
minion_list_temp = [
    ["Kill", "Reborn"],
    ["Kill", "Reborn"],
    ["SP", "Reborn", 2],
    ["SP", "Reborn", 2],
    ["SP", "Reborn", 2],
    ["SP", "Reborn", 2],
    ["SP", "Reborn", 2],
]

MAX_MINIONS = 7

# ----------------------------
# TKINTER SETUP
# ----------------------------
root = tk.Tk()
root.title("Timewarped Embalmer Simulator")

num_minions = tk.IntVar(value=MAX_MINIONS )
buttons = []

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# ----------------------------
# BUTTON TEXT
# ----------------------------
def button_text(i):
    m = minion_list_temp[i]
    if m[0] == "Kill":
        return f"{i+1}\nKill\n{m[1]}"
    else:
        return f"{i+1}\nSP\n{m[1]}\nCharge:{m[2]}"


# ----------------------------
# REFRESH UI
# ----------------------------
def refresh_buttons():
    for i, btn in enumerate(buttons):
        btn.config(text=button_text(i))


# ----------------------------
# EDIT WINDOW
# ----------------------------
def edit_minion(index):
    win = tk.Toplevel(root)
    win.title(f"Edit {index+1}")

    type_var = tk.StringVar(value=minion_list_temp[index][0])
    reborn_var = tk.StringVar(value=minion_list_temp[index][1])
    charge_var = tk.IntVar(value=minion_list_temp[index][2] if len(minion_list_temp[index]) == 3 else 0)

    ttk.Label(win, text="Type").grid(row=0, column=0)
    type_box = ttk.Combobox(win, textvariable=type_var, values=["Kill", "SP"], state="readonly")
    type_box.grid(row=0, column=1)

    ttk.Label(win, text="Reborn").grid(row=1, column=0)
    reborn_box = ttk.Combobox(win, textvariable=reborn_var, values=["Reborn", "No Reborn"], state="readonly")
    reborn_box.grid(row=1, column=1)

    ttk.Label(win, text="Charges").grid(row=2, column=0)
    charge_box = ttk.Combobox(win, textvariable=charge_var, values=[0, 1, 2], state="readonly")
    charge_box.grid(row=2, column=1)

    def update_state(event=None):
        if type_var.get() == "Kill":
            charge_box.config(state="disabled")
        else:
            charge_box.config(state="readonly")

    type_box.bind("<<ComboboxSelected>>", update_state)
    update_state()

    def save():
        if type_var.get() == "Kill":
            minion_list_temp[index] = ["Kill", reborn_var.get()]
        else:
            minion_list_temp[index] = ["SP", reborn_var.get(), charge_var.get()]

        refresh_buttons()
        win.destroy()

    ttk.Button(win, text="Save", command=save).grid(row=3, column=0, columnspan=2)


# ----------------------------
# REBUILD BUTTONS
# ----------------------------
def rebuild_buttons(event=None):
    global buttons

    for w in button_frame.winfo_children():
        w.destroy()

    buttons.clear()

    n = num_minions.get()

    while len(minion_list_temp) < n:
        minion_list_temp.append(["SP", "Reborn", 2])

    while len(minion_list_temp) > n:
        minion_list_temp.pop()

    for i in range(n):
        btn = tk.Button(
            button_frame,
            width=14,
            height=4,
            text=button_text(i),
            command=lambda i=i: edit_minion(i)
        )
        btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        buttons.append(btn)

    refresh_buttons()


# ----------------------------
# SIMULATION
# ----------------------------
def run_simulation():
    total_token_dict = {}
    total_kill_dict = {}

    print(minion_list_temp)
    for i in range(10000):
        print(i)

        minion_list = copy.deepcopy(minion_list_temp)

        kill_count = 0
        for j in range(300000):

            if j % 2 == 0:  # attack first
                if minion_list[0][0] == "Kill":
                    kill_count += 1
                if minion_list[0][1] == "Reborn":  # if attacking minion has reborn
                    if all(
                            item == 0
                            for i, sublist in enumerate(minion_list)
                            if i != 0
                            for item in sublist
                            if isinstance(item, (int, float))
                    ):
                        minion_list[0][1] = "No Reborn"
                    else:
                        for k in range(len(minion_list)):
                            if k == 0:  # if checking attacking minion
                                continue

                            if minion_list[k][0] == "SP":  # if the checking minion has give reborn ability
                                if minion_list[k][2] > 0:  # check if the reborn ability can still be use
                                    minion_list[k][2] -= 1  # minus one usage
                                    if minion_list[0][0] == "SP":  # if attacking minion has give reborn ability
                                        minion_list[0][2] = 2  # reset it

                                    break





                else:
                    minion_list.pop(0)

                    if minion_list == []:
                        break
            elif j % 2 == 1:  # attack first
                random_index = random.randrange(0, len(minion_list))
                if minion_list[random_index][0] == "Kill":
                    kill_count += 1
                if minion_list[random_index][1] == "Reborn":  # if attacked minion has reborn
                    if all(
                            item == 0
                            for i, sublist in enumerate(minion_list)
                            if i != k
                            for item in sublist
                            if isinstance(item, (int, float))
                    ):
                        minion_list[random_index][1] = "No Reborn"
                    else:
                        for k in range(len(minion_list)):
                            if k == random_index:  # if checking attacking minion
                                continue

                            if minion_list[k][0] == "SP":  # if the checking minion has give reborn ability

                                if minion_list[k][2] > 0:  # check if the reborn ability can still be use
                                    minion_list[k][2] -= 1  # minus one usage
                                    if minion_list[random_index][
                                        0] == "SP":  # if attacked minion has give reborn ability
                                        minion_list[random_index][2] = 2  # reset it

                                    break  # stop cehcking so reborn check will not change (reborn check = true  will cause it not to reborn)






                else:
                    minion_list.pop(random_index)

                    if minion_list == []:
                        break

            print(minion_list)
        if j + 1 in total_token_dict:
            total_token_dict[j + 1] += 1
        else:
            total_token_dict[j + 1] = 1
        if kill_count in total_kill_dict:
            total_kill_dict[kill_count] += 1
        else:
            total_kill_dict[kill_count] = 1
        print(total_token_dict)
        print(total_kill_dict)

    plt.figure(figsize=(8, 5))
    plt.bar(total_token_dict.keys(), total_token_dict.values())
    plt.title("Total Tokens")
    plt.xlabel("Total tokens")
    plt.ylabel("No_simulations")

    plt.figure(figsize=(8, 5))
    plt.bar(total_kill_dict.keys(), total_kill_dict.values())
    plt.title("Total kills")
    plt.xlabel("Total Kills")
    plt.ylabel("No_simulations")
    #
    plt.show()


# ----------------------------
# TOP UI
# ----------------------------
top = tk.Frame(root)
top.pack()

ttk.Label(top, text="Minions:").pack(side="left")

count_box = ttk.Combobox(
    top,
    textvariable=num_minions,
    values=list(range(1, 8)),
    state="readonly",
    width=3
)
count_box.pack(side="left")

count_box.bind("<<ComboboxSelected>>", rebuild_buttons)

ttk.Button(top, text="RUN SIMULATION", command=run_simulation).pack(side="left", padx=10)

# ----------------------------
# START
# ----------------------------
rebuild_buttons()
root.mainloop()