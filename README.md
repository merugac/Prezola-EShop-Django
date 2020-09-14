Installation to run in Local Host

Clone the repository
https://github.com/merugac/Prezola-EShop-Django/

Move into the repository
cd Prezola-EShop-Django/

Install the required packages
pip install -r requirements.txt

Make Migrations
python manage.py makemigrations
python manage.py migrate

Running Server
python manage.py runserver

open in browser http://127.0.0.1:8000/

Admin Panel Access: http://127.0.0.1:8000/admin
user: admin, psw: admin

Accessing the Database:

open https://sqliteonline.com/

Open File Menu > OpenDB > browse for db.sqlite3 file in Prezola-Django folder and runthe SQL commands to get data from database.

Application Code along with docker file for creating the docker image for EShop Application

Instruction for Creating the Docker Image and running the application in Docker conatiners is provided inthis read me file.

Note: Docker conatiner uses gunicorn python Web Server Gateway Interface HTTP server. 


# EShop

Build the Docker Image

docker build . -t eshop:1.0.0


# Check image

docker image ls

# Run Docker Images

docker run -ti -d -p 8000:8000 eshop:1.0.0


# Check docker container status

docker ps

# Access the application on port the docker host machines port 8000 


# Features:

SignUp to Create to User Account
Login page for Registered Users
Add/Remove Products
Add/Remove Product Categories
Add Products to Cart
Increase and Decrease Quantities
Cart Checkout
Placing Orders
Listing Orders
Uploading Product Images
Navbar added to Home Page
Listing Category in Home Page for filtering Products
Customer Form Submission & Redirection to Home Page after successful login by mapping in url
Form Validation
Email Validation to avoid duplication in registration
Storing products, categories, customers, sessions, users in database
Refactoring the code without changing its behavior
Password Hashing & Encryption using Hashers, makepassword and check password modules
session identifying requests from users by server
Creating cart object in session
Logout from the application





