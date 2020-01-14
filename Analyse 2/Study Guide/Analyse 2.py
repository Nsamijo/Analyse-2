class Lesson1:
    '''This class will contain examples for lesson one: Lists'''

    listName = ''
    listElements = []

    #set and get name from the list
    def setName(name):
        self.listName = name

    def getName():
        return self.listName

    #list functions
    def addToList(item):
        self.listElements.append(item)

    def deleteItem(num):
        try:
            del(self.listElements[num])
        except:
            print('Error 404! Index number not valid!')
            print('Avaliable numbers: ' + str(range( len( self.listElements) ) ) )

    def printList():
        print(self.listElements)