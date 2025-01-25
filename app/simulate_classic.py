# simulate_classic.py

from database_con import db, cipher_suite


cursor = db.cursor()

# Fonction pour simuler l'attaque classique
def simulate_classic_attack():
    print("Simulation d'une attaque classique : interception de la clé")

    # L'attaquant "intercepte" la clé et tente de déchiffrer
    cursor.execute("SELECT id, username, password FROM users")
    for id, username, encrypted_password in cursor.fetchall():
        try:
            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
            print(f"ID: {id}, Username: {username}, Password: {decrypted_password}")
        except Exception as e:
            print(f"Erreur de déchiffrement pour {username}: {str(e)}")

# Simuler l'attaque classique
simulate_classic_attack()

# 5. Fermer la connexion
cursor.close()
db.close()
