import mysql.connector

cnx = mysql.connector.connect(user="root",
                              password="happy@456",
                              host="localhost",
                              database="test")



insert_cursor = cnx.cursor(prepared=True)
select_cursor = cnx.cursor(buffered=True)


# insert_tuple =  tuple("Robert"); DROP TABLE profiles;-- ")
# password = "ηελλο νες"
# date = "2021-04-22"

insert_query = """-- sql
INSERT INTO profiles (profile_name, profile_picture_irl, join_date, last_active)
VALUES (%s, %s, DATE(%s), DATE(%s));"""

insert_tuple = ("Bobby", "/link/to/bobby", "2017-03-15", "2018-04-05")

# insert_cursor.execute(insert_query, insert_tuple, multi=True)
select_cursor.execute("SELECT * FROM profiles;")
if select_cursor.rowcount > 0:
    print("hello")
else:
    print("world")

for t in select_cursor:
    print(t)

cnx.commit()
select_cursor.close()
insert_cursor.close()
cnx.close()
