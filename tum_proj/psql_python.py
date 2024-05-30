import psycopg2

from tum_proj.config import host, user, password, db_name

def select_pr_by_teacher_id(id):
    bool = False
    connection = None
    results = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"SELECT link as link_pr, comment FROM pages_schema.pull_requests p JOIN pages_schema.student_pr s ON s.pr_id = p.id JOIN pages_schema.student_teacher st ON st.student_id = s.student_id WHERE teacher_id = {id};"
            )
        
        results = cursor.fetchall()
        
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")


    return results



def create_pull_request(link, comment):
    bool = False
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"INSERT INTO pages_schema.pull_requests (link, comment) VALUES ('{link}', '{comment}');"
            )
        
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")


    return bool


def create_teacher(login, passw):
    bool = False
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"INSERT INTO pages_schema.teacher (login, password) VALUES ('{login}', '{passw}');"
            )
        
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")


    return bool


def create_student(login, passw):
    bool = False
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"INSERT INTO pages_schema.students (login, password) VALUES ('{login}', '{passw}');"
            )
        
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")


    return bool

def send_to_db_html_content(id, content):
    bool = False
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"INSERT INTO pages_schema.pages (id,content) VALUES ('{id}', '{content}');"
            )
        
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")


    return bool