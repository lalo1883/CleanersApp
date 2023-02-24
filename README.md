API Documentation for Cleaners
This API allows for the management of cleaning personnel, allowing for the creation, reading, updating, and deletion of data for registered workers.

Requirements
In order to run the code for this API, the following dependencies must be installed:

FastAPI
Pydantic
Uvicorn
Starlette
All of these dependencies can be installed using the requirements.txt file included in the repository with the following command:

pip install -r requirements.txt

Usage
To use the API, run the main.py file with the following command:

uvicorn main:app --reload

Once the server is running, the different endpoints of the API can be accessed using an HTTP client such as Postman.

Endpoints
The API has the following endpoints:

GET /: Returns a simple HTML page that displays the message "Hello world".

GET /cleaners: Returns a JSON that contains all the data of the registered workers.

GET /cleaners/{id}: Returns a JSON that contains the data of a specific worker, identified by the id parameter.

GET /cleaner/?city=xxx: Returns a JSON that contains all the registered workers who work in the city specified by the city parameter.

GET /cleaners/zone/{zone}: Returns a JSON that contains all the registered workers who work in the zone specified by the zone parameter.

POST /cleaner/: Creates a new cleaning worker and adds them to the list of registered workers.

PUT /cleaner/{id}: Updates the data of a specific worker, identified by the id parameter.

DELETE /cleaner/{id}: Deletes a specific worker, identified by the id parameter.

Each endpoint has a tag indicating which group the endpoint belongs to, allowing for grouping of endpoints in the documentation.

Parameters
Endpoints that accept parameters have validation using the Pydantic Field module and FastAPI's Path and Query decorators. The validations include:

For id: The parameter must be an integer between 0 and 2000.

For city and zone: The parameter must have a minimum length of 5 characters and a maximum length of 15.

Contributions
Contributions to this API are welcome. To suggest changes or improvements, please submit a pull request or create an issue in the repository.