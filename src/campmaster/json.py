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

import json


def init_json_database(json_path: str):
    json_to_init = {
        "games": [
            {
                "game_id": 100,
                "game_type": None,
                "game_name": None,
                "scoring_rule": None,
                "start_interval_seconds": 0,
            }
        ],
        "participants": [
            {
                "participant_id": 1,
                "first_name": None,
                "last_name": None,
                "date_of_birth": None,
                "team": None,
                "age_group": None,
                "gender": None,
            }
        ],
        "scores": [
            {
                "score_id": 1,
                "participant_id": 1,
                "game_id": 100,
                "status": None,
                "start_time_seconds": None,
                "finish_time_seconds": None,
                "points_scored": 0,
                "manual_points_override": None,
            }
        ],
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_to_init, f, indent=2, ensure_ascii=False)
