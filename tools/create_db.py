import os
import sys

from campmaster.main import DATA_DIR, check_for_DATA_DIR, current_year, init_database


def main():
    reply = input("Please input name of database: ")

    if not reply:
        reply = f"T_camp_{current_year()}.db"

    if not reply.endswith(".db"):
        reply += ".db"

    db_path = os.path.join(DATA_DIR, reply)

    if os.path.exists(db_path):
        print(f"[ERROR]: Database '{reply}' already exists!")
        sys.exit()

    check_for_DATA_DIR(data_dir_path=DATA_DIR)

    init_database(db_path=db_path)
    print(f"Database successfully created at: {db_path}")


if __name__ == "__main__":
    main()
