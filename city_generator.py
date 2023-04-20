# This is a little script written by Willey to assign participants their city for missionary work

print("Welcome all Volunteers for ", end="",)
print("missionary work " .title())

print("\n")

print("You will be assigned missionary cities based on your number tag")

names=input("Enter your name: " )
nums=int(input("Whats your tag: "))

print("\n")

def citypicks():
    if nums>=1 and nums<=3:
        citys="Bethlehem"
        #print(citys)
    elif nums>=4 and nums<=6:
        citys='Rome'
        #print(citys)
    elif nums>=7 and nums<=9:
        citys="Babylon"
        #print(citys)
    else:
        citys="Africa"
        #print(citys)
    return citys

        
def assigns():
    picks=citypicks()
    print("Hello", end=" ",)
    print(names .title(), end=" ",) 
    print("you have been posted for Missionary work in:", picks)
    
    
assigns()
