from src.config.mySql import get_mysql_connection

# Save metadata to MySQL
def save_documents_to_database(file,file_location,user_id):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    user_id = 1  # Placeholder, replace with actual user id if available
    insert_query = """
        INSERT INTO documents (file_name, user_id, file_location)
        VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (file.filename, user_id, str(file_location)))
    conn.commit()
    cursor.close()
    conn.close()