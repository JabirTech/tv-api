from flask import Flask, request
import os
import sqlite3

def get_movie_lists():
    connection = sqlite3.connect(os.path.join(os.getcwd(), 'crawler/db.sqlite3'))
    curr = connection.cursor()
    query = "SELECT * from movies"
    res = curr.execute(query)
    res = res.fetchall()
    curr.close()
    connection.commit()

    return res