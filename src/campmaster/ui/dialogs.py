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


from tkinter import messagebox


def mesbox_askyesno(tit: str, msg: str, ico: str = "question", defa: bool = False):
    if defa:
        defa = messagebox.YES
    else:
        defa = messagebox.NO

    return messagebox.askyesno(title=tit, message=msg, icon=ico, default=defa)


def cli_askyesno(tit: str, msg: str):
    print(f"{tit}\n{msg}")
    qYn = input("answer by typing [Y/n]: ")
    return qYn.strip().lower() != "n"


def mesbox_showwarning(msg: str, tit: str = "[Warning]"):
    return messagebox.showwarning(title=tit, message=msg)


def mesbox_showerror(msg: str, tit: str = "[Error]"):
    return messagebox.showerror(title=tit, message=msg)


def mesbox_showinfo(msg: str, tit: str = "[INFO]"):
    return messagebox.showinfo(title=tit, message=msg)
