# CampMaster – An official offline desktop application designed for managing points, disciplines, time measurements, and camp administration at children's summer camps, training camps, and sports events.
# Copyright (C) 2026  47Brambora <47Brambora@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import sqlite3
from functools import partial
from tkinter import *
from tkinter import simpledialog, ttk

from campmaster.config import DATA_DIR, DESCRIPTION, LOGO
from campmaster.database import init_database
from campmaster.ui.dialogs import (
    mesbox_askyesno,
    mesbox_showerror,
    mesbox_showinfo,
    mesbox_showwarning,
)
from campmaster.utils import current_year, get_available_camps

#############
# FUNCTIONS #
#############


# Pop up asking if you want to close the app for SURE!!!
# [I could add more "!", but why yes, or why not?? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]
# ; P
def kill_app(root, event=None):
    reply = mesbox_askyesno(
        tit="CampMaster - EXIT",
        msg="Are you sure you want to close app?\nDid you save all work?",
        ico="question",
    )

    if reply:
        root.destroy()


def update_progress(root, progress_label, step=0):
    max_length = 20

    if step <= max_length:
        filled = "=" * step
        empty = "-" * (max_length - step)
        bar_text = f"||{filled}#>{empty}||"

        if progress_label:
            progress_label.config(text=bar_text)

        root.after(500, partial(update_progress, root, progress_label, step + 1))
    else:
        main_menu(root)


# First page you will see.
def loading_page(root):
    root.title("CampMaster - Loading")

    splash_frame = Frame(root)
    splash_frame.pack(fill=BOTH, expand=True)

    Label(splash_frame, text=LOGO, font=("TkFixedFont", 24), justify=LEFT).pack(
        expand=True
    )
    description_label = Label(
        splash_frame, text=DESCRIPTION, font=("TkFixedFont", 18), justify=CENTER
    )
    description_label.pack(pady=(0, 20), fill=X)

    progress_label = Label(
        splash_frame, text="||>-------------------||", font=("TkFixedFont", 24)
    )
    progress_label.pack(pady=(80, 0))

    def update_wrap(event):
        new_width = event.width - 60
        if new_width > 100:
            description_label.config(wraplength=new_width)

    splash_frame.bind("<Configure>", update_wrap)

    update_progress(root, progress_label, step=0)


def create_new_database(root, data_dir_path: str = DATA_DIR):
    reply = simpledialog.askstring(
        "New database",
        "Enter database name: ",
        initialvalue=f"camp_{current_year()}.db",
    )

    if not reply or not reply.strip():
        mesbox_showwarning(
            msg="Database creation cancelled or name is empty.",
            tit="[Warning] - New database",
        )
        return

    if not reply.endswith(".db"):
        reply += ".db"

    db_path = os.path.join(data_dir_path, reply)

    if os.path.exists(db_path):
        mesbox_showerror(msg=f"Database '{reply}' already exists!")
        return

    init_database(db_path)

    mesbox_showinfo(
        msg=f"Database '{reply}' was successfully created!", tit="[INFO] - New database"
    )

    main_menu(root)


# Open a pop up for camp management and return the chosen action
def open_action_dialog(parent, camp_name: str) -> str | None:
    action = None

    dialog = Toplevel(parent)
    dialog.title(f"Manage Camp: {camp_name}")
    dialog.geometry("320x160")
    dialog.resizable(False, False)
    dialog.transient(parent)
    dialog.grab_set()

    Label(dialog, text=f"Selected camp: {camp_name}\nWhat would you like to do?").pack(
        pady=15
    )

    btn_frame = Frame(dialog)
    btn_frame.pack(pady=10)

    # Helper local fce to save action and close the dialog
    def select_action(act: str):
        nonlocal action
        action = act
        dialog.destroy()

    Button(
        btn_frame, text="Open", width=8, command=partial(select_action, "open")
    ).pack(side=LEFT, padx=5)
    Button(
        btn_frame,
        text="Delete",
        width=8,
        fg="red",
        command=partial(select_action, "delete"),
    ).pack(side=LEFT, padx=5)
    Button(
        btn_frame, text="Cancel", width=8, command=partial(select_action, "cancel")
    ).pack(side=LEFT, padx=5)

    parent.wait_window(dialog)
    return action


def pre_open_camp_database_pop_up_window(
    root, camp: str, data_dir_path: str = DATA_DIR
):
    action = open_action_dialog(root, camp)

    if action == "open":
        print(f"Opening camp workplace for: {camp}")
        open_camp_workplace(root, camp)
    elif action == "delete" and mesbox_askyesno(
        tit="Confirm Deletion",
        msg=f"Are you sure you want to delete database '{camp}'?",
    ):
        db_path = os.path.join(data_dir_path, camp)

        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Deleting database: {camp}")

        main_menu(root)


# TODO:
def add_record(root, camp: str):
    print(f"Adding record to {camp}")


# TODO:
def remove_record(root, camp: str):
    print(f"Removing record from {camp}")


# TODO:
def modify_record(root, camp: str):
    print(f"Modifying record in {camp}")


# TODO:
def refresh_workplace(root, camp: str):
    print(f"Refreshing workplace for {camp}")
    open_camp_workplace(root, camp=camp)


def open_camp_workplace(root, camp: str):
    def top_bar():
        t_bar = Frame(root)
        t_bar.pack(fill=X, padx=10, pady=10)

        Label(t_bar, text=f"Active Camp: {camp}", font=("Arial", 11, "bold")).pack(
            side=LEFT
        )

    def bottom_bar():
        b_bar = Frame(root)
        b_bar.pack(side=BOTTOM, fill=X, padx=20, pady=10)

        Button(b_bar, text="Back to Main Menu", command=partial(main_menu, root)).pack(
            side=RIGHT, padx=5
        )
        Button(
            b_bar,
            text="Refresh",
            command=partial(refresh_workplace, root, camp),
            width=8,
        ).pack(side=LEFT, padx=5)
        Button(
            b_bar, text="Modify", command=partial(modify_record, root, camp), width=8
        ).pack(side=LEFT, padx=5)
        Button(
            b_bar, text="Remove", command=partial(remove_record, root, camp), width=8
        ).pack(side=LEFT, padx=5)
        Button(
            b_bar, text="Add", command=partial(add_record, root, camp), width=8
        ).pack(side=LEFT, padx=5)

    db_path = os.path.join(DATA_DIR, camp)

    # deleting whole main page
    for widget in root.winfo_children():
        widget.destroy()

    root.title(f"CampMaster - Managing: {camp}")

    # -- TOP BAR --
    top_bar()

    # -- BOTTOM BAR --
    bottom_bar()

    # -- TABLE  --

    dat = None

    try:
        dat = sqlite3.connect(db_path)
        cursor = dat.cursor()
        notebook = ttk.Notebook(root)
        notebook.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        )
        tables = [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        mesbox_showerror(
            msg=f"Could not read database tables:\n{e}", tit="Database Error"
        )
        main_menu(root)
        return
    finally:
        if dat is not None:
            dat.close()

    if not tables:
        empty_frame = Frame(notebook)
        notebook.add(empty_frame, text="Empty")
        Label(empty_frame, text="No tables found.").pack(pady=20)
        return

    for table in tables:
        tab_frame = Frame(notebook)
        notebook.add(tab_frame, text=table.capitalize())
        Label(tab_frame, text=f"Data management for: {table}").pack(pady=20)

    dat.close()


def camp_list_on_main_page(root, camp_list: list, data_dir_path: str = DATA_DIR):
    camp_list_frame = Frame(root)
    camp_list_frame.pack(pady=10)

    if not camp_list:
        camp_list_text = Label(
            camp_list_frame,
            text=f"No camp database found in '{data_dir_path}'/. Please create one.",
        )
        create_btn = Button(
            camp_list_frame,
            text="Create new database",
            command=partial(create_new_database, root),
        )
        camp_list_text.pack(pady=5)
        create_btn.pack(pady=5)
    else:
        for camp in camp_list:
            camp_btn = Button(
                camp_list_frame,
                text=camp,
                command=partial(pre_open_camp_database_pop_up_window, root, camp),
                width=25,
            )
            camp_btn.pack(padx=5, pady=2.5)


def main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("CampMaster - Main Menu")

    camps = get_available_camps()
    camp_list_on_main_page(root=root, camp_list=camps)

    bottom_nav_frame = Frame(root)
    bottom_nav_frame.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)

    close_btn = Button(
        bottom_nav_frame,
        text="Close app",
        command=partial(kill_app, root),
        bg="red",
    )
    create_btn = Button(
        bottom_nav_frame,
        text="Create new database",
        command=partial(create_new_database, root),
    )

    close_btn.pack(side=RIGHT, padx=5)
    create_btn.pack(side=RIGHT, padx=5)

    def create_on_enter(event):
        create_new_database(root)

    close_btn.bind("<Return>", partial(kill_app, root))
    create_btn.bind("<Return>", create_on_enter)
