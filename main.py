from fastapi import FastAPI, Request
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


'''
When use Path Params and When Use Query Params, the main difference is in how the parameters are passed in the URL.

Path Params are part of the URL path and are defined using curly braces {} in the route. 
They are used to identify a specific resource. For example, in the route /products/{product_id}, the product_id is a path parameter that identifies a specific product.

Query Params are passed as key-value pairs in the URL after a question mark ?. 
They are used to filter or sort data. For example, in the route /greet?name=John&age=30, name and age are query parameters that provide additional information for the greeting.
'''


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


# Query Params...
# @app.get("/greet") # Define a route for the /greet URL
# def greet_user(name:str,age:int):
#     return f"Hello, {name}! You are {age} years old."


#Query Params...
@app.get("/greet")
# Short hand way to get query parameters using Request object
def greet_user(request: Request):
    name = request.query_params.get("name")
    age = request.query_params.get("age")
    return f"Hello, {name}! You are {age} years old."