from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

con = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password= 'root',
    database= 'pandeyji_eatery'
)

@app.route('/getTable', methods=['GET'])
def get_tables():
    cursor=con.cursor()
    cursor.execute("SHOW TABLES;")
    tables=cursor.fetchall()
    cursor.close()
    con.close()
    table_names=[table[0] for table in tables]
    return jsonify({"tables":table_names}),200


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    body = request.get_json(force = True)
    print('hi')
    print (body)
    return jsonify(
        {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "This response is from webhook"
                        ]
                    }
                }

            ]

        }

    )

if __name__=="__main__":
    print("connecting to DB...")
    app.run(debug=True)
