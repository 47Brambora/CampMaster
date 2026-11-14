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

    return [f for f in os.listdir(data_dir_path) if f.endswith(".db")]
