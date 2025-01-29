

from database_con import db_1, cipher_suite


cursor = db_1.cursor()


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


simulate_classic_attack()

cursor.close()
db_1.close()
