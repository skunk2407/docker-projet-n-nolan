# Band Names Generator – Docker Project

## Table des matières
- [Description](#description)
- [Lancer le projet](#lancer-le-projet)
- [Gestion des environnements](#gestion-des-environnements)
- [Liens utiles](#liens-utiles)
- [Remarques](#remarques)

## Description
Projet de conteneurisation composé de trois services :
- **web** : application Flask
- **db** : base MySQL initialisée automatiquement avec `init.sql`
- **admin** : interface Adminer

L’application permet :
- de vérifier la communication avec la base MySQL,
- de générer 10 noms de groupe aléatoires au format **`The {adjective} {noun}`** à partir des données stockées en base.

## Lancer le projet

### 1. Préparation de l’environnement
Créer un fichier `.env` (non versionné) à partir du modèle :
```bash
cp .env.dist .env