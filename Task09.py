# *********** Finding the percentage ************


telebe = {

    "samir": [20, 30, 40],
    "ali": [10, 10, 50],
    "samira": [30, 40, 50]
}


yoxla = input("ortalama qiymetini bilmek istediyiniz telebenin adini yazin : ")


def OrtalamaHesab():
    for i in telebe:
        if yoxla == i:
            x = telebe.get(yoxla)
            print(i)
            print(x)

    ortalama = sum(x)/len(x)
    print(ortalama)
    

OrtalamaHesab()
       
    
         
      
   














