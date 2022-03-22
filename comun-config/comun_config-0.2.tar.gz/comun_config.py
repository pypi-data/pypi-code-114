import psycopg
from psycopg.rows import namedtuple_row


def get_config_params(connection_string, id_project):

    conn = psycopg.connect(connection_string, row_factory=namedtuple_row)

    cursor = conn.cursor()
    cursor.execute('SELECT key, value FROM params WHERE project_id=%s OR project_id=0', [id_project])
    rows = cursor.fetchall()
    conn.close()

    DB_CONFIG = {}
    for row in rows:
        DB_CONFIG[row[0]] = row[1]

    return DB_CONFIG

