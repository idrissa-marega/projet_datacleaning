# Projet : Pipeline de Nettoyage CRM & Catalogue Produit

Ce projet contient pipelines python permettant de nettoyer et d'unifier des données clients (CRM) issues du fichier clients.csv ainsi que des catalogue issues des fichiers catalog_fr.csv et catalog_us.csv

L’objectif est d'obtenir des données propres, standardisées et prêtes à être utilisées

Prérequis : il faut d'abord installer python et les dépandances (pip install pandas)

# Pipeline CRM



OBJECTIFS :

Standardiser : emails, pays, téléphones, dates
Supprimer les doublons
calculer des indicateurs de qualité de données


TRAVAIL EFFECTUE :

Normalisation des emails (minuscule)
Nettoyage des numéros de téléphone
Harmonisation des pays
Dates au format ISO
Suppression des doublons basés sur l’email
KPI qualité : lignes initiales, finales, doublons supprimés, valeurs manquantes

FICHIER GENERE : 

clients_clean.csv 
kpi_qualite.csv


# Pipeline Catalogue

OBJECTIFS :

Fusionner les catalogues français & américains

Convertir unités :
Poids → kg
Prix → €

Harmoniser les catégories via mapping_categories.csv
Supprimer les doublons de SKU


TRAVAIL EFFECTUE :  

Conversion poids (lb → kg)
Conversion prix ($ → €)

Normalisation des colonnes
Mapping des catégories (source → target)
Dé-duplication des SKU (garde le produit le plus pertinent)
KPI catalogue : produits avant/après, catégories manquantes

FICHIER GENERE : 

catalog_canonique.csv
kpi_catalogue.csv
