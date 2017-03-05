import sqlite3
import random
import string
sqlite_file = 'products.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


sqlCREATETABLES = '''
DROP TABLE IF EXISTS items;
CREATE TABLE items (
           itemId number unique primary key,
           itemName text,
           itemPrice number,
           itemSale number,
           itemGender text,
           itemUrl text
);

DROP TABLE IF EXISTS sizes;
CREATE TABLE sizes (
           itemIdSize number,
           itemSize number,
           FOREIGN KEY(itemIdSize) REFERENCES items(itemId)
);

DROP TABLE IF EXISTS tags;
CREATE TABLE tags (
           itemIdTag number,
           itemTag text,
           FOREIGN KEY(itemIdTag) REFERENCES items(itemId)
);


DROP TABLE IF EXISTS users;
CREATE TABLE users (
           username text unique primary key,
           password text
);

'''



def insertItems():
    sqlINSERTTABLES = ''
    for i in range(0,200):
        rndPrice = random.randint(1,100)
        rndSale = random.randint(0,50)
        rndGender = random.randint(0,1)
        if rndGender == 0: rndGender = 'm'
        else: rndGender = 'f'
        name = ''

        for x in range(0,7):
           name += random.choice(string.ascii_letters)

        sqlINSERTTABLES += f'insert into items values ({i},"{name}",{rndPrice},{rndSale},"{rndGender}","unknown");'

def insertSizes():
    sqlINSERTTABLES = ''

    for i in range(0,200):
        sizes = random.randint(0,10)
        sqlINSERTTABLES += f'insert into sizes values ({i},{sizes});'

    return sqlINSERTTABLES

def insertTags():
    sqlINSERTTABLES = ''
    tags =["1920's Gatsby", "1950's", "60's & 70's", "1980's", 'Animals', 'Accessories', 'Book Week Adults', 'Book Week Boys', 'Book Week Girls', 'Bunnies & Maids', 'Burlesque & Showgirl', 'Characters & Fairytale', "Children's", 'Circus', 'Cowboys & Indians', 'Fairies & Pixies', 'Festive', 'Flight', 'Heroes & Villains', 'Horror', 'Icons & Idols', 'International', 'Medieval & Renaissancce', 'Military', 'Novelty', 'Nurse & Fire', 'Occupations & School', 'Oktoberfest', 'Pirates', 'Police ', 'Roman & Greek', 'Sailors', 'Sports', 'Stone Age & Vikings', 'Wigs', "Dan'Sound", 'North Side Party Productions']

    for l in range(0,3):
        for i in range(0,200):
            tag = random.choice(tags)
            sqlINSERTTABLES += f'insert into tags values ({i},"{tag}");\n'

    return sqlINSERTTABLES

#c.executescript(x)
sqlusers = '''
INSERT INTO users VALUES ('admin','giisow');
'''
c.executescript(sqlusers)
conn.commit()