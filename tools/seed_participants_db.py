# What I need to put in DB
# 1. participant_id
# 2. first_name
# 3. last_name
# 4. date_of_birth
# 5. team
# 6. age_group
# 7. gender

DATA_DICTATORY = {
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

import datetime
import random
import sqlite3

from campmaster.main import current_year


def gen_random_participants(count: int = 20) -> list[dict]:
    participants_list = []

    base_year = current_year()

    for i in range(count):
        gender = random.choice(["M", "F"])
        if gender == "M":
            first_name = random.choice(DATA_DICTATORY["FIRST_NAMES_MALE"])
        else:
            first_name = random.choice(DATA_DICTATORY["FIRST_NAMES_FEMALE"])
        last_name = random.choice(DATA_DICTATORY["LAST_NAMES"])

        age = random.randint(5, 18)
        birth_year = base_year - age
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        date_of_birth = datetime.date(birth_year, birth_month, birth_day).strftime(
            "%Y-%m-%d"
        )

        if age >= 16:
            age_group = "A"
        elif age >= 13:
            age_group = "B"
        elif age >= 11:
            age_group = "C"
        elif age >= 9:
            age_group = "D"
        elif age >= 7:
            age_group = "E"
        else:
            age_group = "F"

        team = random.choice(DATA_DICTATORY["TEAMS"])

        participant_data = {
            "participant_id": i + 1,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "team": team,
            "age_group": age_group,
            "gender": gender,
        }
        participants_list.append(participant_data)

    return participants_list


def save_parcipants_to_db(participants_list: list[dict], db_path: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        sql = """
            INSERT INTO participants (first_name, last_name, date_of_birth, team, age_group, gender)
            VALUES (:first_name, :last_name, :date_of_birth, :team, :age_group, :gender)
        """

        # Opraveno: volání bez klíčových slov (sql a seq_of_parameters)
        cursor.executemany(sql, participants_list)
        conn.commit()

    print(f"Úspěšně uloženo {len(participants_list)} účastníků do databáze {db_path}!")


def main():
    save_parcipants_to_db(gen_random_participants(), "data/camp_2026.db")


if __name__ == "__main__":
    main()
