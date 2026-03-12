############# Partie 1 : Création d’une structure de base 

from abc import ABC , abstractmethod 

class Boisson (ABC) : 

  @abstractmethod
  def cout(self) : 
    pass
  @abstractmethod 
  def description(self) : 
    pass

  def __add__(self , other) : 
    return Combiner_Boisson(self , other)
  
  
############# Partie 2 : Création de boissons concrètes

class Cafe(Boisson) :

  def cout(self) : 
    return 2.0
  
  def description(self) : 
    return "Café simple"
  
class The(Boisson) :

  def cout(self) :
    return 1.5 

  def description(self) : 
    return "Thé"
  

############# Partie 3 : Ajout d’ingrédients

class DecorateurBoisson(Boisson) : 

  def __init__(self , boisson) : 
    self._boisson = boisson 

### Ajout de lait 
class Lait(DecorateurBoisson) : 

  def cout(self) : 
    return self._boisson.cout() + 0.5 
  
  def description(self) : 
    return self._boisson.description() + " au lait"
  
### Ajout de sucre 
class Sucre(DecorateurBoisson) : 

  def cout(self) : 
    return self._boisson.cout() + 0.2
  
  def description(self) : 
    return self._boisson.description() + " sucré"  
  
### Ajout de caramel 
class Caramel(DecorateurBoisson) : 

  def cout(self) : 
    return self._boisson.cout() + 0.3
  
  def description(self) : 
    return self._boisson.description() + " au caramel"
  
############# Partie 4 : Combinaison de boissons

class Combiner_Boisson(Boisson) : 
   def __init__(self , boisson1 , boisson2) : 
    self._boisson1 = boisson1
    self._boisson2 = boisson2 

   def cout(self) : 
    return self._boisson1.cout() + self._boisson2.cout() 
   
   def description(self) : 
    return self._boisson1.description() + " + " + self._boisson2.description()
   
############# Partie 5 : Représentation d’un client 

from dataclasses import dataclass 

@dataclass
class Client : 
  nom : str 
  numero : int 
  points_fidelite : int = 0 

############# Partie 7 : Gestion des commandes (héritage multiple et polymorphisme)
### 1 ###
class Commande : 
  def __init__(self , client) : 
    self._client = client
    self._boissons = []

  def ajouter_boisson(self , boisson) : 
     self._boissons.append(boisson)

  def prix_total(self) : 
    total = 0 
    for boisson in self._boissons : 
      total = total + boisson.cout()
    return total 
  
  def afficher_commande(self) : 
    print("Client :", self._client.nom)
    print("Boissons commandées :")
    for boisson in self._boissons : 
      print( boisson.description(), ":" , boisson.cout(),"€")

    print("Total : ", self.prix_total(), "€") 

### 2 ###
class CommandeSurPlace(Commande): 
  def afficher_commande(self) : 
    print("Commande sur place ")
    super().afficher_commande()

class CommandeEmporter(Commande):   
  def afficher_commande(self) : 
    print("Commande a emporter ")
    super().afficher_commande() 

### 3 ###
class Fidelite : 
  def ajouter_points_fidelite(self , client , montant) : 
    points_fidelite = int(montant)
    client.points_fidelite += points_fidelite

### 4 ###
class CommandeFidele(Commande , Fidelite) : 
  def valider_commande(self) : 
    total = self.prix_total() 
    self.ajouter_points_fidelite(self._client , total )

### 5 ###
# créer des clients
client1 = Client("aya" , 1)
client2 = Client("Narjes" , 2)

cafe = Cafe()
the = The()

# créer plusieurs boissons
boisson1 = cafe
boisson2 = Lait(cafe)
boisson2 = Sucre(boisson2)
boisson3 = Caramel(cafe)
boisson4 = the
boisson5 = Lait(the)
boisson5 = Sucre(boisson5)

# créer les commandes
commande1 = CommandeFidele(client1)
commande2 = Commande(client2)

# ajouter des boissons
commande1.ajouter_boisson(boisson1)
commande1.ajouter_boisson(boisson2)
commande1.ajouter_boisson(boisson3)
commande1.ajouter_boisson(boisson4)
commande1.ajouter_boisson(boisson5)

commande2.ajouter_boisson(boisson3)
commande2.ajouter_boisson(boisson5)

# afficher le contenu de la commande
commande1.afficher_commande()

# afficher les points de fidélité du client après la validation
commande1.valider_commande()
print("Points de fidelite du client  :", client1.points_fidelite)

commande2.afficher_commande()
print("Points de fidelite du client  :", client2.points_fidelite)


############# Partie 8 : Questions de réflexion

### 1 ### partie 3 class DecorateurBoisson

### 2 ### Aucune il faut juste definir une autre classe dans partie 2 appele class ChocolatChaud(Boisson) : herite de la classe abstraite Boisson

### 3 ### Programme plus clair et plus organise et il permet de modifier ou ajouter une fonctionnalite sans devoir changer tout le programme .




       



   


   




  

  




  
