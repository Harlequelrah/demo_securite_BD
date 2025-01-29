from database_con import db_1,cipher_suite
cursor = db_1.cursor()

def insert_user(id, username, password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    insert_query = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (id, username, encrypted_password))
    db_1.commit()
    print(f"Utilisateur {username} inséré avec succès.")


insert_user(1, "alice", "wakawaka")
insert_user(2, "bob", "bakabaka")


cursor.close()
db_1.close()
