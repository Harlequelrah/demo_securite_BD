from database_con import db_2,cipher_suite
cursor = db_2.cursor()

cursor.execute("SELECT id, username, password FROM users")
for id, username, encrypted_password in cursor.fetchall():
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
    print(f"ID: {id}, Username: {username}, Password: {decrypted_password}")


cursor.close()
db_2.close()
