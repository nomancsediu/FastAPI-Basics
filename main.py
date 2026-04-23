from fastapi import FastAPI

app = FastAPI() # Create a FastAPI instance


@app.get("/") # Define a route for the root URL

# Define a function to handle requests to the root URL
def home():
    return "Welcome to the FastAPI application!"


@app.get("/contact") # Define a route for the contact page

# Define a function to handle requests to the contact page
def contact():
    return "You can connect us anytime!"