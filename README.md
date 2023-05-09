### API_CRM

## Suite de tests pour l'API

Cette suite de tests est conçue pour tester une API fonctionnant sur http://127.0.0.1:8080. Elle effectue une série de tests pour vérifier la justesse et le comportement attendu des différentes routes de l'API. Les tests utilisent la bibliothèque httpx pour effectuer des requêtes HTTP et pytest pour les assertions.

### Configuration

Le script récupère le token d'authentification à partir d'une variable d'environnement nommée TOKEN.

### Tests effectués

test_customers: Vérifie si la route /customers retourne un code de statut HTTP 200 avec le token d'authentification valide.
test_orders: Vérifie si la route /orders retourne un code de statut HTTP 200 pour un identifiant de commande valide.
test_products: Vérifie si la route /products retourne un code de statut HTTP 200 pour des identifiants de client et de commande valides.
test_orders_invalid_customer_id: Vérifie si la route /orders retourne un code de statut HTTP 200 et un message d'erreur approprié pour un identifiant de client invalide.
test_products_invalid_ids: Vérifie si la route /products retourne un code de statut HTTP 200 et un message d'erreur approprié pour des identifiants de client et de commande invalides.
test_invalid_token: Vérifie si les routes /customers, /orders, et /products retournent un code de statut HTTP 401 pour un token d'authentification invalide.

## Suite de tests pour la sécurité

Ce code Python contient deux fonctions de test unitaires qui testent la fonctionnalité de génération de jeton et de hachage de mot de passe, ainsi que leur vérification.

La fonction generate_token(username) génère un jeton JWT à partir du nom d'utilisateur fourni. Le jeton est généré en utilisant la clé secrète définie dans le fichier secure.py.

La fonction verify_jwt_token(token) vérifie le jeton JWT fourni. Si le jeton est valide, la fonction renvoie les données du jeton. Sinon, la fonction renvoie une erreur.

La fonction hash_pwd(password) hache un mot de passe en utilisant l'algorithme de hachage SHA-256. Le mot de passe haché est stocké dans la base de données pour l'authentification ultérieure.

La fonction verify_pwd(password, hashed_password) vérifie qu'un mot de passe en clair correspond à un mot de passe haché. Elle utilise l'algorithme SHA-256 pour hacher le mot de passe en clair et le compare avec le mot de passe haché stocké dans la base de données.

Le code contient également deux fonctions de test unitaires:

test_generate_and_verify_token() teste la fonction generate_token(username) en vérifiant que le jeton généré peut être vérifié correctement en utilisant la fonction verify_jwt_token(token). La fonction vérifie également que les données du jeton contiennent le nom d'utilisateur fourni.

test_hash_and_verify_password() teste la fonction hash_pwd(password) en vérifiant que le mot de passe haché est vérifié correctement en utilisant la fonction verify_pwd(password, hashed_password). La fonction vérifie également que le mot de passe incorrect ne correspond pas au mot de passe haché.

Les tests unitaires sont exécutés à l'aide du framework de test unitaire Python pytest. Le framework pytest permet d'exécuter les tests de manière isolée, avec une configuration minimale, en utilisant les assertions pour vérifier que les résultats attendus sont corrects.


## Authentification et gestion des mots de passe

Ce module fournit des fonctions pour gérer l'authentification et les mots de passe en utilisant JWT (JSON Web Tokens) et Argon2.

### Classes

#### TokenData
Modèle Pydantic pour la représentation des données du jeton.

Attributs :

sub: str
### Fonctions

#### generate_token(username: str) -> str
Génère un jeton JWT signé contenant le nom d'utilisateur.

Arguments :

username : Nom d'utilisateur à inclure dans le jeton.
Retourne :

token : Jeton JWT signé en tant que chaîne de caractères.
#### verify_jwt_token(authorization: str = Header(...)) -> TokenData
Vérifie si un jeton JWT est valide et extrait les données du jeton.

Arguments :

authorization : Chaîne d'autorisation contenant le jeton JWT.
Retourne :

token_data : Objet TokenData contenant les données extraites du jeton.
Lève :

HTTPException : Exception levée si le jeton JWT est invalide.
#### hash_pwd(pwd: str) -> str
Hash un mot de passe en utilisant Argon2.

Arguments :

pwd : Le mot de passe en clair à hasher.
Retourne :

hashed_pwd : Le mot de passe hashé.
##### verify_pwd(user_pwd: str, hashed_pwd: str) -> bool
Vérifie si un mot de passe en clair correspond au mot de passe hashé.

Arguments :

user_pwd : Le mot de passe en clair fourni par l'utilisateur.
hashed_pwd : Le mot de passe hashé stocké.
Retourne :

bool : True si les mots de passe correspondent, sinon False.
