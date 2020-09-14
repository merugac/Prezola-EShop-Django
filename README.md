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

## Improvements

Implementing Inventory Management

Generating Invoices

Integrating web app with social media.

Custom dashboard for end users with custom look and feel.

Developing Rich Fornt end UI application behaviour with JavaScript and CSS framworks and navigation links to other pages

Add Child Page Buttons to drilldown further

Developing Django models, views and forms with a particular emphasis in improving the experience of end-users.

Defyning how to register the models with the admin site. & modified versions of admin panel

site-specific settings, urls, models, views, and templates.

Defyning Models Creating database tables for the application using Django models. 

Django ORM to query the database and filter through results.

Sessions Framework adding a session-based visit-counter to the home page.

User Authentication & Permissions Email and Password Reset we can use email to send a password reset link to a user so that the user can reset their password

Payment gateway is the part of the checkout page that collects the customer’s billing information and sends it to the payment 
processing which was selected on various factors like supported cards, payment methods, security features, monthly fees, fee per txn..

Django web application security Protecting user data & design Django's built-in protections to handle security threats

Implementing Chatbot Agent to address user queries and product information 

Multi Lingual & supporting Multi Currencies

Coupoun Management

And many more.....
