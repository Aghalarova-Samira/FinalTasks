#******** Nested Lists *********



records = [

["ali",50],
["gunay",60],
["samir", 70],
["samira",60],
["togrul",70]

]


list = []
listQiymet = []
SagirdSayi=(len(records))
# print(SagirdSayi)


for i in records:
    # print(i[0])
    # print(i[1])
    list.append(i[0])
    list.append(i[1])
    listQiymet.append(i[1])

listQiymet.sort()

def secGade():
    for i in range(len(listQiymet)):
     
       if listQiymet[i] != listQiymet[i+1] :
           return listQiymet[i+1]



# print(secGade())

def alfabetik():
    a = secGade()
    alfabetikList = []
    for i in records:
       if a in i:

        #  print(i[0])
         alfabetikList.append(i[0])
         
    alfabetikList.sort()
    print(alfabetikList)




alfabetik()        

       
    















    
         











    