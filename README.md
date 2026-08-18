# Calculateur de Trajet Zemidjan / Taxi

## Description

Ce projet est un calculateur de trajet réalisé en Python dans le cadre du challenge **30 Days of Python 2026 — PyCon Togo**.

Le programme permet de calculer le prix d'un trajet en **Zemidjan** ou en **Taxi**, en fonction de la distance et de l'heure du trajet.

Le programme prend également en compte les majorations appliquées pendant les heures de pointe.

## Fonctionnalités

* Choix entre Zemidjan et Taxi
* Calcul du prix selon la distance
* Détection des heures de pointe
* Application des majorations
* Calcul de plusieurs trajets
* Historique des trajets de la session
* Arrondissement du prix au multiple de 25 FCFA le plus proche
* Gestion des erreurs de saisie

## Tarifs

Transport :  Zemidjan / Taxi
Tarif de base :  150 FCFA / 200 FCFA
Prix/km : 75 FCFA / 100 FCFA 
Majoration : 15 % / 25 % 

### Heures de pointe

* 07h00 - 08h45
* 11h45 - 13h00
* 17h00 - 19h00

## Installation

Aucune bibliothèque externe n'est nécessaire.

Il faut simplement avoir python installé.

## Lancement

Dans le terminal, se placer dans le dossier du projet puis exécuter :

```bash
python calculateur-de-trajet.py
```

## Exemple d'exécution

```text
CALCULATEUR DE TRAJET
Veuillez choisir une option.
1 - Zemidjan
2 - Taxi
0 - Quitter

Choisissez votre moyen de transport : 1
Entrer la distance en km : 5
Entre l'heure du trajet (ex: 11:45) : 07:30

RÉCAPITULATIF
moyen : Zemidjan
Distance : 5.0 km
Heure : 07:30
Heure de pointe : Oui
Prix final : 600 FCFA
```

## Auteur

**Prénom :** Jedidja

**Username Fata :** @legendb

**GitHub :** https://github.com/Blackvelt/
## Challenge

Projet réalisé dans le cadre du **Challenge 30 Days of Python 2026 — PyCon Togo**.

