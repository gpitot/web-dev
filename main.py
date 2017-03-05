import bottle
from bottle import static_file
import os
from bottle import error

#other python files
import interface
import content
import security




#setting up bottle
app = bottle.Bottle()
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

@app.route('/images/<filename>')
def server_images(filename):
    return static_file(filename, root='images')

@app.route('/images/costumes/<filename>')
def server_costumes(filename):
    return static_file(filename, root='images/costumes')

@app.error(404)
def error404(error):
    return 'Page not found.'







@app.route('/')
def main():
    return bottle.template(os.path.join('views','main.tpl'),)



@app.route('/range')
def products():
    sideNav = content.sideBarMenu()
    return bottle.template(os.path.join('views','range.tpl'),sideNav = sideNav)


@app.post('/loadData')
def loadData():
    print('loading')
    c = interface.connect()
    dict = bottle.request.json['searchProductsDict']
    price = dict['price']
    categories = dict['categories']
    result = interface.retrieveData(c,price,categories)
    resultHtml = content.rangeMainContent(result)
    resultJson = {'contentMain':resultHtml}
    return resultJson



@app.route('/admin')
def admin():
    return bottle.template(os.path.join('views','admin.tpl'),
                           loginVisible = '$(".edit").hide();',gendersDropdownHtml = '',
                           tagsDropdownHtml='',sizesDropdownHtml='',checkedArray = '[];',tableList = '')



@app.post('/admin')
def admin():
    c = interface.connect()
    username = bottle.request.forms['username']
    password = bottle.request.forms['password']
    hashedPass = security.pass2hash(password)
    checkPass = interface.checkPass(c,username,hashedPass)

    if checkPass:
        return adminTable()
    else:
        return bottle.template(os.path.join('views','admin.tpl'),loginVisible = '$("#edit").hide();'
                               ,gendersDropdownHtml = '',
                           tagsDropdownHtml='',sizesDropdownHtml='',
                               checkedArray = '[];')

@app.post('/addItem')
def addItem():
    #UPLOAD THE ITEM to file AND RETURN THE TPL
    c = interface.connect()

    print('uploading attempt [addItem]')
    upload = bottle.request.files.get('pImg')
    id = bottle.request.forms['pId']
    print(id)
    print('upload = ', upload)
    if upload != None:
        if upload.content_type == 'image/jpeg' or upload.content_type == 'image/png':
            print('png')
            name = upload.filename
            save_path = os.path.join("images/costumes", upload.filename)
            try:
                upload.save(save_path)
            except OSError:
                name = '2' + upload.filename
                save_path = os.path.join("images/costumes", name)
            print(name)
            interface.addFileName(c, name, id)
    return adminTable()






@app.post('/editItem')
def editItem():
    c = interface.connect()
    data = bottle.request.json['jsonData']
    print(data)
    checkArray = data['checklist']
    id = data['id']
    name = data['name']
    price = data['price']
    sale = data['sale']
    print(id,name,price,sale,checkArray)

    genderCheck = checkArray[0]
    tagsCheck = checkArray[1]
    sizesCheck = checkArray[2]

    unsortedTagsList = content.getCategories()
    tagsSorted = []
    for item in unsortedTagsList.values():
        for x in item:
            if len(x) > 2:
                if x[2] == 0:
                    tagsSorted.append(x[1])
    sizesList = content.getSizes()
    gendersList = content.getGenders()

    gender = []
    for g in range(0, len(genderCheck)):
        if genderCheck[g]:
            gender.append(gendersList[g])

    tags = []

    for t in range(0, len(tagsCheck)):
        if tagsCheck[t]:
            tags.append(tagsSorted[t])

    sizes = []
    for s in range(0, len(sizesCheck)):
        if sizesCheck[s]:
            sizes.append(sizesList[s])

    interface.addItem(c, id, name, tags, price, sale, sizes, gender)


    return {'success':'yes'}









def adminTable():
    c = interface.connect()
    dropdowns = content.getDropdowns()
    listOfItems = interface.getItems(c)
    itemTable = content.getAllItems(listOfItems)
    return bottle.template(os.path.join('views','admin.tpl'),loginVisible = '$(".login").hide();$("#edit").show();'
                               ,gendersDropdownHtml = dropdowns[0],
                                tagsDropdownHtml=dropdowns[1],
                                sizesDropdownHtml=dropdowns[2],
                                checkedArray = dropdowns[3],
                                tableList = itemTable
                        )



if __name__ == "__main__":
    app.run()
