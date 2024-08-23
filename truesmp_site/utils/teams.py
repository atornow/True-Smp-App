import pymysql
from flask import current_app

def get_teams_connection():
    return pymysql.connect(
        host=current_app.config['TEAMS_DB_HOST'],
        user=current_app.config['TEAMS_DB_USER'],
        password=current_app.config['TEAMS_DB_PASSWORD'],
        db=current_app.config['TEAMS_DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_team_name(uuid):
    query = """
    SELECT bt.name AS teamName
    FROM BetterTeams_Players AS bp
    JOIN BetterTeams_Team AS bt ON bp.teamID = bt.teamID
    WHERE bp.playerUUID = %s
    """
    with get_teams_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (uuid,))
            result = cursor.fetchone()
            return result['teamName'] if result else 'No Team'

# Add more Teams-related utility functions as needed