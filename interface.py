import sqlite3

def connect():
    conn = sqlite3.connect('products.db')
    return conn


def retrieveData(db,price,categories):
    curr = db.cursor()
    gStr = ''
    sStr = ''

    tagList = []
    for x in range(0,len(categories[0][0])):
        if categories[0][0][x]:
            tagList.append(categories[1][0][x])


    sql = f'SELECT itemIdTag FROM tags WHERE itemTag = ?'

    idArray =[]
    itemsArray = []
    for tag in tagList:
        curr.execute(sql,[tag])
        result = curr.fetchall()

        for id in result:
            idArray.append(id[0])

    if (categories[0][2][0] ==1) and (categories[0][2][1] !=1):
        print('male')
        gStr = 'AND itemGender = "m"'
    if (categories[0][2][0] !=1) and (categories[0][2][1] ==1):
        print('female')
        gStr = 'AND itemGender = "f"'

    if (categories[0][2][0] ==1) and (categories[0][2][1] ==1):
        print('both m/f')
        gStr = 'AND (itemGender = "f" OR itemGender = "m")'


    '''
    if sale != 0:
        sStr = 'order by itemSale'
    '''

    for id in idArray:
        sql = f'SELECT itemName, itemPrice, itemSale, itemUrl, itemGender FROM items WHERE itemId = ? {gStr} LIMIT 27'

        curr.execute(sql,[id])
        result = curr.fetchall()
        for value in result:
            itemsArray.append(value)


    if len(idArray) < 1:

        if gStr == 'AND itemGender = "m"':

            sql = f'SELECT itemName, itemPrice, itemSale, itemUrl, itemGender FROM items WHERE itemGender = "m" LIMIT 27'
            curr.execute(sql)
            result = curr.fetchall()
            for value in result:
                itemsArray.append(value)
        if gStr == 'AND itemGender = "f"':
            sql = f'SELECT itemName, itemPrice, itemSale, itemUrl, itemGender FROM items WHERE itemGender = "f" LIMIT 27'
            curr.execute(sql)
            result = curr.fetchall()
            for value in result:
                itemsArray.append(value)

        if gStr == 'AND (itemGender = "f" OR itemGender = "m")':
            sql = f'SELECT itemName, itemPrice, itemSale, itemUrl, itemGender FROM items WHERE itemGender = "m" OR itemGender = "f" LIMIT 27'
            curr.execute(sql)
            result = curr.fetchall()
            for value in result:
                itemsArray.append(value)


    return itemsArray





def checkPass(db,username,password):
    curr = db.cursor()
    sql = 'SELECT * FROM users WHERE username = ? AND password = ?'

    curr.execute(sql,[username,password])


    result = curr.fetchall()
    for res in result:

        return True

    return False



def addItem(db,id, name,tags,price,sale,sizes,gender):
    curr = db.cursor()
    #id , name, price, sale, gender, url

    if int(id) == -1:
        genderStr = ''
        if len(gender) > 0:
            if 'Male' and 'Female' in gender:
                genderStr = ''
            elif 'Male' in gender:
                genderStr = 'm'
            else:
                genderStr = 'f'
        sql = 'SELECT count(*) FROM items'
        curr.execute(sql)
        result = curr.fetchall()
        for r in result:
            print(r)
            id = r[0] + 1

        print(id)
        sql1 = 'INSERT INTO items (itemId, itemName, itemPrice, itemSale, itemGender) VALUES (?, ?, ?, ?, ?);'
        sql2 = 'INSERT INTO sizes VALUES (?, ?);'
        sql3 = 'INSERT INTO tags VALUES (?, ?);'

        curr.execute(sql1,[id,name, price, sale, genderStr])
        for size in sizes:
            sizeNum = int(size)
            curr.execute(sql2,[id,sizeNum])
        for tag in tags:
            curr.execute(sql3,[id,tag])



    else:
        print(id, name,tags,price,sale,sizes,gender)
        if name != 'UNKNOWN':
            sql = f'UPDATE items SET itemName="{name}" WHERE itemId = {id}'
            curr.execute(sql)
        if price != 'UNKNOWN':
            sql = f'UPDATE items SET itemPrice="{price}" WHERE itemId = {id}'
            curr.execute(sql)
        if sale != 'UNKNOWN':
            sql = f'UPDATE items SET itemSale="{sale}" WHERE itemId = {id}'
            curr.execute(sql)


        if 'Female' in gender and 'Male' not in gender:
            sqlG = f'UPDATE items SET itemGender="f" WHERE itemId = {id}'

        if 'Male' in gender and 'Female' not in gender:
            sqlG = f'UPDATE items SET itemGender="m" WHERE itemId = {id}'

        if 'Female' in gender and 'Male' in gender:
            sqlG = f'UPDATE items SET itemGender="" WHERE itemId = {id}'

        curr.execute(sqlG)

        sql = f'DELETE FROM tags WHERE itemIdTag = {id}'
        curr.execute(sql)
        sql = f'DELETE FROM sizes WHERE itemIdSize = {id}'
        curr.execute(sql)

        sql2 = 'INSERT INTO sizes VALUES (?, ?);'
        sql3 = 'INSERT INTO tags VALUES (?, ?);'
        for size in sizes:
            sizeNum = int(size)
            curr.execute(sql2,[id,sizeNum])
        for tag in tags:
            curr.execute(sql3,[id,tag])





    db.commit()
def addFileName(db,name,id):
    print('addFileName', name, type(id))
    curr = db.cursor()
    if int(id) == -1:
        sql = 'SELECT count(*) FROM items'
        curr.execute(sql)
        result = curr.fetchall()
        print('res',result)
        for r in result:
            print(r)
            id = r[0]

    sql = f'UPDATE items SET itemUrl="{name}" WHERE itemId = {id}'
    print(sql)
    curr.execute(sql)
    db.commit()



def getItems(db):
    #return id, name price sale gender sizes tags img
    #   example = [[199, 'vudlCzX', 59, 33, 'f', 'unknown.png', 3, 5, 'Fairies & Pixies', 'Occupations & School', 'Book Week Girls']]
    listOfItems = []


    curr = db.cursor()
    sql = 'SELECT * FROM items ORDER BY itemId DESC'
    curr.execute(sql)
    result = curr.fetchall()
    for res in result:
        r = list(res)
        listOfItems.append(r)


    sql = 'SELECT * FROM sizes'
    curr.execute(sql)
    result = curr.fetchall()
    for res in result:

        for item in listOfItems:
            if res[0] == item[0]:
                item.append(res[1])

    sql = 'SELECT * FROM tags'
    curr.execute(sql)
    result = curr.fetchall()
    for res in result:

        for item in listOfItems:
            if res[0] == item[0]:
                item.append(res[1])
    return listOfItems


