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
