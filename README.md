# Credit Guard
Credit Guard is a Python-based application designed to help manage and secure credit card information. This application provides three main functionalities, card creation, card number validation and retriving cards list based on card's user-creator. I think the problem was ambiguous with it's requirements for the CardViewSet so I wrote it two different ways, therefore there are also two serializers, one for each viewset, also two different URLs, one with DefaultRouter and other as regular url.

## App Features
- **User Management:** Add, update, and delete user information.
- **Card Number Validation:** This project validates credit card number with an algorithm that is a variant of the broader concept of modular exponentiation.
- **Credit Card Management:** Store, retrieve, and manage credit card details securely.

## Installation

- Clone the repository:
```
git clone https://github.com/onise2001/credit_guard.git

``` 
- Navigate to the project directory:
```
cd credit_guard
```

- Create a virtual environment:
```
python -m venv venv
```

- Install the required modules:
```
pip install -r requirements.txt
```
## Usage

- Start the application with:
```
python manage.py runserver
```
-  **Authentication**
This project uses JSON Web Tokens for registration and login purposes.

- **Registration:** By sending a POST request to this api endpoint, ```/auth/signup/``` , with correct request body, a new User will be created and    added to the database.

- **Login:** By sending a POST request to this api endpoint, ```/auth/login/``` , with correct request body, you will get an Authorization Token.

- **Users have following fields:**
- Username
- Email
- Password

- **Card creation and listing:**

- **Create:** By sending a POST request to this api endpoint, ```/cards/``` , with correct request body, a new Card will be created and added to the database.
- **List:** By sending a GET request to this api endpoint, ```/cards/``` , you will get a list of cards that you created.





