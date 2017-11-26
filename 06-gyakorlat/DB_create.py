#!/usr/bin/env python
# -*- coding: utf-8 -*-

import DB_commands
import sys
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create():
    conn = create_connection(sys.argv[1])
    if conn is not None:
        create_table(conn, DB_commands.sql_create_projects_table)
        create_table(conn, DB_commands.sql_create_tasks_table)
        """
        Ellenorzes:
        >sqlite3 [DB file]
        sqlite>.tables
        """
    else:
        print("Error! cannot create the database connection.")