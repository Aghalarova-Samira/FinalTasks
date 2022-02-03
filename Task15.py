#********* Find a string *************

birinciSoz = input("Sozu yazin: ")
ikinciSoz = input("Sozu yazin: ")

count = 0
flag = True
start = 0

while flag:
    a = birinciSoz.find(ikinciSoz, start)
    if a == -1:    
        flag = False
    else: 
        count += 1  
        start = a + 1
print(count)










# word = 'geeks for geeks'
  
# # returns first occurrence of Substring
# result = word.find('geeks')
# print ("Substring 'geeks' found at index:", result )
