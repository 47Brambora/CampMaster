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
