#********* Find the Runner-Up Score! **********

scores = []
while True:
    n = int(input("skoru daxil edin: (1-10) "))
    scores.append(n)

    scores.sort(reverse=True)
 
    print(scores)
    if len(scores)>1:
        print(scores[1])

    

  



