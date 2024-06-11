from datetime import datetime
import psycopg2
import numpy as np
import re
from tum_proj.config import host, user, password, db_name
from tum_proj.test_data import PullRequestModel

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
                f"SELECT DISTINCT st.login, pr.link, pr.lab_num FROM  pages_schema.student_pr as st_pr, pages_schema.pull_requests as pr, pages_schema.student_teacher as st_tch, pages_schema.students as st WHERE st_pr.pr_id = pr.id AND st.id = st_tch.student_id AND st_tch.teacher_id = {id}"
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
    pd = []
    for a in results:
        sn = a[0].replace(' ', '')
        l = re.sub('\s+', '', a[1])
        pd.append(PullRequestModel(labNumber=a[2], studentName=sn, date=datetime(2024, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink=l))
    # pd = list(map(lambda a: PullRequestModel(labNumber=1, studentName=a[0], date=datetime(2024, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink=a[1]), np.unique(results)))
    return pd



def create_pull_request(link, comment, student_id, lr_num):
    bool = False
    pr_id = None
    _ = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
                f"INSERT INTO pages_schema.pull_requests (link, comment, lab_num) VALUES ('{link}', '{comment}', '{lr_num}');", 
            )
        cursor.execute('SELECT LASTVAL()')
        pr_id = cursor.fetchone()[0]
        cursor.execute(
            f"INSERT INTO pages_schema.student_pr (student_id, pr_id) VALUES ('{student_id}', '{pr_id}');", 
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
    connection = None
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


def create_student(login, passw, teacher):
    bool = False
    connection = None
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
        cursor.execute('SELECT LASTVAL()')
        student_id = cursor.fetchone()[0]
        cursor.execute(
            f"SELECT id FROM pages_schema.teacher WHERE login = '{teacher}';"
        )
        teacher_id = cursor.fetchone()[0]
        cursor.execute(
            f"INSERT INTO pages_schema.student_teacher (student_id, teacher_id) VALUES ('{student_id}', '{teacher_id}');"
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


def check_student(login, passw):
    bool = False
    # connection = None
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
                f"SELECT id, login, password FROM pages_schema.students WHERE login = '{login}' and password = '{passw}';"
            )
        
        results = cursor.fetchall()
        print(results)
    
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            bool = True
            connection.commit()
            connection.close()
            print("[INFO] POSTGRE CLOSED")
    return results


def check_teacher(login, passw):
    bool = False
    # connection = None
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
                f"SELECT id, login, password FROM pages_schema.teacher WHERE login = '{login}' and password = '{passw}';"
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