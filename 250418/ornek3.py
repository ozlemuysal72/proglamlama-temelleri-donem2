otopark=int(input("Kaldığınız süreyi giriniz :"))   
if otopark == 1 :
    print("ödeyeceğiniz miktar :,5TL ") 
elif otopark >1 and otopark <5:
    print("ödeyeceğiniz miktar:",otopark *4)  
elif otopark >=5:
    print("ödeyeceğiniz miktar:",otopark *5) 
else:
    print("yanlış bilgi girdiniz ")                                    