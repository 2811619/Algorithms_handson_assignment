# def getKeysByValue(dictOfElements, valueToFind):
#     listOfKeys = list()
#     listOfItems = dictOfElements.items()
#     for item  in listOfItems:
#         if item[1] == valueToFind:
#             listOfKeys.append(item[0])
#     return  listOfKeys

def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == listOfValues[0]:
            listOfKeys.append(item[0])
            return  listOfKeys 

if __name__ == "__main__":


    a_file = open("title.ratings.txt")
    names, ratings = [], []
    next(a_file)
    name_score_dict ={}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0]) #key: name
        ratings.append(float(temp[1])) #name: rating
        name_score_dict[temp[0]] = float(temp[1])
        sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
     8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4, 7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]
    listOfKeys = getKeysByValues(name_score_dict, ['9.4'])
print("Keys with value equal to 9.4")
#Iterate over the list of keys
sorted=[]
for key in listOfKeys:
        print(key)