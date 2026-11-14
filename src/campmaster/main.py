from tkinter import Tk  # noqa: I001

from campmaster.ui.views import loading_page
from campmaster.config import DESCRIPTION, LOGO


def main():
    global root
    print(LOGO)
    print(DESCRIPTION)

    root = Tk()
    root.geometry("800x600")

    loading_page(root)

    root.mainloop()


if __name__ == "__main__":
    main()
