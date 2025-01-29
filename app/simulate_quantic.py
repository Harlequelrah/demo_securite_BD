

import random
from cryptography.fernet import Fernet
from database_con import db_2, cipher_suite

cursor = db_2.cursor()

# 1. Générer ou charger la clé
def load_or_generate_key():
    key_path = "secret.key"
    try:
        with open(key_path, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key


def simulate_quantum_attack():
    print("Simulation d'une attaque quantique : tentative de manipulation de la clé")

    # L'attaquant tente d'intercepter la clé et de perturber les données
    cursor.execute("SELECT id, username, password FROM users")
    for id, username, encrypted_password in cursor.fetchall():
        try:
            # Perturbation simulée : ajout de bruit dans les données
            print("Tentative de manipulation des données...")
            if random.choice([True, False]):
                print("Perturbation des données détectée!")
                encrypted_password = b"wrong data"  # Données altérées

            # Tentative de déchiffrement
            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
            print(f"ID: {id}, Username: {username}, Password: {decrypted_password}")

        except Exception as e:
            print(f"Erreur de déchiffrement pour {username}: {str(e)}")
            print("Erreur de déchiffrement : la clé a été compromise ou l'attaque a échoué.")


simulate_quantum_attack()


cursor.close()
db_2.close()
