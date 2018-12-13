# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:05:05 2018

@author: titou
"""

#code cryptage :

def minuscules(k,a,b) :
    """cette fonction crypte les lettres en minuscules en utilisant leurs codes unicode """
    num=a*(ord(k)-97)+b                             #transformation du code unicode(-97 pour obtenir un  nombre en 0 et 25) du caractère par la fonction affine donnée par le couple (a,b)
    num=num%26
    lettre=chr(num+97)                              #renvoi du caractere associé au nombre renvoyé par l'image de la fonction modulo 26
    return(lettre)
    
def majuscules (k,a,b) :
    """cette fonction crypte les lettres en majuscules en utilisant leurs codes unicode"""
    num=a*(ord(k)-65)+b                             #transformation du code unicode(-97 pour obtenir un  nombre en 0 et 25) du caractère par la fonction affine donnée par le couple (a,b)
    num=num%26
    lettre=chr(num+65)                              #renvoi du caractere associé au nombre renvoyé par l'image de la fonction modulo 26
    return(lettre)
    

def PGCD(a,b) :
    """cette fonction calcule le PGCD de 2 nombres par l'algorithme d'Euclide
       quel que soit l'ordre d'entrée des termes 
    """
    c=max(a,b)
    d=min(a,b)
    #prise du max et du min pour que le calcul puisse se faire 
    #peu importe l'ordre de saisie des termes
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
    """fonction cryptant les termes en fonction de leurs codes unicode"""
    if (ord(lettre)>=97 and ord(lettre)<=122) :             #codage des minuscules 
        return(minuscules(lettre,cle_a,cle_b))
    elif(ord(lettre)>=65 and ord(lettre)<=90) :             #codage des majuscules 
        return(majuscules(lettre,cle_a,cle_b))
    else :                                                  #codage des caractères spéciaux (inchangés)
        return(lettre)
    
    
def decryptage(lettre,cle_a,cle_b):
    """ permet le décryptage des termes en fonction du couple de clés 
        (a,b) utilisées """
    if (ord(lettre)>=97 and ord(lettre)<=122) :     #décryptage des minuscules
        num=ord(lettre)-97                      #donne la valeur associé au caractère comprise entre 0 et 25
        num=(num-cle_b)%26                      
        num2=(num*inverse(cle_a,26))%26         #renvoi la valeur modulo 26 associée au caractère décrypté
        return(chr(num2+97))                    #retourne le caractère décrypté
        
    elif(ord(lettre)>=65 and ord(lettre)<=90):      #décryptage des majuscules (meme fonctionnement que pour les minuscules)
        num=ord(lettre)-65
        num=(num-cle_b)%26
        num2=(num*inverse(cle_a,26))%26
        return(chr(num2+65))
    else :                                          #décryptage caractères speciaux
        return(lettre)

# programme principal        
import random

p=0
while(p!=4) :
    p=int(input("que voulez vous faire (1:cryptage, 2:décryptage,3:quitter le programme) : "))    
    c=0
    if p==1 :   
        fichier1=open('texte_codé.txt','w')
        while(c!=1 and c!=2):
            c=int(input("clés aléatoires (saisir 1) ou clés choisies(saisir 2) : "))  # choix entre un couple de clés aléatoires ou un couple de clés entrées par l'utilisateur
        if c==1 :
            a=random.randint(1,25)
            b=random.randint(0,25)
        if c==2 :    
            a=int(input('donner la clé a : '))
            b=int(input ('donner la clé b : '))
        texte=input('texte a coder : ')
        texte_code=''
        for k in texte:     
            texte_code=texte_code+cryptage(k,a,b)
        print("le texte : \n",texte,"\n\ncodé avec le couple(%s,%d) donne \n\n:"%(a,b),texte_code)      
        fichier1.write(texte_code)
        fichier1.close()
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
    if p==3 :
        fichier=open(r"C:\Users\titou\Documents\UCO\Info\complement_info\projet_crypto\Notre_Dame_de_Paris.txt","r")
        fichierP=open("Notre_Dame_de_Paris_Crypte.txt","w")
        a=random.randint(1,25)
        b=random.randint(0,25)
        code=''
        for k in fichier :
            lettre=decryptage(k,a,b)
            code=code+lettre
        fichierP.write(code)
        fichierP.close()
        fichier.close()
        
        
            
            
   
            
