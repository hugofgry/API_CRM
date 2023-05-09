### API_CRM

# Documentation

Voici la documentation pour les différents fichiers de code que vous avez partagés. Les fichiers de code sont organisés en sections pour faciliter la compréhension de leur fonction.

## api.py

Ce fichier contient l'implémentation de l'API FastAPI, avec les points de terminaison /customers, /orders et /products. L'API utilise des jetons JWT pour la protection des routes et communique avec une autre API externe pour obtenir les données.

### Points de terminaison
/customers: Retourne les données protégées pour les clients.
/orders: Retourne les données protégées pour les commandes d'un client spécifique.
/products: Retourne les données protégées pour les produits d'une commande spécifique appartenant à un client spécifique.

## secure.py

Ce fichier contient des fonctions pour générer et vérifier les jetons JWT, ainsi que pour hacher et vérifier les mots de passe à l'aide de la bibliothèque Argon2.

### Fonctions
generate_token(username: str) -> str: Génère un jeton JWT pour un nom d'utilisateur spécifique.
verify_jwt_token(authorization: str = Header(...)) -> TokenData: Vérifie un jeton JWT et extrait les données du jeton.
hash_pwd(pwd: str) -> str: Hache un mot de passe en clair à l'aide de la bibliothèque Argon2.
verify_pwd(user_pwd: str, hashed_pwd: str) -> bool: Vérifie si un mot de passe en clair correspond à un mot de passe haché à l'aide de la bibliothèque Argon2.

## test_api.py

Ce fichier contient des tests pour les points de terminaison de l'API et les fonctions de sécurité.

### Tests

test_customers(): Teste le point de terminaison /customers.
test_orders(): Teste le point de terminaison /orders.
test_products(): Teste le point de terminaison /products.
test_orders_invalid_customer_id(): Teste le point de terminaison /orders avec un ID client invalide.
test_products_invalid_ids(): Teste le point de terminaison /products avec des ID client et commande invalides.
test_invalid_token(): Teste les points de terminaison avec un jeton JWT invalide.

## test_secure.py

Ce fichier contient des tests pour les fonctions de génération et de vérification de jetons JWT, ainsi que pour les fonctions de hachage et de vérification des mots de passe.

### Tests
test_generate_and_verify_token(): Teste les fonctions generate_token() et verify_jwt_token().
test_hash_and_verify_password(): Teste les fonctions hash_pwd() et verify_pwd().

## run_tests.py

Ce fichier exécute les tests en utilisant la bibliothèque pytest et imprime les résultats.

## ci.yaml

Ce fichier contient la configuration pour GitHub Actions. Il définit un workflow qui est déclenché lorsqu'un commit est poussé ou lorsqu'une pull request est ouverte. Le workflow exécute les tests, puis déploie l'application sur Heroku si les tests réussissent.

## requirements.txt

Ce fichier liste les dépendances requises pour l'application. Vous devez installer ces dépendances pour exécuter l'application ou les tests.

Dépendances
psycopg2
datetime
pyjwt
argon2
pydantic
fastapi
fastapi.security
requests
uvicorn
pytest
httpx
argon2-cffi
Fichier 8: runtime.txt

Ce fichier spécifie la version de Python à utiliser pour l'application. Dans ce cas, il s'agit de Python 3.11.3.

## Procfile

Ce fichier indique à la plateforme Heroku comment démarrer l'application. Il spécifie la commande à exécuter pour démarrer l'application FastAPI à l'aide de Uvicorn.

### Commande

web: uvicorn api:app --host=0.0.0.0 --port=${PORT:-5000}

Cette commande démarre l'application FastAPI à l'aide de Uvicorn, en écoutant sur l'adresse 0.0.0.0 et en utilisant le port défini par la variable d'environnement PORT ou 5000 par défaut.

## Bibliothèques utilisées

Les bibliothèques utilisées dans ce projet sont :

fastapi
uvicorn
pydantic
argon2
requests
httpx
pyjwt
pytest
argon2-cffi

## Fonctionnalités du projet

1.Protection des données sensibles avec des tokens JWT  

2.Routes /customers, /orders et /products  

3.Fonctions d'authentification et de sécurité dans secure.py

4.Tests unitaires dans test_api.py et test_secure.py 

5.Déploiement automatique sur Heroku avec le fichier ci.yaml 

## Résumé

Cette application comprend plusieurs fichiers pour gérer l'API, la sécurité, les tests et le déploiement. L'API utilise FastAPI pour définir des points de terminaison protégés par des jetons JWT. Les fonctions de sécurité permettent de générer et de vérifier les jetons JWT, ainsi que de hacher et de vérifier les mots de passe. Les tests garantissent le bon fonctionnement de l'API et des fonctions de sécurité. La configuration de GitHub Actions permet d'exécuter les tests et de déployer l'application sur Heroku lorsque des modifications sont poussées ou lorsqu'une pull request est ouverte. Les dépendances nécessaires à l'application sont répertoriées dans requirements.txt, et la version de Python à utiliser est spécifiée dans runtime.txt. Enfin, le fichier Procfile indique à Heroku comment démarrer l'application.
