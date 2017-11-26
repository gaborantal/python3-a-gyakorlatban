#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import sqlite3

def update_task(conn, task):
    sql = """UPDATE tasks SET priority = ? , begin_date = ? , end_date = ? WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, task)

def update_project(conn, project):
    sql = """UPDATE projects SET name = ? WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, project)


def update():
    conn = sqlite3.connect(sys.argv[1])
    with conn:
        update_task(conn, (2, '2015-01-04', '2015-01-06',2))
        update_project(conn, ("Best Python", 2))