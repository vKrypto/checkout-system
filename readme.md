# Checkout System

## Requirements

- Python 3.8 or higher
- `pytest/tox` for running tests

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/vKrypto/checkout-system.git
    cd checkout-system
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run:
    ```sh
    uvicorn main:app
    ```

## Using Docker
To build and run the Docker container:

1. Build the Docker image:
    ```sh
    docker build -t checkout-system .
    ```

2. Run the Docker container::
    ```sh
    docker run --rm -p 8000:8000 checkout-system
    ```

## Run API:
API will be available at POST: 127.0.0.1:8000/checkout



## Using Black:
1. install black:
    ```sh
    pip install black
    ```

2. Run Black to format code::
    ```sh
    black .
    ```

## Using Pytest

To run tests using pytest, follow these steps:

1. Install `pytest`:

    ```sh
    pip install pytest pytest-mock
    ```

2. Run `tox`:

    ```sh
    pytest
    ```


## Using Tox

To run tests in multiple environments using `tox`, follow these steps:

1. Install `tox`:

    ```sh
    pip install tox
    ```

2. Run `tox`:

    ```sh
    tox
    ```
