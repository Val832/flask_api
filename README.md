# Aperçu du Projet

Ce projet est une évolution du "Projet de Modélisation de Données" ([data_modeling](https://github.com/Val832/data_modeling)) ainsi que des "Projets de Scraping" ([scrap_projects](https://github.com/Val832/scrap_projects)).

## Description du Projet

La base de données semi-structurée issue du projet d'extraction de données de Castorama a été initialement transformée en une base de données relationnelle via SQLite.Une migration  de la base vers PostgreSQL a ensuite été entrepris, un SGBD plus robuste et adapté à l'usage en entreprise. PostgreSQL a été configuré pour fonctionner localement, avec l'implémentation de mesures de sécurité telles que l'utilisation de variables d'environnement et de clés secrètes.

## Fonctionnalités

- **Migration vers PostgreSQL** : Transition d'une base de données SQLite vers une base de données PostgreSQL.
- **Configuration de Sécurité PostgreSQL** : Installation et configuration de PostgreSQL avec des mesures de sécurité essentielles.
- **API REST avec Flask** : Mise en place d'une API RESTful conçue pour faciliter les interactions client-serveur.
- **Routes API Internes** : Définition de routes API optimisées pour les besoins internes de l'entreprise.
- **Sérialisation des Données et Blueprints** : Création de modèles pour la sérialisation des données et utilisation de blueprints pour une organisation efficace du code.
