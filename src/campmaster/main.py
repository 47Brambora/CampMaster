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
