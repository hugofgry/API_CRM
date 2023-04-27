from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
import jwt
import uvicorn
import db

app = FastAPI()
security = HTTPBearer()

# Vos informations d'identification d'utilisateur, stockées dans un dictionnaire
users_db = {
    "john": "password123",
    "jane": "password456"
}

# Clé secrète pour signer les jetons JWT
SECRET_KEY = "votre_clé_secrète"

# Durée de validité du jeton (nous utilisons timedelta pour que nous puissions facilement ajouter ou soustraire du temps)
TOKEN_EXPIRATION_TIME = timedelta(days=7)


# Fonction pour générer un jeton JWT valide pour l'utilisateur donné
def generate_token(username: str) -> str:
    # Définir la date d'expiration du jeton
    expiration = datetime.utcnow() + TOKEN_EXPIRATION_TIME

    # Créer la charge utile pour le jeton JWT (nous incluons le nom d'utilisateur et la date d'expiration)
    payload = {"sub": username, "exp": expiration}

    # Créer le jeton JWT en signant la charge utile avec la clé secrète
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Retourner le jeton en tant que chaîne de caractères
    return token



# Endpoint pour la connexion

@app.get("/login")
async def login(username: str, password: str, token: str):

     pwd_in_db, token_in_db = db.get_user_token(username)

    # Vérifier que les informations d'identification sont valides
     if password != pwd_in_db or token!= token_in_db:
        raise HTTPException(status_code=401, detail="Nom d'utilisateur ou mot de passe incorrect")

     return "access to API ok"

@app.post("/create_user")
async def create_user(username: str, password: str, role: str):

    # Générer un jeton pour l'utilisateur
    token = generate_token(username)

    # Insérer l'user dans la db
    db.insert(username, password, role, token)


# Endpoint protégé par un jeton
@app.get("/data")
async def protected_data(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        # Extraire le jeton JWT de l'en-tête d'autorisation
        token = credentials.credentials

        # Décoder et vérifier le jeton JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        # Vérifier que le jeton n'a pas expiré
        expiration = datetime.fromtimestamp(payload["exp"])
        if datetime.utcnow() > expiration:
            raise HTTPException(status_code=401, detail="Le jeton d'authentification a expiré")

        # Renvoyer les données protégées
        return {"data": "Ceci sont des données protégées!"}

    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Jeton d'authentification invalide")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
