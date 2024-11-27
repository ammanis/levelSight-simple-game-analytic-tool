API Reference
=============

Available Endpoints
-------------------
- **`/upload`**: Upload player logs.
- **`/analyze`**: Generate insights and return a JSON response.
- **`/export`**: Export data in CSV or JSON format.

Example Usage
-------------
To interact with the API, you can use Python's `requests` library:

.. code:: python

    import requests

    # Example request to the analyze endpoint
    response = requests.post("http://localhost:8000/analyze", data={"game_id": "1234"})

    # Print the JSON response
    print(response.json())
