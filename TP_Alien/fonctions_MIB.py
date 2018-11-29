# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:49:31 2018

@author: titou
"""
from MaBase_MIB import*

def lettre(gardien,aliment):
    if gardien[0]==aliment[0]:
        n='oui'
    else:
        n='non'
    return(n)
    
    
def autre(gardien,aliment):
    return( gardien[0]==aliment[0])
       
def nom_x(nom) :
    n=0
    for i in range (len(nom)):
        if nom[i]=='x':
            n=n+1
    if n!=0 :
        return(nom)
        
def question_11(ensemble) :
    if len(ensemble)>0 :
        print('oui')
    else :
         print("non")

def lettre_aliment (gardien,aliment):
    n=0
    if gardien[0]==aliment[0]:
        n=n+1
    return(n)