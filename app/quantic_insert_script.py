from database_con import db_2,cipher_suite
cursor = db_2.cursor()

def insert_user(id, username, password):
    encrypted_password = cipher_suite.encrypt(password.encode())  # Chiffrement
    insert_query = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (id, username, encrypted_password))
    db_2.commit()
    print(f"Utilisateur {username} inséré avec succès.")


insert_user(1, "alice", "wakawaka")
insert_user(2, "bob", "bakabaka")

cursor.close()
db_2.close()
