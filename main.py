from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():
    return{"data":{"name":"ammu"}}
@app.get("/about")
def about_section():
    return{"data":"displaying about page"}
