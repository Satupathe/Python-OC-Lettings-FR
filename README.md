## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement de l'application

### Fonctionnement général du déploiement
Lorsque de nouvelles modifications sont poussées vers le Dépôt GitHub, le pipeline s'active pour lancer les tests via la commande pytest. Il y a vérification aussi des conventions d'écriture PEP8 avec FLake8.
Ces tests concernent l'ensemble des branches.

Lorsque les changements sont effectués et poussés à partir de la branche master, la seconde partie du pipeline s'engage en complément:
Si l'ensemble des tests est validé la construction de l'image Docker démarre:
  - Login au dépôt DockerHub
  - Contruction de l'image Docker de l'application et ajout d'un tag
  - Publication de l'image sur le DockerHub

Si la construction de l'image Docker est réussie, le déploiement est amorcé:
  - Installation de Heroku CLI
  - Mise en place du lien entre Docker et Heroku
  - Création des variables d'environnement
  - Connection de Heroku au DockerHub
  - Récupération de l'image et publication sur Heroku
  - Déploiement de l'image

### Configuration
- Un compte Github
- Un compte CircleCI
- Variables d'environnement du projet sur CircleCI:
    1. Clé API Heroku
    2. Nom du dépôt dockerHub
    2. Login DockerHub
    3. Mot de passe Dockerhub, clé secrete Django)
    4. Nom de l'application Heroku
- Un compte DockerHub et un dépôt distant pour le projet
- Un compte Heroku et un dépôt distant pour le projet
- Un compte Sentry

### Etapes nécessaires
- Créer un nouveau projet sur GitHub
- Récupérer les fichiers du projet
- Lier le compte CircleCI et le compte GitHub
- Ajouter les variables d'environnement dans le projet sur CircleCI
- Créer une nouvelle application sur Heroku
- Ajouter Heroku-Postgres dans les add-ons
- Créer un nouveau dépôt sur DockerHub
- Créer un nouveau projet Sentry 
- Ajouter le lien du projet fournit par Sentry en bas de Settings.py dans sentry_sdk.init(dsn =... 
- Adapter le fichier config.yml du dossier circleci
- Pousser les modifications à partir de la branche master

## Accès à l'application

### Via Docker
 - Ouvrir le terminal de commande
 - Aller sur DockerHub et récupérer le tag de la dernière image poussée vers le dépôt distant.
 - Copier le nom de l'image
 - Taper la commande dans le terminal: `docker run -p 8080:8080 satupathe/orange_lettings_oc:270a7a61966940e58cce7db12170a527a4fec0d7` le numéro après les : dépends de la version de l'image précédemment copiée
 - Entrer l'adresse suivante dans le navigateur : 127.0.0.1:8000

### Avec Heroku
  https://oc-lettings-12.herokuapp.com/ 
