from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK', 200


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    body = request.get_json()
    print (body)
    return jsonify(
        {
    "fulfillmentMessages":[
        {
            "text": {
                "text": [
                    "Text response from webhook"
                ]
            }
        }

    ]

        }

    )