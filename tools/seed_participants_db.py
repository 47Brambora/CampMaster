# What I need to put in DB
# 1. participant_id
# 2. first_name
# 3. last_name
# 4. date_of_birth
# 5. team
# 6. age_group
# 7. gender

DATA_DICTIONARY = {
    "FIRST_NAMES_MALE": [
        "Jan",
        "Tomáš",
        "Filip",
        "Honza",
        "Petr",
        "Radek",
        "Bohuslav",
        "Jakub",
        "Ondřej",
        "Martin",
        "Pavel",
        "Lukáš",
        "David",
        "Jiří",
        "Patrik",
        "František",
        "Šimon",
        "Jaroslav",
        "Jára",
        "Václav",
        "Vašek",
        "Přemek",
        "Honza",
        "Aleš",
        "Tobias",
        "Ondra",
        "Vítek",
        "Víťa",
        "Michal",
        "Daniel",
        "Dan",
        "Tom",
        "Marek",
        "Jindra",
        "Mikuláš",
    ],
    "FIRST_NAMES_FEMALE": [
        "Tereza",
        "Jitka",
        "Eliška",
        "Anna",
        "Karolína",
        "Michaela",
        "Naďa",
        "Adéla",
        "Andrea",
        "Barbora",
        "Kateřina",
        "Kristýna",
        "Veronika",
        "Natálie",
        "Klára",
        "Kačka",
        "Toňa",
        "Veronika",
        "Verča",
        "Róza",
        "Bára",
        "Štěpánka",
        "Terezka",
        "Lucka",
        "Aneta",
        "Anetka",
        "Simona",
        "Simča",
        "Natálie",
        "Natálka",
        "Zuzka",
        "Zuzana",
        "Anastázie",
        "Anežka",
    ],
    "LAST_NAMES": [
        "Novák",
        "Mikeš",
        "Myslík",
        "Skála",
        "Bureš",
        "Frajer",
        "Hrnčíř",
        "Polák",
        "Hron",
        "Hervert",
        "Soukup",
        "Klein",
        "Svoboda",
        "Dvořák",
        "Hrdina",
        "Osvald",
        "Tryt",
        "Javůrek",
        "Míka",
        "Reinhard",
        "Bureš",
        "Holeček",
        "Osvalda",
        "Bambousek",
        "Rendl",
        "Holoubek",
        "Hrubá",
        "Novotný",
        "Král",
        "Vrňák",
        "Jelínek",
        "Dufek",
        "Jelínek",
        "Dvořák",
        "Valvoda",
        "Skála",
        "Vacek",
        "Faltejsek",
        "Veltruský",
        "Handlíř",
        "Pešek",
    ],
    "TEAMS": [
        "BLACK",
        "RED",
        "GREEN",
        "YELLOW",
    ],
    "AGE_GROUPS": [
        "A",  # 16+
        "B",  # 13-15
        "C",  # 11-12
        "D",  #  9-10
        "E",  #  7- 8
        "F",  #  5- 6
    ],
}

AGE_GROUPS = [(16, "A"), (13, "B"), (11, "C"), (9, "D"), (7, "E"), (0, "F")]

GENDERS = ("M", "F")
AGE_RANGE = (5, 18)
DEFAULT_COUNT = 42

import datetime
import os
import random
import sqlite3

from campmaster.config import DATA_DIR
from campmaster.utils import current_year, get_available_camps


def age_group_for(age: int) -> str:
    for min_age, group in AGE_GROUPS:
        if age >= min_age:
            return group
    return AGE_GROUPS[-1][1]


def gen_random_participants(
    count: int = DEFAULT_COUNT, seed: int | None = None
) -> list[dict]:
    rng = random.Random(seed)
    base_year = current_year()
    participants = []

    for i in range(count):
        gender = rng.choice(GENDERS)
        names = DATA_DICTIONARY[
            "FIRST_NAMES_MALE" if gender == "M" else "FIRST_NAMES_FEMALE"
        ]

        age = rng.randint(*AGE_RANGE)
        date_of_birth = datetime.date(
            base_year - age, rng.randint(1, 12), rng.randint(1, 28)
        ).isoformat()

        participants.append(
            {
                "first_name": rng.choice(names),
                "last_name": rng.choice(DATA_DICTIONARY["LAST_NAMES"]),
                "date_of_birth": date_of_birth,
                "team": DATA_DICTIONARY["TEAMS"][i % len(DATA_DICTIONARY["TEAMS"])],
                "age_group": age_group_for(age),
                "gender": gender,
            }
        )

    rng.shuffle(participants)
    return participants


def save_participants_to_db(participants: list[dict], db_path: str) -> None:
    db_path = db_path.strip()
    if not db_path:
        db_path = os.path.join(DATA_DIR, f"camp_{current_year()}.db")
    if not db_path.endswith(".db"):
        db_path += ".db"

    sql = """
        INSERT INTO participants (first_name, last_name, date_of_birth, team, age_group, gender)
        VALUES (:first_name, :last_name, :date_of_birth, :team, :age_group, :gender)
    """
    with sqlite3.connect(db_path) as conn:
        conn.executemany(sql, participants)

    print(f"Uloženo {len(participants)} účastníků do {db_path}.")


def ask_positive_int(prompt: str, default: int) -> int:
    while True:
        raw = input(prompt).strip()
        if not raw:
            return default
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Zadejte kladné celé číslo.")


def main() -> None:
    count = ask_positive_int(
        "Kolik účastníků chcete vygenerovat? [42]: ", DEFAULT_COUNT
    )

    print("Dostupné tábory:")
    for camp in get_available_camps(data_dir_path=DATA_DIR):
        print(f"  - {camp}")

    db_path = input("Do které databáze to vložit? (prázdné = camp_ROK.db): ")
    save_participants_to_db(gen_random_participants(count=count), db_path=db_path)


if __name__ == "__main__":
    main()
