#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3

def create_project(conn, project):
    sql = """INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    sql = """INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def insert():
    conn = sqlite3.connect(sys.argv[1])
    with conn:
        project_1 = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_2 = ('Cool App with SQLite & Python 2', '2015-01-01', '2015-01-30');
        create_project(conn, project_1)
        project_id = create_project(conn, project_2)
        #print(project_id)

        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
        task_3 = ('Confirm with user about the top requirements 2', 2, 1, project_id, '2015-01-06', '2015-01-10')

        create_task(conn, task_1)
        create_task(conn, task_2)
        create_task(conn, task_3)