# CampMaster

An official offline desktop application designed for managing points, disciplines, time measurements, and camp administration at children's summer camps, training camps, and sports events.

The application is built entirely in **Python** and runs locally as a standalone executable (`.exe`), eliminating the need to install Python, web servers, or third-party tools. It uses a robust local database for secure data storage while offering seamless export options to formatted Excel files (`.xlsx`).

## Key Features

- **Local Database & Secure Storage:**
  - Structured local storage (SQLite-based) for participants, categories, points, and sensitive data (such as health records and contracts).
  - Designed with data privacy and offline reliability in mind.
- **Participant Management:**
  - Clear overview and management of participants divided into categories **A** through **E**.
- **Point Disciplines:**
  - Quick entry and back-editing of points with instant feedback.
- **Time Disciplines with Interval Starts:**
  - **Live Calculation:** Setup of start times and fixed intervals (e.g., 1 minute). Net time is calculated immediately upon finishing.
  - **Manual Start Override:** Ability to modify the start time for specific participants.
  - **Delay Checkbox:** Option whether a manual shift propagates to subsequent starts or stays isolated.
- **Formatted Excel Exports (`.xlsx`):**
  - Export current results and standings into a styled Excel file complete with colors and custom formatting, perfect for printing, archiving, or sharing with camp leaders.
- **100% Offline Standalone App:**
  - Runs locally as a standalone executable compiled via PyInstaller—no internet connection, Wi-Fi, or pre-installed Python required for end-users.
  
## Getting Started (Development & Source)

During the current development phase, you can run the application directly from source using [uv](https://github.com/astral-sh/uv) for ultra-fast dependency management and execution:

1. **Clone or download the repository:**

```bash
git clone git@github.com:47Brambora/CampMaster.git
cd CampMaster
```

2. **Run the application directly using `uv`:**

```bash
uv run mastercamp
```

`uv` will automatically handle the virtual environment, sync required dependencies and launch the application.

## Architecture & Technology

- **Core & Logic:** Pure Python
- **Database:** Local structured database (SQLite) for application data and records
- **Reporting / Export:** Excel generation with custom styling and colors (`openpyxl` / pandas)
- **Distribution:** Standalone `.exe` package via PyInstaller (zero-dependency local execution)
