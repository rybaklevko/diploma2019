import sqlite3

conn = sqlite3.connect("mydatabase1.db")
cursor = conn.cursor()




def create_table():
    cursor.execute("""CREATE TABLE albums
                      (title text, artist text, release_date text,
                       publisher text, media_type text)
                   """)

    conn.commit()

def insert_values():
    albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
              ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
              ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
              ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
    conn.commit()

def get_values():
    t = ('RHAT',)
    cursor.execute('SELECT title text FROM albums')

    for row in cursor:
        print(row[0])
    #print(cursor.fetchall())
    conn.commit()


get_values()



