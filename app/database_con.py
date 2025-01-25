import mysql.connector
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
load_dotenv()

# 1. Charger ou générer une clé de chiffrement
def load_or_generate_key():
    """Génère ou charge une clé de chiffrement dans le répertoire courant."""
    key_path="D:\\Programmation\\PY\\projects\\demo_securite_BD\\app\\secret.key"
    try:
        with open(key_path, "rb") as key_file:
            print(f"Clé chargée depuis {key_path}")
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        print(f"Nouvelle clé générée et enregistrée dans {key_path}")
        return key


key = load_or_generate_key()
cipher_suite = Fernet(key)

# 2. Connexion à la base de données
db = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)


