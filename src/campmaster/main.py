import datetime
import os
import sqlite3
from tkinter import *
from tkinter import messagebox, simpledialog


##############
#   CONFIG   #
##############

DATA_DIR = "data"
root = None
splash_frame = None
progress_label = None
progress_step = 0
logo = r"""
      ______                                     __       __                        __
     /      \                                   |  \     /  \                      |  \
    |  ######\  ______   ______ ____    ______  | ##\   /  ##  ______    _______  _| ##_     ______    ______
    | ##   \## |      \ |      \    \  /      \ | ###\ /  ### |      \  /       \|   ## \   /      \  /      \
    | ##        \######\| ######\####\|  ######\| ####\  ####  \######\|  ####### \######  |  ######\|  ######\
    | ##   __  /      ##| ## | ## | ##| ##  | ##| ##\## ## ## /      ## \##    \   | ## __ | ##    ##| ##   \##
    | ##__/  \|  #######| ## | ## | ##| ##__/ ##| ## \###| ##|  ####### _\######\  | ##|  \| ########| ##
     \##    ## \##    ##| ## | ## | ##| ##    ##| ##  \# | ## \##    ##|       ##   \##  ## \##     \| ##
      \######   \####### \##  \##  \##| #######  \##      \##  \####### \#######     \####   \####### \##
                                      | ##
                                      | ##
                                       \##
"""
description = "An official offline desktop application designed for managing points, disciplines, time measurements, and camp administration at children's summer camps, training camps, and sports events."


###############
#   LOGICAL   #
###############

# Get current year
def current_year():
    today = datetime.date.today()
    year = today.year
    return year

def get_available_camps():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        return []

    return [f for f in os.listdir(DATA_DIR) if f.endswith(".db")]


##########
#   UI   #
##########

# Pop up asking if you want to close the app for SURE!!!
# [I could add more "!", but why yes, or why not?? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]
# ; P
def kill_app(event=None):
    reply = messagebox.askyesno(
        title="CampMaster - EXIT",
        message="Are you sure you want to close app?\nDid you save all work?",
        icon="question",
        default=messagebox.NO
    )

    if reply:
        root.destroy()

# TODO: Creating new database by fixed standards. You can look in /data/camp_3026.json
def create_new_database():
    reply = simpledialog.askstring("New database", "Enter database name: ", initialvalue=f"camp_{current_year()}.db")

    if not reply or not reply.strip():
        messagebox.showwarning(
            title="[Warning] - New database",
            message="Database creation cancelled or name is empty."
        )
        return

    if not reply.endswith(".db"):
        reply += ".db"

    db_path = os.path.join(DATA_DIR, reply)

    if os.path.exists(db_path):
        messagebox.showerror(
            title="[Error] - New database",
            message=f"Database '{reply}' already exists!"
        )
        return

    with sqlite3.connect(db_path) as dat:
        pass

    messagebox.showinfo(
        title="[Success] - New database",
        message=f"Database '{reply}' was successfully created!"
    )

# bottom navigation bar
def bottom_navigation_bar():
    btn_frame = Frame(root)
    btn_frame.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)

    close_btn = Button(btn_frame, text="Close app", command=kill_app)
    create_btn = Button(btn_frame, text="Create new database", command=create_new_database)

    close_btn.pack(side=RIGHT, padx=5)
    create_btn.pack(side=RIGHT, padx=5)

    close_btn.bind("<Return>", kill_app)
    create_btn.bind("<Return>", create_new_database)

def update_progress():
    global progress_step
    max_length = 20

    if progress_step <= max_length:
        filled = "=" * progress_step
        empty = "-" * (max_length - progress_step)
        bar_text = f"||{filled}#>{empty}||"

        if progress_label:
            progress_label.config(text=bar_text)

        progress_step += 1
        root.after(500, update_progress)
    else:
        main_menu()

# First page you will see.
def loading_page():
    global splash_frame, progress_label

    root.title("CampMaster - Loading")

    splash_frame = Frame(root)
    splash_frame.pack(fill=BOTH, expand=True)

    logo_label = Label(splash_frame, text=logo, font=("TkFixedFont", 24), justify=LEFT)
    description_label = Label(splash_frame, text=description, font=("TkFixedFont", 18), justify=CENTER)

    logo_label.pack(expand=True)
    description_label.pack(pady=(0, 20), fill=X)

    progress_label = Label(splash_frame, text="||>-------------------||", font=("TkFixedFont", 24))
    progress_label.pack(pady=(80, 0))

    def update_wrap(event):
        new_width = event.width - 60
        if new_width > 100:
            description_label.config(wraplength=new_width)

    splash_frame.bind("<Configure>", update_wrap)

    update_progress()

def main_menu():
    splash_frame.destroy()

    root.title("CampMaster - Main Menu")

    camps = get_available_camps()
    if not camps:
        info_text = "No camp database found in 'data/'. Please create one."
    else:
        info_text = f"Found databases: {', '.join(camps)}"

    info_label = Label(root, text=info_text, font=("Arial", 32))
    info_label.pack(pady=100)

    bottom_navigation_bar()


############
#   MAIN   #
############

def main():
    global root
    print(logo)
    print(description)

    root = Tk()
    root.geometry("800x600")

    loading_page()

    root.mainloop()


if __name__ == "__main__":
    main()
