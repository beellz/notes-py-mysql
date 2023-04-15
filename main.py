import mysql.connector
from mysql.connector import Error



# 2, 'Dragon ball Z', 291, '1989-04-26    
# CREATE TABLE anime_list (id int, name varchar(255), episode varchar(255), ReleaseDate varchar(255));

def connect():
    global  connection, cursor
    connection = mysql.connector.connect(host='127.0.0.1', database='Anime',port='13306',user='root', password='notes')
    if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)      


def Create():
    connect()
    sql_create = """INSERT INTO anime_list values (5, 'dragon2' , '203' , 2024-12-19);"""
    cursor.execute(sql_create)
    # sql_select_query = """select * from anime_list where id = 1;"""
    # cursor.execute(sql_select_query)
    # mySql_insert_query = """INSERT INTO anime_list (id, name, episode, ReleaseDate) 
    #                        VALUES 
    #                        (4, 'Inuyasha2', 162, '16-10-2002') """

    # cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Anime table")
    # record = cursor.fetchone()
    # print(record)
    connection.close()
    # print("created")


def showtable():
    connect()
    cursor.execute("SELECT * FROM anime_list")
    rows=cursor.fetchall()
    connection.close()
    return rows


Create()
print(showtable())   
        
        

    
