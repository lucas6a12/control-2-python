#lucas gutierrez#
def calcularcosto(ms):
    total = 0
    for i in ms:
        if(i=="ñ" or i=="á" or i=="é" or i=="í" or i=="ó" or i =="ú"):
            total = total+30
        elif(i>-99999999999 or i<9999999999):
            total = total+20
        else:
            total = total+10
    return total


print("ingrese mensaje")
ms = input()
print("el valor del mensaje:",ms,"es de $",calcularcosto(ms))

