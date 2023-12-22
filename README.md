# Card Status API

Card Status API is a Flask-based web application that provides an internal API to query the status of a user's card based on the provided phone number or card ID.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Loading Data](#loading-data)
  - [Running the Application](#running-the-application)
  - [API Endpoint](#api-endpoint)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (3.8 or later)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/card-status-api.git
    cd card-status-api
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Loading Data

To load data from CSV files into the database, uncomment the line in `app.py`:

```python
# Uncomment the line below to load data into the database
# load_data()
Then run the application once to load the data:

bash
Copy code
python app.py
Running the Application
Run the Flask application:

bash
Copy code
python app.py
By default, the application will be accessible at http://127.0.0.1:5000/.

API Endpoint
The application provides an endpoint for querying the card status:

Endpoint: /get_card_status
Method: GET
Parameters:
input: User's phone number or card ID
Example Request:
bash
Copy code
curl http://127.0.0.1:5000/get_card_status?input=ZYW8890
Example Response:
json
Copy code
{
  "card_id": "ZYW8890",
  "user_contact": "534534534",
  "timestamp": "14-11-2023 12:00 PM",
  "status_type": "returned",
  "comment": null
