# Checkout System

## Requirements

- Python 3.7 or higher
- `pytest/tox` for running tests

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/supermarket-checkout.git
    cd supermarket-checkout
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

## Using Pytest

To run tests in multiple environments using `tox`, follow these steps:

1. Install `tox`:

    ```sh
    pip install pytest
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
