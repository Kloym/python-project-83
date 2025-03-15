import psycopg2
from psycopg2.extras import RealDictCursor


def connect_db(DATABASE_URL):
    return psycopg2.connect(DATABASE_URL)

def close(conn):
    conn.close()

def get_all_urls(conn):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            '''
            SELECT
                urls.id,
                urls.name,
                last_checks.created_at,
                last_checks.status_code
            FROM urls
            LEFT JOIN (
                SELECT DISTINCT ON (url_id)
                    url_id,
                    created_at,
                    status_code
                FROM url_checks
                ORDER BY url_id, created_at DESC
            ) AS last_checks
            ON urls.id = last_checks.url_id
            ORDER BY urls.id;
            '''
        )
        urls = cursor.fetchall()
        return urls

def insert_url(conn, url):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            '''
            INSERT INTO urls (name) VALUES (%s) 
            RETURNING id
            '''
        )
        id = cursor.fetchone()['id']
        conn.commit()
        return id
    
def find(conn, url_id):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            '''
            SELECT * FROM urls
            WHERE id = %s
            ''',
            (url_id,),
        )
        url = cursor.fetchone()
        if not url:
            return None
        
        cursor.execute(
            """
            SELECT * FROM url_checks
            WHERE url_id = %s
            """,
            (url_id,),
        )
        url["checks"] = cursor.fetchall()
        return url
    
def check_url(conn, name):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            '''
            SELECT * FROM urls 
            WHERE name = %s
            ''',
            (name,),
        )
        return cursor.fetchone()
        