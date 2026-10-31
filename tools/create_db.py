import os
import sys

from campmaster.main import DATA_DIR, current_year, init_database

reply = input("Please input name of database")

if not reply:
    reply = f"T_camp_{current_year()}"
if not reply.endswith(".db"):
    reply += ".db"

db_path = os.path.join(DATA_DIR, reply)

if os.path.exists(db_path):
    print(f"[ERROR]: Database {db_path} already exists")
    sys.exit()

init_database(db_path=db_path)

print(f"Test database successfully created at: {db_path}")
