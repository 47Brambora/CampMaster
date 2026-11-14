def cli_askyesno(tit: str, msg: str):
    print(f"{tit}\n{msg}")
    qYn = input("answer by typing [Y/n]: ")
    return qYn.strip().lower() != "n"
