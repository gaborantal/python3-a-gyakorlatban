import sys
import sqlite3


def delete_task(conn, id):
    sql = """DELETE FROM tasks WHERE id=?"""
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_all_tasks(conn):
    sql = """DELETE FROM tasks"""
    cur = conn.cursor()
    cur.execute(sql)

def delete():
    conn = sqlite3.connect(sys.argv[1])
    with conn:
        delete_task(conn, 2)
        #delete_all_tasks(conn)