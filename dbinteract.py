import mysql.connector
import random

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='project',
    user='dbuser',
    password='123456',
    autocommit=True
    )

def get_random_airport():
    sql = 'select ident from airport;'
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    random_airport = random.choice(response)[0]
    return random_airport

def register_new_player(player_name):
    initial_airport = get_random_airport()
    sql = f'insert into game values (default, "{player_name}", default, "{initial_airport}", default);'
    cursor = connection.cursor()
    cursor.execute(sql)

def get_existing_names():
    sql = 'select player_name from game;'
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()

    existing_names = []
    for item in response:
        existing_names.append(item[0])

    return existing_names

def get_coordinate(ident):
    sql = f"select latitude_deg, longitude_deg from airport where ident='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    coordinate = cursor.fetchall()[0]
    return coordinate
