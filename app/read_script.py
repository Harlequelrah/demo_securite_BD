# Lecture des utilisateurs et déchiffrement des mots de passe
from database_con import db,cipher_suite
cursor = db.cursor()

cursor.execute("SELECT id, username, password FROM users")
for id, username, encrypted_password in cursor.fetchall():
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
    print(f"ID: {id}, Username: {username}, Password: {decrypted_password}")




# 5. Fermer la connexion
cursor.close()
db.close()
