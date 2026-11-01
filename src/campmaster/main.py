import datetime
import os
import sqlite3
from functools import partial
from tkinter import *
from tkinter import messagebox, simpledialog

##############
#   CONFIG   #
##############

DATA_DIR = "data"
root = None
splash_frame = None
camp_list_Frame = None
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

# Ensure the data directory exists, create it if missing
def check_for_DATA_DIR() -> None:
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

# Get current year
def current_year():
    return datetime.date.today().year

# Scan the data directory for existing camp database files (.db)
def get_available_camps() -> list[str]:
    check_for_DATA_DIR()

    return [f for f in os.listdir(DATA_DIR) if f.endswith(".db")]

# Initialize database schema
def init_database(db_path:str):
    with sqlite3.connect(db_path) as dat:
        # ! Change from activities to games
        #* Legend for games: \
            # game_id                   [INTEGER]               => Unique identifier starting from 100
            # game_type                 [TEXT]                  => Type of that specific game/discipline:
                # 'points'  => Evaluated purely by scored points (e.g., target shooting, quiz,...)
                # 'time'    => Evaluated by measured time / stopwatch (e.g., running, obstacle course,...)
            # game_name                 [TEXT]                  => name of the game
            #scoring_rule               [TEXT]                  => Strategy for calculating points / standings:
                # fixed_max_XX                      => Fixed maximum points limit (e.g., max 10 or 20 points regardless of participants)
                # child_in_group_count_max_points   => Max points equal to the total count of children participating in the group/category
                # descending_by_participants        => Points awarded descending by rank (1st place gets max participants points, last gets 1)
                # ascending_by_participants         => Points awarded ascending by rank (inverse scoring or penalty-based ranking)
            # start_interval_seconds    [INTEGER]   {default 0} => Time gap between individual starts in seconds (default 0 for simultaneous or non-time games)
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_type TEXT NOT NULL,
                game_name TEXT NOT NULL,
                scoring_rule TEXT NOT NULL,
                start_interval_seconds INTEGER DEFAULT 0
            )
        """)
        # Set up to get IDs from 100 and up
        dat.cursor().execute("""
            INSERT OR IGNORE INTO sqlite_sequence (name, seq)
            VALUES ('games', 99)
        """)
        # ! Change from children to participants
        #* Legend for participants \
            # participant_id    [INTEGER]
            # first_name        [TEXT]
            # last_name         [TEXT]
            # date_of_birth      [DATETIME]
            # team              [TEXT]
            # age_group         [TEXT] => Category classification (e.g., categories A through E)
            # gender            [TEXT]
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS participants (
                participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                date_of_birth DATETIME NOT NULL,
                team TEXT NOT NULL,
                age_group TEXT NOT NULL,
                gender TEXT NOT NULL
            )
        """)
        #* Legend for scores \
            # score_id                  [INTEGER]
            # participant_id            [INTEGER]
            # game_id                   [INTEGER]
            # status                    [TEXT]      => Current state of participation (e.g., 'OK', 'DNS' - did not start, 'DNF' - did not finish, 'DQ' - disqualified)
            # start_time_seconds        [INTEGER]
            # finish_time_seconds       [INTEGER]
            # points_scored             [INTEGER]
            # manual_points_override    [INTEGER]
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS scores (
                score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                participant_id INTEGER NOT NULL,
                game_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                start_time_seconds INTEGER NOT NULL,
                finish_time_seconds INTEGER NOT NULL,
                points_scored INTEGER NOT NULL,
                manual_points_override INTEGER NOT NULL,
                FOREIGN KEY(participant_id) REFERENCES participants(id) ON DELETE CASCADE,
                FOREIGN KEY(game_id) REFERENCES games(game_id) ON DELETE CASCADE
            )
        """)
        dat.commit()


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

# Open a pop up for camp management and return the chosen action
def open_action_dialog(parent, camp_name:str) -> str | None:
    action = None

    dialog = Toplevel(parent)
    dialog.title(f"Manage Camp: {camp_name}")
    dialog.geometry("320x160")
    dialog.resizable(False, False)

    dialog.transient(parent)
    dialog.grab_set()

    Label(dialog, text=f"Selected camp: {camp_name}\nWhat would you like to do?").pack(pady=15)

    btn_frame = Frame(dialog)
    btn_frame.pack(pady=10)

    # Helper local fce to save action and close the dialog
    def select_action(act:str):
        nonlocal action
        action = act
        dialog.destroy()

    Button(btn_frame, text="Open", width=8, command=partial(select_action, "open")).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Delete", width=8, fg="red", command=partial(select_action, "delete")).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Cancel", width=8, command=partial(select_action, "cancel")).pack(side=LEFT, padx=5)

    parent.wait_window(dialog)
    return action

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

    init_database(db_path)

    messagebox.showinfo(
        title="[Success] - New database",
        message=f"Database '{reply}' was successfully created!"
    )

def pre_open_camp_database_pop_up_window(camp:str):
    action = open_action_dialog(root, camp)

    if action == "open":
        print(f"Opening camp: {camp}")
        # TODO: Add modify logic here
    elif action == "delete" and messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete database '{camp}'?", icon="question", default=messagebox.NO):
        print(f"Deleting database: {camp}")
        # TODO: Add delete file logic here

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

def camp_list_on_main_page(camp_list:list):
    global camp_list_Frame

    if camp_list_Frame is not None:
        camp_list_Frame.destroy()

    camp_list_Frame = Frame(root)
    camp_list_Frame.pack(pady=10)

    if not camp_list:
        camp_list_text = Label(camp_list_Frame, text=f"No camp database found in '{DATA_DIR}'/. Please create one.")
        create_btn = Button(camp_list_Frame, text="Create new database", command=create_new_database)
        camp_list_text.pack(pady=5)
        create_btn.pack(pady=5)
    else:
        for camp in camp_list:
            camp_btn = Button(camp_list_Frame, text=camp, command=partial(pre_open_camp_database_pop_up_window, camp), width=25)
            camp_btn.pack(padx=5, pady=2.5)

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
    camp_list_on_main_page(camp_list=camps)

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
