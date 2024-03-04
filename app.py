from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
            "name": "Chair",
            "price": 15.99
            }
        ]
        
    }
]


@app.get('/store') # 'http://12.7.0.0.1:5000/store'
def get_stores():
    return {"stores": stores}

@app.get('/test')
def get_stores():
    return "<h1>LAB 2 <strong/>Finish</h1>"
