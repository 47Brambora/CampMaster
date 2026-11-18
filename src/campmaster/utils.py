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


import datetime
import os

from campmaster.config import DATA_DIR


# Ensure the data directory exists, create it if missing
def check_for_DATA_DIR(data_dir_path: str = DATA_DIR) -> None:
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)


# Get current year
def current_year():
    return datetime.datetime.now().astimezone().year


# Scan the data directory for existing camp database files (.db)
def get_available_camps(data_dir_path: str = DATA_DIR) -> list[str]:
    check_for_DATA_DIR(data_dir_path=data_dir_path)

    return [
        f for f in os.listdir(data_dir_path) if f.endswith((".db", ".json"))
    ]
