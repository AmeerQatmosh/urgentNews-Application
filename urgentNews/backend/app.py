from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

@app.route('/getUrgentNews', methods=['GET'])
def get_urgent_news():
    connection = pymysql.connect(
        host='database',
        user='root',
        password='password',
        database='urgentnews'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM News ORDER BY id DESC LIMIT 10')
    results = cursor.fetchall()
    news = [{'title': row[1], 'content': row[2]} for row in results]
    connection.close()
    return jsonify(news)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
