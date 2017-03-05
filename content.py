import pprint


def sideBarMenu():


    searchBar = getCategories()
    htmlArray = []
    checkedArray = [[],[],[],[]]
    flattenedArray = [[],[],[],[]]

    categoryCount = 0
    saleCount = 0
    genderCount = 0

    for item in searchBar.values():
        html = ''

        for x in item:

            if x[0] == 0:
                padding = ''
                html += f'<li class = "categories" id = "cat-{x[1]}" {padding}><a>{x[1]}</a></li>'
            if x[0] == 1:
                padding = 'style = "padding-left:15px"'
                html += f'<li class = "categories" id = "cat-{x[1]}" {padding}><a>{x[1]}</a></li>'

            if x[0] == 2:
                padding = 'style = "padding-left:30px"'


                #1 = category
                if x[2] == 0:
                    html += f'<li class = "categories" id = "cat-{x[1]}" {padding}><a><input type="checkbox" name="check-{x[1]}" onclick="checkedFn({x[2]}, {categoryCount})">{x[1]}</a></li>'
                    categoryCount += 1
                    checkedArray[0].append(0)
                    flattenedArray[0].append(x[1])
                #2 == sale
                if x[2] == 1:
                    html += f'<li class = "categories" id = "cat-{x[1]}" {padding}><a><input type="checkbox" name="check-{x[1]}" onclick="checkedFn({x[2]}, {saleCount})">{x[1]}</a></li>'
                    saleCount += 1
                    checkedArray[1].append(0)
                    flattenedArray[1].append(x[1])
                #3 = gender
                if x[2] == 2:
                    html += f'<li class = "categories" id = "cat-{x[1]}" {padding}><a><input type="checkbox" name="check-{x[1]}" onclick="checkedFn({x[2]}, {genderCount})">{x[1]}</a></li>'
                    genderCount += 1
                    checkedArray[2].append(0)
                    flattenedArray[2].append(x[1])

            if x[0] == -1:
                checkedArray[3].append(0)
                flattenedArray[3].append(x[1])


                html += '<li class = "categories" id = "cat-Price" style = "padding-left:15px"><a> line goes here  </a></li>'


        htmlArray.append(html)

    idArray = []
    stateArray = []
    for ids in searchBar.keys():
        idArray.append('cat-'+ids)
        stateArray.append('closed')

    return [htmlArray,idArray,stateArray,checkedArray,flattenedArray]

#sideBarMenu()

def rangeMainContent(array):

    html = '<div class = "mainWrapper">'
    count = 0
    for item in array:
        if count < 27:
            itemName = item[0]
            itemPrice = item[1]
            itemSale = item[2]
            url = 'images/costumes/' + item[3]
            '''
            if item[3] == 'unknown':
                url = 'images/costumes/' + item[3] + '.png'
            else:
                url = 'images/costumes/' + item[3]
            '''

            html += f'<div class = "mainItem">\
                                    <img src = "{url}">\
                                    <div class = "mainItem name">\
                                        {itemName}\
                                    </div>\
                                    <div class = "mainItem price">\
                                        ${itemPrice}\
                                    </div>\
                                </div>'
            count += 1

    html += '</div>'
    return html


def getDropdowns():
    unsortedTags = getCategories()
    tags = []
    genders = getGenders()
    sizes = getSizes()
    for item in unsortedTags.values():
        for x in item:
            if len(x) > 2:
                if x[2] == 0:
                    tags.append(x[1])

    genderHtml = ''
    for i in range(0,len(genders)):
        genderHtml += f'<a>{genders[i]} <input type="checkbox" onclick="checkFn(0,{i})"></a>'


    tagsHtml = ''
    for i in range(0,len(tags)):
        tagsHtml += f'<a>{tags[i]} <input type="checkbox" onclick="checkFn(1,{i})"></a>'



    sizeHtml = ''
    for i in range(0,len(sizes)):
        sizeHtml += f'<a>{sizes[i]} <input type="checkbox" onclick="checkFn(2,{i})"></a>'


    checkedArray = [[],[],[]]
    combinedArray = [genders,tags,sizes]
    for x in range(0,len(combinedArray)):
        for z in combinedArray[x]:
            checkedArray[x].append(0)


    return (genderHtml,tagsHtml,sizeHtml,checkedArray)


def getCategories():
    searchBar = {
        'Categories':[[0,'Categories'],[1,'Decade'],[1,'Film'],[1,'Holiday']],
        #name, [[position (0 = 0px) (-1 = special) , htmlName, subject (category/sale/gender)
        'Price':[[0,'Price'],[-1,'priceLine',3]],


        'Decade':[[0,'Categories'],[1,'Decade'],[2,'1920s',0],[2,'1930s',0],[2,'1940s',0],[2,'1950s',0],[2,'1960s',0],[1,'Film'],[1,'Holiday']],
        'Film':[[0,'Categories'],[1,'Decade'],[1,'Film'],[2,'Animals',0],[2,'Accessories',0],[2,'Film3',0],[2,'Film3',0],[2,'Film3',0],[1,'Holiday']],
        'Holiday':[[0,'Categories'],[1,'Decade'],[1,'Film'],[1,'Holiday'],[2,'Easter',0],[2,'Halloween',0],[2,'Christmas',0]],

        'Sale':[[0,'Sale'],[2,'0-10% Off',1],[2,'10-20% Off',1],[2,'20-50% Off',1]],
        'Gender':[[0,'Gender',2],[2,'Male',2],[2,'Female',2]]
    }
    return searchBar



def getSizes():
    sizes = ['0','1','2','3','4','5','6','7','8','9','10','11','12','14','16']
    return sizes

def getGenders():
    genders = ['Male','Female']
    return genders






def getAllItems(items):
    #items in shape [[id, name, price, sale, gender, imgurl, sizes, tags]]
    #items in shape [[199, 'vudlCzX', 59, 33, 'f', 'unknown.png', 3, 5, 'Fairies & Pixies', 'Occupations & School', 'Book Week Girls']]

    #getting the dropdown menus
    unsortedTags = getCategories()
    tags = []
    genders = getGenders()
    sizes = getSizes()
    for item in unsortedTags.values():
        for x in item:
            if len(x) > 2:
                if x[2] == 0:
                    tags.append(x[1])






    html = '''
        <table class  = 'update'>
        <tr>
        <th style="border-style:none;">EDIT ITEMS</th>
        </tr>
    '''
    for item in items:
        genderHtml = ''

        if item[4] == 'm':
            genderHtml += f'''
                            <a>Male <input type="checkbox" name = Male checked = "True"></a>
                            <a>Female <input type="checkbox" name = Female></a>
                            '''
        if item[4] == 'f':
            genderHtml += f'''
                            <a>Male <input type="checkbox" name = Male></a>
                            <a>Female <input type="checkbox" name = Female checked = "True"></a>
                            '''
        if item[4] == '':
            genderHtml += f'''
                            <a>Male <input type="checkbox" name = Male></a>
                            <a>Female <input type="checkbox" name = Female></a>
                            '''

        tagHtml = ''
        for t in tags:
            added = False
            for c in item[5:]:
                if t == c:
                    added = True
                    tagHtml += f'<a>{t} <input type="checkbox" name = {t} checked = "True"></a>'
            if not added:
                tagHtml += f'<a>{t} <input type="checkbox" name = {t}></a>'

        sizeHtml = ''
        for t in sizes:
            addedSize = False

            for c in item[5:]:

                if str(t) == str(c):
                    addedSize = True
                    sizeHtml += f'<a>{t} <input type="checkbox" name = {t} checked = "True"></a>'
            if not addedSize:
                sizeHtml += f'<a>{t} <input type="checkbox" name = {t}></a>'



        html += f'''
        <tr id = {item[0]}>
            <th><input type='text' placeholder='{item[1]}' id = 'name{item[0]}'></th>
            <th><input type='text' placeholder='${item[2]}' id = 'price{item[0]}'></th>
            <th><input type='text' placeholder='{item[3]}% Off' id = 'sale{item[0]}'></th>
            <th>
                <div class = 'dropdown'>
                        <div onclick="myFunction('genderDropdown{item[0]}')" class="dropbtn">Gender</div>

                        <div id="genderDropdown{item[0]}" class="dropdown-content">
                                <input type="text" placeholder="Search.." id="genderInput{item[0]}" onkeyup="filterFunction('genderInput{item[0]}','genderDropdown{item[0]}')">
                                    {genderHtml}
                        </div>
                </div>
            </th>
            <th>
                <div class = 'dropdown'>
                        <div onclick="myFunction('tagDropdown{item[0]}')" class="dropbtn">Tags</div>

                        <div id="tagDropdown{item[0]}" class="dropdown-content">
                                <input type="text" placeholder="Search.." id="tagInput{item[0]}" onkeyup="filterFunction('tagInput{item[0]}','tagDropdown{item[0]}')">
                                    {tagHtml}
                        </div>
                </div>
            </th>
            <th>
                <div class = 'dropdown'>
                        <div onclick="myFunction('sizeDropdown{item[0]}')" class="dropbtn">Sizes</div>

                        <div id="sizeDropdown{item[0]}" class="dropdown-content">
                                <input type="text" placeholder="Search.." id="sizeInput{item[0]}" onkeyup="filterFunction('sizeInput{item[0]}','sizeDropdown{item[0]}')">
                                    {sizeHtml}
                        </div>
                </div>
            </th>
            <th>
                <form action="/addItem" method = "post" id = "upload{item[0]}" enctype='multipart/form-data'>

                        <input type = "file" name = "pImg" id = "pImg">
                        <input type = "hidden" name = "pId" value = {item[0]}>

                </form>
            </th>
            <th>delete</th>
            <th><div onclick="updateItems({item[0]})">Update</div></th>
        </tr>
        '''


    return html




#getAllItems([[199, 'vudlCzX', 59, 33, 'f', 'unknown.png', 3, 5, 'Fairies & Pixies', 'Occupations & School', 'Book Week Girls']])



















