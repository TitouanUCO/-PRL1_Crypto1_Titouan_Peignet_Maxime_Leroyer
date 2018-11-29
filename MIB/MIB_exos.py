# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:46:04 2018

@author: titou
"""
# -*- coding: utf-8 -*-

from MaBase_MIB import *


### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
les_villes_agents = {agent.Ville for agent in BaseAgents}
triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

#question 4 :
couples = { (alien.Nom, cabine.NoAllee) for alien in BaseAliens for cabine in BaseCabines if cabine.NoCabine == alien.NoCabine}

#question 5 :
allee2={ (alien.Nom) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine == cabine.NoCabine and cabine.NoAllee == '2'}

#question 6 :
cabine_pair={alien.Planete for alien in BaseAliens for cabine in BaseCabines if int(alien.NoCabine)%2 == 0}

#question 7 :
gardien_Terminus={alien.Nom for alien in BaseAliens for cabine in BaseCabines for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}

#question 8 :
gardien_feminins_bortsch={gardien.Nom for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if alien.NoCabine==gardien.NoCabine and alien.Sexe=='F' and alien.Nom==miam.NomAlien and miam.Aliment=='Bortsch'}

#question 9 :
Terminus_ou_filles={gardien.NoCabine for cabine in BaseCabines for gardien in BaseGardiens for agent in BaseAgents for alien in BaseAliens if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and (agent.Ville=='Terminus'or alien.Sexe=='F')}

#question 10 :
lettre_aliment_gardien={ miam.Aliment for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams for cabine in BaseCabines if gardien.NoCabine==alien.NoCabine and alien.Nom==miam.NomAlien  and gardien.Nom[0]==miam.Aliment[0] }
question_10={len(lettre_aliment_gardien)!=0}

# question 11 : existe t'il alien d'eurterpe
euterpe={alien.Nom for alien in BaseAliens if alien.Planete=='Euterpe'}
question11={len(euterpe)==0}
   
                           

#question 12 :
alien_x={alien.Nom for alien in BaseAliens if 'x' in alien.Nom}   #ensemble des aliens ayant un x dans leur nom
nom_alien={alien.Nom for alien in BaseAliens}
question_12={len(alien_x)==len(nom_alien)}
    
#question 13 :
question_13={gardien_Terminus.issubset(alien_x) for alien in BaseAliens }  

#question 14 :
condition={alien.Nom for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents for cabine in BaseCabines for miam in BaseMiams if alien.Nom==miam.NomAlien  and  alien.Sexe=='M' and alien.Planete=='Trantor' and ( miam.Aliment=='Bortsch' or (alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus') ) } #bouger les parentheses en fonction de l'interpretation de la question
question14={len(condition)!=0}    



