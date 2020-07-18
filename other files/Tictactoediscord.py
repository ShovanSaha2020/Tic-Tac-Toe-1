def display(kclist):
    print("--------")
    for i in range(0,7,3):
        print(f"|{kclist[i]}|{kclist[i+1]}|{kclist[i+2]}|")
    print("--------")

def userchoice(coordinates,turn,kclist):
    while True:
        choice=input("Enter the coordinates: ")
        if choice not in coordinates or choice==".":
            print("Please enter a suitable choice.")
            continue
        index=[i for i in range(len(coordinates)) if coordinates[i]==choice][0]
        if turn%2==0:
            kclist[index]="X"
        else:
            kclist[index]="O"
        coordinates[index]="."
        return coordinates,turn,kclist

def winner(kclist):
    outcomes=[[0,1,2],[0,3,6],[3,4,5],[1,4,7],[6,7,8],[2,5,8],[0,4,8],[2,4,6]]
    for l in outcomes:
        if kclist[l[0]]==kclist[l[1]]==kclist[l[2]] and not any(j=="-" for j in [kclist[l[0]],kclist[l[1]],kclist[l[2]]]):
            return True
    return False

coordinates=["1 3","2 3","3 3","1 2","2 2","3 2","1 1","2 1","3 1"]
turn=0
knotsandcrosses=["-" for i in range(9)]

for i in range(9):
    display(knotsandcrosses)
    coordinates,turn,knotsandcrosses=userchoice(coordinates,turn,knotsandcrosses)
    turn+=1
    if winner(knotsandcrosses)==True:
        display(knotsandcrosses)
        break




    



        

