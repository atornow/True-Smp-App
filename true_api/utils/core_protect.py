import pymysql
from flask import current_app

def get_core_protect_connection():
    return pymysql.connect(
        host=current_app.config['COREPROTECT_DB_HOST'],
        user=current_app.config['COREPROTECT_DB_USER'],
        password=current_app.config['COREPROTECT_DB_PASSWORD'],
        db=current_app.config['COREPROTECT_DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_unique_users():
    with get_core_protect_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT user FROM co_user")
            return [row['user'] for row in cursor.fetchall()]

def fetch_user_stats(username, stat_type, action, lookback):
    query = """
    SELECT
        TYPE,
        SUM(CASE WHEN co_block.time >= UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL %s SECOND)) AND action = %s THEN 1 ELSE 0 END) AS type_count
    FROM
        co_block
    JOIN
        co_user ON co_block.user = co_user.rowid
    WHERE
        co_user.user = %s
    GROUP BY
        TYPE
    ORDER BY
        TYPE
    """
    with get_core_protect_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (lookback, action, username))
            return {row['TYPE']: row['type_count'] for row in cursor.fetchall()}

# Add more CoreProtect-related utility functions as needed