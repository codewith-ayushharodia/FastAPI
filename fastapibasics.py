from fastapi import FastAPI
app = FastAPI()
a = [{"name":"Ayush","id":1},{"name":"Avika","id":2}]
@app.get("/")
def home():
    return "hello!"
@app.get("/con")
def contacts():
    return "contact me soon"
@app.get("/products")
def hello():
    return a

#path parameter
@app.get('/ayush/{id}')
def nike(id:int):
    for i in a:
        if i["id"] == id:
            return i
      
    return "nigga"

#query parameter
@app.get('/bhalu')
def bhalu(name:str):
    return f"How are you? {name}"