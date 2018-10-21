import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def hack5a():
    if request.headers.get('Authorization') == '40':
        return jsonify({"40": "A vingança nunca é plena, mata a alma e envenena."})
    return jsonify({"message": "4040404040"})

@app.route('/1')
def hack5a():
    if request.headers.get('Authorization') == '30':
        return jsonify({"30": "A vingança nunca é plena, mata a alma e envenena."})
    return jsonify({"message": "3030303030"})

@app.route('/2')
def hack5a():
    if request.headers.get('Authorization') == '20':
        return jsonify({"20": "A vingança nunca é plena, mata a alma e envenena."})
    return jsonify({"message": "2020202020"})

@app.route('/3')
def hack5a():
    if request.headers.get('Authorization') == '10':
        return jsonify({"10": "A vingança nunca é plena, mata a alma e envenena."})
    return jsonify({"message": "1010101010"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
