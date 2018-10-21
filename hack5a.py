import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/serviceTypeList')
def serviceTypeList():
    return jsonify(
    {
        "id":1,
        "name": "Internet, telefone, TV a cabo",
        "imageName" : "Internet"
    },
    {
    	"id": 2,
    	"name": "Manutenção",
        "imageName" : "Maintenance"
    },
    {
    	"id": 3,
    	"name": "Chaves",
        "imageName" : "Keys"
    },
    {
    	"id": 4,
    	"name": "Seguro",
        "imageName" : "Assurance"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
