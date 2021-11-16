integer = int(input())
n =integer
force = True
while force:
    if(integer==0):
        force = False
    elif(integer%2==0 and integer%n==0):
        force = False
    else:
        integer+=1

print(integer)  