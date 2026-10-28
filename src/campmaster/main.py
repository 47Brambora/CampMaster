import os
from tkinter import *
from tkinter import messagebox


##############
#   CONFIG   #
##############

DATA_DIR = "data"
root = None
splash_frame = None
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


###############
#   LOGICAL   #
###############

# Pop up asking if you want to close the app for SURE!!!
# [I could do more "!", but why yes, or why not?? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]
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

def create_new_database():
    pass

def get_available_camps():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        return []

    return [f for f in os.listdir(DATA_DIR) if f.endswith(".db")]


##########
#   UI   #
##########

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

# First page you will see.
def loading_page():
    global splash_frame

    root.title("CampMaster - Loading")

    splash_frame = Frame(root)
    splash_frame.pack(fill=BOTH, expand=True)

    logo_label = Label(splash_frame, text=logo, font=("TkFixedFont", 16), justify=LEFT)
    logo_label.pack(expand=True)

    # time in ms 10000ms = 10s
    root.after(10000, main_menu)

def main_menu():
    global splash_frame

    splash_frame.destroy()

    root.title("CampMaster - Main Menu")

    camps = get_available_camps()
    if not camps:
        info_text = "No camp database found in 'data/'. Please create one."
    else:
        info_text = f"Found databases: {', .'.join(camps)}"

    info_label = Label(root, text=info_text, font=("Arial", 24))
    info_label.pack(pady=100)

    bottom_navigation_bar()


############
#   MAIN   #
############

def main():
    global root
    print(logo)

    root = Tk()
    root.geometry("800x600")

    loading_page()

    root.mainloop()


if __name__ == "__main__":
    main()
