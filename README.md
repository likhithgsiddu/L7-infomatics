# Chocolate House Application

## Overview
This application is designed to manage the seasonal flavor offerings, ingredient inventory, and customer flavor suggestions for a fictional chocolate house.

### Features:
- Manage seasonal flavors (add, list).
- Manage ingredient inventory (add, list).
- Capture customer suggestions and allergy concerns.

## Requirements
- Python 3.9+
- Docker (if using Docker to run the application)

## Setup Instructions

### Local Development
1. Clone the repository.
2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Use the application by modifying the `app.py` functions to add or retrieve data.

### Docker Build and Run
1. Build the Docker image:
    ```bash
    docker build -t chocolate-house-app .
    ```
2. Run the container:
    ```bash
    docker run --rm chocolate-house-app
    ```

### Testing the Application
1. Verify that the database tables are created when running the app.
2. Modify the `app.py` file to test different CRUD operations (add flavors, list flavors, etc.).
