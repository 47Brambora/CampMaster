import sqlite3


# Initialize database schema
def init_database(db_path: str):
    with sqlite3.connect(db_path) as dat:
        # ! Change from activities to games
        # * Legend for games: \
        # - game_id                   [INTEGER]               => Unique identifier starting from 100
        # - game_type                 [TEXT]                  => Type of that specific game/discipline:
        #   - 'points'  => Evaluated purely by scored points (e.g., target shooting, quiz,...)
        #   - 'time'    => Evaluated by measured time / stopwatch (e.g., running, obstacle course,...)
        # - game_name                 [TEXT]                  => name of the game
        # - scoring_rule               [TEXT]                  => Strategy for calculating points / standings:
        #   - fixed_max_XX                      => Fixed maximum points limit (e.g., max 10 or 20 points regardless of participants)
        #   - child_in_group_count_max_points   => Max points equal to the total count of children participating in the group/category
        #   - descending_by_participants        => Points awarded descending by rank (1st place gets max participants points, last gets 1)
        #   - ascending_by_participants         => Points awarded ascending by rank (inverse scoring or penalty-based ranking)
        # - start_interval_seconds    [INTEGER]   {default 0} => Time gap between individual starts in seconds (default 0 for simultaneous or non-time games)
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_type TEXT NOT NULL,
                game_name TEXT NOT NULL,
                scoring_rule TEXT NOT NULL,
                start_interval_seconds INTEGER DEFAULT 0
            )
        """)
        # Set up to get IDs from 100 and up
        dat.cursor().execute("""
            INSERT OR IGNORE INTO sqlite_sequence (name, seq)
            VALUES ('games', 99)
        """)
        # ! Change from children to participants
        # * Legend for participants \
        # - participant_id    [INTEGER]
        # - first_name        [TEXT]
        # - last_name         [TEXT]
        # - date_of_birth      [DATETIME]
        # - team              [TEXT]
        # - age_group         [TEXT] => Category classification (e.g., categories A through E)
        # - gender            [TEXT]
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS participants (
                participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                date_of_birth DATETIME NOT NULL,
                team TEXT NOT NULL,
                age_group TEXT NOT NULL,
                gender TEXT NOT NULL
            )
        """)
        # * Legend for scores \
        # - score_id                  [INTEGER]
        # - participant_id            [INTEGER]
        # - game_id                   [INTEGER]
        # - status                    [TEXT]      => Current state of participation (e.g., 'OK', 'DNS' - did not start, 'DNF' - did not finish, 'DQ' - disqualified)
        # - start_time_seconds        [INTEGER]
        # - finish_time_seconds       [INTEGER]
        # - points_scored             [INTEGER]
        # - manual_points_override    [INTEGER]
        dat.cursor().execute("""
            CREATE TABLE IF NOT EXISTS scores (
                score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                participant_id INTEGER NOT NULL,
                game_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                start_time_seconds INTEGER NOT NULL,
                finish_time_seconds INTEGER NOT NULL,
                points_scored INTEGER NOT NULL,
                manual_points_override INTEGER NOT NULL,
                FOREIGN KEY(participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
                FOREIGN KEY(game_id) REFERENCES games(game_id) ON DELETE CASCADE
            )
        """)
        dat.commit()
