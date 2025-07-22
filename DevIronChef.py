# Farrahpepino,Daniel Woods,Daniel Wooda,Sam Miller,Greydon CAST Timthoy,zoe Harris,Rayn saad,julain ,nick stokES,elliot 

ironchef = []

print("Tracking Iron Chef:", ironchef)

ans = input("Did you finish an iron chef today? yes or no")       

while (True):
    if ans=="yes":
        staff = input("Whose iron chef did you finish? ")
        print("Adding", staff)
        ironchef.append(staff)
        print("You finished", len(ironchef), "staffs' iron chef:", ironchef)
        ans = input("Would you like to add more? ")
        if ans  == "yes":
            continue
        if ans == "no":
            print("No more")
            print("Iron chef list:", ironchef)
    elif ans=="no":
        print("You finished", len(ironchef), "staffs' iron chef:", ironchef)
        break
    

if len(ironchef)==56:
    print ("Congratulations! You've won the Iron Chef Challenge! " )


