# Math Utility Functions

This repository contains a simple Python module (`math_utils.py`) that provides basic arithmetic operations: addition, subtraction, multiplication, and division. It's designed to be straightforward, type-hinted, and includes basic error handling for division.

## Project Description

The `math_utils.py` file offers a set of fundamental mathematical functions:
-   `add(a: float, b: float) -> float`: Returns the sum of two numbers.
-   `subtract(a: float, b: float) -> float`: Returns the difference between two numbers.
-   `multiply(a: float, b: float) -> float`: Returns the product of two numbers.
-   `divide(a: float, b: float) -> float`: Returns the result of dividing `a` by `b`. It raises a `ValueError` if `b` is zero.

Each function is equipped with type hints and a clear docstring, promoting code readability and maintainability.

## Installation

To set up the project and its testing environment, follow these steps:

1.  **Save the `math_utils.py` file:**
    Ensure the provided Python code is saved as `math_utils.py` in your desired project directory.

2.  **Create a virtual environment (recommended):**
    Open your terminal or command prompt, navigate to your project directory, and run:
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install pytest:**
    With your virtual environment activated, install the `pytest` testing framework:
    ```bash
    pip install pytest
    ```

## How to Run Tests

Once you have installed `pytest` and activated your virtual environment, you can run the tests for the `math_utils.py` module.

1.  **Place the test file:**
    Save the generated `test_math_utils.py` file in the *same directory* as `math_utils.py`.

2.  **Execute tests:**
    Ensure you are in the project's root directory (where both `math_utils.py` and `test_math_utils.py` are located). Then, run:
    ```bash
    pytest
    ```
    This command will automatically discover and execute all tests within `test_math_utils.py`.

3.  **For more verbose output:**
    To see detailed information about each test and its outcome, use the `-v` flag:
    ```bash
    pytest -v
    ```