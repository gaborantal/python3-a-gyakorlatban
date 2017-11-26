#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import sqlite3

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("\n")


def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("\n")

def select_task_2(conn):
    cur = conn.cursor()
    cur.execute("SELECT name,status_id  FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("\n")


def select():
    conn = sqlite3.connect(sys.argv[1])
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn,1)

        print("2. Query all tasks (only name and status id")
        select_task_2(conn)

        print("3. Query all tasks")
        select_all_tasks(conn)
