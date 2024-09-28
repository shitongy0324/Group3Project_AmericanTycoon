# Functions about travelling

import mysql.connector
import geopy.distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='project',
    user='dbuser',
    password='123456',
    autocommit=True
    )

def get_coordinate(ident):
    sql = f"select latitude_deg, longitude_deg from airport where ident='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    coordinate = cursor.fetchall()[0]
    return coordinate

def get_distance(coordinate1, coordinate2):
    return geopy.distance.distance(coordinate1, coordinate2)

## Calculate the travelling time: 1 hour per 500 km






