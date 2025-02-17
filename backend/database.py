import psycopg2

# Database connection function
def connect_to_db():
    return psycopg2.connect(
        host="5434",        
        database="AI-Internal-Linking-Tool",   
        user="postgres",          
        password="abc123"  
    )

# Function to insert crawled data into the database
def insert_page_data(url, title, body_text):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to insert page data
        query = "INSERT INTO pages (url, title, body_text) VALUES (%s, %s, %s)"
        cursor.execute(query, (url, title, body_text))

        # Commit transaction
        connection.commit()

        print(f"Inserted: {url}")

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
