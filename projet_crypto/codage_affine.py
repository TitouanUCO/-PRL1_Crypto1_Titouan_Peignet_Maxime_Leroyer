# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:05:05 2018

@author: titou
"""

#code cryptage :

def minuscules(k,a,b) :
    """cette fonction crypte les lettres en minuscules en utilisant leurs codes ASCII """
    num=a*(ord(k)-97)+b
    num=num%26
    lettre=chr(num+97)     
    return(lettre)
    
def majuscules (k,a,b) :
    """cette fonction crypte les lettres en majuscules en utilisant leurs codes ASCII"""
    num=a*(ord(k)-65)+b
    num=num%26
    lettre=chr(num+65)
    return(lettre)
    

def PGCD(a,b) :
    """cette fonction calcule le PGCD de 2 nombres par l'algorithme d'Euclide
       quel que soit l'ordre d'entrée des termes 
    """
    c=max(a,b)
    d=min(a,b)
    """prise du max et du min pour que le calcul puisse se faire 
       peut importe l'ordre de saisie des termes""" 
    while(c>=d):
        r=c%d
        if(r==0):
            return(d)
        else:
            c=d
            d=r

def inverse(a,b):
    """renvoie l'inverse d'un nombre a au modulo b
       Attention: a doit etre premier avec b 
    """
    k=0
    while(((a*k)%b)!=1):
        k=k+1
    return(k)

def cryptage(lettre,cle_a,cle_b) :
    """fonction cryptant les termes en fonction de leurs codes ASCII"""
    if (ord(lettre)>=97 and ord(lettre)<=122) :
        return(minuscules(lettre,cle_a,cle_b))
    elif(ord(lettre)>=65 and ord(lettre)<=90) :
        return(majuscules(lettre,cle_a,cle_b))
    else :
        return(lettre)
    
    
def decryptage(lettre,cle_a,cle_b):
    """ permet le décryptage des termes en fonction du couple de clés 
        (a,b) utilisées """
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

# programme principal        
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
        print("le texte"/n,texte,"codé donne :",texte_code)        
    if p==2 :
        a=int(input("donnez la clé a utilisée : "))
        b=int(input("donnez la clé b utilisée : "))
        texte=input("donnez le texte a décoder : ")
        decodage=''
        if PGCD(a,26)==1 :
            for k in texte :
                lettre_de=decryptage(k,a,b)
                decodage=decodage+lettre_de
            print(decodage)
        else : 
            print("impossible a decrypter puisque a n'est pas premier avec 26")

        
            
        
    
    
        