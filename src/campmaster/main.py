from tkinter import *
from tkinter import messagebox

DATA_DIR = "data"
root = None
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


def main():
    global root
    print(logo)

    root = Tk()
    root.title("CampMaster")
    root.geometry("800x600")


    root.mainloop()


if __name__ == "__main__":
    main()
