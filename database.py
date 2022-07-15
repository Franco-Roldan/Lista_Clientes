import mysql.connector
from esquema import intrucciones
def database():
    db = mysql.connector.connect(
        host = "#######",
        user = "#######",
        password = "#######",
        database = "#######"
    )
    c = db.cursor()

    return db, c

def init_db():
    db, c = database()

    for i in intrucciones:
        c.execute(i)
    
    db.commit()
