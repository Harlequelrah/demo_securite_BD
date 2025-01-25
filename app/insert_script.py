from database_con import db,cipher_suite
cursor = db.cursor()
# 3. Fonction pour insérer des utilisateurs avec chiffrement
def insert_user(id, username, password):
    encrypted_password = cipher_suite.encrypt(password.encode())  # Chiffrement
    insert_query = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (id, username, encrypted_password))
    db.commit()
    print(f"Utilisateur {username} inséré avec succès.")

# 4. Insérer des utilisateurs
insert_user(1, "alice", "wakawaka")
insert_user(2, "bob", "bakabaka")
# 5. Fermer la connexion
cursor.close()
db.close()
