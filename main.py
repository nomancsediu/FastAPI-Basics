from fastapi import FastAPI
from mockData import products

app = FastAPI() # Create a FastAPI instance


@app.get("/") # Define a route for the root URL

# Define a function to handle requests to the root URL
def home():
    return "Welcome to the FastAPI application!"


@app.get("/products") # Define a route for the /products URL

# Define a function to handle requests to the /products URL
def get_products():
    return products


#Path Params...
# Define a route for the /products/{product_id} URL, where {product_id} is a path parameter
@app.get("/products/{product_id}")
def get_one_products(product_id: int):

    # Loop through the products to find the one with the matching id
    for oneProduct in products:
        if oneProduct["id"] == product_id:
            return oneProduct

    return {
        "error": "Product not found"
    }


#Query Params...
@app.get("/greet") # Define a route for the /greet URL
def greet_user(name:str,age:int):
    return f"Hello, {name}! You are {age} years old."
