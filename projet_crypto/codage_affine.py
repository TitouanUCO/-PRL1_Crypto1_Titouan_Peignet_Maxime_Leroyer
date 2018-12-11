# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:05:05 2018

@author: titou
"""

#code cryptage :




def minuscules(k,a,b) :
    num=a*(ord(k)-97)+b
    num=num%26
    lettre=chr(num+97)     
    return(lettre)
    
def majuscules (k,a,b) :
    num=a*(ord(k)-65)+b
    num=num%26
    lettre=chr(num+65)
    return(lettre)
    
'''a=int(input('donner la clé a : '))
b=int(input ('donner la clé b : '))
texte=input('texte a coder : ')
texte_code=''
for k in texte:     
    if (ord(k)>=97 and ord(k)<=122) :               #traitement des caractères en minuscules 
        lettre=minuscules(k,a,b)
        texte_code=texte_code+lettre
    elif(ord(k)>=65 and ord(k)<=90):                #traitement des caractères minuscules
        lettre=majuscules(k,a,b)
        texte_code=texte_code+lettre
    else :                                          #gestion caracteres spéciaux(espaces,guillemets,parenthèses)
        texte_code=texte_code+k

print(texte_code) 
'''
                

def PGCD(a,b) :
    c=max(a,b)
    d=min(a,b)
    while(c>d):
        r=c%d
        if(r==0):
            return(d)
        else:
            c=d
            d=r

def inverse(a,b):
    k=0
    while(((a*k)%b)!=1):
        k=k+1
    return(k)

def cryptage(lettre,cle_a,cle_b) :
    if (ord(lettre)>=97 and ord(lettre)<=122) :
        return(minuscules(lettre,cle_a,cle_b))
    elif(ord(lettre)>=65 and ord(lettre)<=90) :
        return(majuscules(lettre,cle_a,cle_b))
    else :
        return(lettre)
    
    



def decryptage(lettre,cle_a,cle_b):
    if (ord(lettre)>=97 and ord(lettre)<=122) : 
        num=ord(lettre)-97
        num=(num-cle_b)%26
        num2=(num*inverse(cle_a,26))%26
        return(chr(num2+97))
    elif(ord(lettre)>=65 and ord(lettre)<=90):
        num=ord(lettre)-65
        num=(num-cle_b)%26
        num2=(num*inverse(cle_a,26))%26
        return(chr(num2+65))
    else :
        return(lettre)


#programme principal
'''p=int(input("que voulez vous faire (1:cryptage, 2:décryptage) : "))    
    
if p==1 :        
    a=int(input('donner la clé a : '))
    b=int(input ('donner la clé b : '))
    texte=input('texte a coder : ')
    texte_code=''
    for k in texte:     
        texte_code=texte_code+cryptage(k,a,b)
    print(texte_code)        
if p==2 :
 
    a=int(input("donnez la clé a utilisée : "))
    b=int(input("donnez la clé b utilisée : "))
    texte=input("donnez le texte a décoder : ")
    decodage=''
    if PGCD(a,26)==1 :
        for k in texte :
            lettre_de=decryptage(k,a,b)
            decodage=decodage+str(lettre_de)
        print(decodage)
    else : 
        print("impossible a decrypter puisque a n'est pas premier avec 26")'''


#autre programme principal        
p=0
while(p!=3) :
    p=int(input("que voulez vous faire (1:cryptage, 2:décryptage,3:quitter le programme) : "))    
    
    if p==1 :        
        a=int(input('donner la clé a : '))
        b=int(input ('donner la clé b : '))
        texte=input('texte a coder : ')
        texte_code=''
        for k in texte:     
            texte_code=texte_code+cryptage(k,a,b)
        print(texte_code)        
    if p==2 :
        a=int(input("donnez la clé a utilisée : "))
        b=int(input("donnez la clé b utilisée : "))
        texte=input("donnez le texte a décoder : ")
        decodage=''
        if PGCD(a,26)==1 :
            for k in texte :
                lettre_de=decryptage(k,a,b)
                decodage=decodage+str(lettre_de)
            print(decodage)
        else : 
            print("impossible a decrypter puisque a n'est pas premier avec 26")
    else :
        p=int(input("donnez autre valeur"))
        
            
        
    
    
        