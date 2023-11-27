# REST & JSON APIs

## Flask Cupcakes Exercise

This repository contains code for a Flask Cupcakes Exercise, on building a JSON API, perform testing using Insomnia, write integration tests, and create a simple HTML/JS frontend.

### Setup

  1. Create a virtual environment and install dependencies:
         python -m venv venv
         source venv/bin/activate
         pip install -r requirements.txt

  2. Initialize a Git repository:
          git init


### Development Steps


#### Part One: Cupcake Model

° Create the Cupcake model in models.py.
° Set up a cupcakes database.
° Run seed.py to add sample cupcakes.


#### Part Two: Listing, Getting & Creating Cupcakes

° Implement routes:
  ° GET /api/cupcakes: Get all cupcakes.
  ° GET /api/cupcakes/<cupcake-id>: Get a single cupcake.
  ° POST /api/cupcakes: Create a cupcake.
° Test using Insomnia.
° Run provided tests:
        python -m unittest -v tests


#### Part Three: Update & Delete Cupcakes

° Implement routes:
  ° PATCH /api/cupcakes/<cupcake-id>: Update a cupcake.
  ° DELETE /api/cupcakes/<cupcake-id>: Delete a cupcake.
° Test using Insomnia.


#### Part Four: Write More Tests

° Add tests for the PATCH and DELETE routes.


#### Part Five: Start on the Frontend

° Implement the GET /: route to return an HTML page.
° Use JavaScript (axios and jQuery) to:
  ° Query the API to get cupcakes and add them to the page.
  ° Handle form submission to inform the API about a new cupcake and update the page's cupcake list.


### Running the Application

1. Start the Flask application:
     flask run
2. Access the application in your browser at http://localhost:5000.


### Additional Notes

° Make sure your virtual environment is activated before running any commands.
° Inspect the browser console for any JavaScript errors.
° Ensure the Flask server is running when accessing the frontend.
° Refer to the provided code and comments for detailed explanations.
