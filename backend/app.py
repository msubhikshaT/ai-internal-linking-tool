from flask import Flask, request, jsonify
from crawler import crawl_page
import psycopg2

app = Flask(__name__)

# Database connection
def connect_db():
    return psycopg2.connect(
        host="5434",
        database="AI-Internal-Linking-Tool",
        user="postgres",
        password="abc123"
    )

# API Route to Crawl a Page
@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    page_data = crawl_page(url)

    return jsonify(page_data)

# API Route to Get Stored Pages
@app.route('/pages', methods=['GET'])
def get_pages():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT url, title FROM pages")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
