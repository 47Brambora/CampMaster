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


def get_available_camps():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        return []

    return [f for f in os.listdir(DATA_DIR) if f.endswith(".db")]


def main():
    global root
    print(logo)

    root = Tk()
    root.title("CampMaster")
    root.geometry("800x600")

    close_btn = Button(root, text="Close app", command=kill_app)
    close_btn.pack(pady=50)
    close_btn.bind("<Return>", kill_app)

    root.mainloop()


if __name__ == "__main__":
    main()
