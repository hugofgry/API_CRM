# API_CRM

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
