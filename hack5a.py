import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/serviceTypeList')
def serviceTypeList():
    return jsonify(
    {
        "id": 1,
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

@app.route('/availableServicesForInternet')
def availableServicesForInternet():
    return jsonify(
     {
        "connectionSpeed" : "TIM 40 MB",
        "offers" : [
            {
                "id" : 1,
                "name" : "NET",
                "price" : 59.99
            },
            {
                "id" : 2,
                "name" : "Vivo",
                "price" : 125.00
            },
            {
                "id" : 3,
                "name" : "TIM",
                "price" : 105.00
            }
        ]
     },
     {
         "connectionSpeed" : "VIVO 60 MB",
         "offers" : [
             {
                 "id" : 1,
                 "name" : "NET",
                 "price" : 79.00
             },
             {
                 "id" : 2,
                 "name" : "Vivo",
                 "price" : 145.00
             },
             {
                 "id" : 3,
                 "name" : "TIM",
                 "price" : 105.80
             }
         ]
     },
     {
         "connectionSpeed" : "TIM 100 MB",
         "offers" : [
             {
                 "id" : 1,
                 "name" : "NET",
                 "price" : 79.00
             },
             {
                 "id" : 2,
                 "name" : "Vivo",
                 "price" : 165.00
             },
             {
                 "id" : 3,
                 "name" : "TIM",
                 "price" : 97.50
             }
         ]
     },
     {
         "connectionSpeed" : "VIVO 200 MB",
         "offers" : [
             {
                 "id" : 1,
                 "name" : "NET",
                 "price" : 139.00
             },
             {
                 "id" : 2,
                 "name" : "Vivo",
                 "price" : 185.00
             },
             {
                 "id" : 3,
                 "name" : "TIM",
                 "price" : 120.00
             }
         ]
     })

@app.route('/servicesListForPhone')
def servicesListForPhone():
    return jsonify(
     {
         "id" : 1,
         "name" : "Fixo Local",
         "price" : 99.00
     },
     {
         "id" : 2,
         "name" : "Fixo + Móvel Local",
         "price" : 129.00
     },
     {
         "id" : 3,
         "name" : "Fixo + Móvel Brasil",
         "price" : 149.00
     })

@app.route('/servicesListForTV')
def servicesListForTV():
    return jsonify(
     {
         "id" : 1,
         "name" : "Mix HD",
         "price" : 59.00,
         "channels" : "222 canais"
     },
     {
         "id" : 2,
         "name" : "Fácil HD",
         "price" : 79.99,
         "channels" : "112 canais"
     },
     {
         "id" : 3,
         "name" : "Top HD",
         "price" : 139.99,
         "channels" : "259 canais"
     })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
