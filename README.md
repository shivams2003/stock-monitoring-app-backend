
# Stock Monitoring App

This repository contains a stock monitoring application with a backend built using Django and a frontend built using React. The application allows users to register, log in, view their watchlist, and see a dashboard of stock prices. The backend uses MongoDB for data storage.


## Table of Contents

- Features
- Setup Instructions
    - Prerequisites
    - Backend Setup
    - Frontend Setup
- Environment Variables
- Usage
- Technologies Used

## Features

- User registration and authentication
- View and manage stock watchlist
- Stock price dashboard
- Persistent user sessions
## Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- MongoDB (Atlas or local instance)
## Backend setup
 - Clone the repository
 ```http
  git clone https://github.com/your-username/stock-monitoring.git
  cd stock-monitoring/backend
```
- Create a virtual environment:
```http
  python -m venv venv
```
- Activate the virtual environment:
    - Windows
    ```http
        venv\Scripts\activate
    ```
    - macOS
    ```http
        source venv/bin/activate
    ```
- Install the dependencies    
    ```http
  pip install -r requirements.txt
    ```
- Set up environment variables:

    ```http
    SECRET_KEY="your-secret-key"
    DEBUG=True
    ALLOWED_HOSTS="localhost,127.0.0.1"
    CORS_ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"

    # MongoDB Settings
    MONGODB_URI="your-mongodb-uri"
    MONGO_DB_NAME="stock_monitoring"
    DB_PORT="27017"
    DB_USER="your-db-user"
    DB_PASSWORD="your-db-password"

    ```

- Run migrations:
    ```http
    python manage.py migrate
    ```    
- Start the backend server:
    ```http
    python manage.py runserver

    ```    
    
## Frontend setup
 - Navigate to Frontend directory
    ```http
    cd ../frontend
    ```
  - Install the dependencies:
    ```http
    npm install
    ```   
  - Start the frontend development server:
    ```http
    npm start
    ```  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- SECRET_KEY: A secret key for Django.
- DEBUG: Set to True for development.
- ALLOWED_HOSTS: A comma-separated list of allowed hosts.
- CORS_ALLOWED_ORIGINS: A comma-separated list of allowed origins for CORS.
- MONGODB_URI: The URI for connecting to MongoDB.
- MONGO_DB_NAME: The name of the MongoDB database.
- DB_PORT: The port for connecting to MongoDB.
- DB_USER: The MongoDB username.
- DB_PASSWORD: The MongoDB password
## Usage

- Register: Create a new user account.
- Login: Log in to your account.
- Watchlist: View and manage your stock watchlist.
- Dashboard: View stock prices in a dashboard.



## Tech Stack
**Backend**: Django, Django REST Framework, MongoDB, mongoengine
**Frontend**: React, Material-UI, Axios


