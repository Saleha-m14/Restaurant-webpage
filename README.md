# **Yummy Restaurant**


![View the Yummy Restaurant Homepage](images/main-image.png)

This is my fourth project in [Code Institute](https://codeinstitute.net/de/) that is a for a Yummy fictional resturant. It is a very good place where people can go and eat the most delicious foods in Berlin, Germany. The customer can view the menu items and this webpage allows the user to sign in or sign up and book a table online and view the bookings to edit or delete them.

[View the live project here!](https://yummy-restaurant-webpage-6c0b2e074e4b.herokuapp.com/)


[View the Github repository](https://github.com/Saleha-m14/Restaurant-webpage)


# **Table of Contents**

- [**Yummy Restaurant**](#yummy-restaurant)
- [**Table of Contents**](#table-of-contents)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Frameworks, Libraries \& Tools](#frameworks-libraries--tools)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Deploying with heroku](#deploying-with-heroku)


## Project Goals

The main goal for this project is to create a webpage for the customers of Yummy Restaurant that eligibles the user to view the restaurant webpage click on the book a table button and easily reserve a table. The user can view the bookings, edit and delete them.

## User Stories

- ### Administrator
  -  As a website admin I can log in to admin panel using the super user.
  -  As a website admin I can view the bookings and make changes to it.
  -  As a website admin I can edit or delete the bookings.


 -  ### First Time User
    -  As a first time user I want to view the Yummy Restaurant webpage and see information about resturant.
    -  As a first time user I can see the menu items to know which kinds of foods I can eat at this restaurant.
    -  As a first time user, I want to see some photos of restaurant.
    -  As a first time user I want to be able to find the relevant information to know how to contact with this restaurant.
    -  As a first time user I want to be able to book a table online bcause I want to be sure that there is an empty table for me.

 -  ### Frequent User
    - As a returning user I can create and log in it to see my bookings
    - As a returning user I can see my bookings.
    - As a reaturning user I can edit or delete bookings that I have made previously.

- ### Returning User

    -  As a returning user I want to be able to sign in and manage my bookings.
    -  As a returning user I want to be able to make changes to my current booking or cancel it.
    -  As a returning user I want to edit or delete my bookings.

- ### Agile Methodology

The user stories are added to project as [issues in the Github](https://github.com/Saleha-m14/Restaurant-webpage/issues) and are prioritzed using lables. The [Kanban Board](<https://github.com/users/Saleha-m14/projects/3>) is used to implement Agile in this project. This way I have devided all tasks and managed to complete the project.


-  ### Design
 I have used a bootstrap free template for this project that was created for a restaurant webpage.
 The template name is Deliscious and the author is bootstrapmade.com
  - Template Name: Delicious
  - Updated: Sep 18 2023 with Bootstrap v5.3.2
  - Template URL: <https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/>
  - Author: BootstrapMade.com
  - License: <https://bootstrapmade.com/license/>
 [Bootstrap restaurant template](https://bootstrapmade.com/demo/Restaurantly/)

## Features

  - ### Future Features
    - As a future feature the user will be able to order food  from the menu items.
    - As a future feature I want to add some more foods to the menu.
    - As a future featura I want to add special offers for the customers.
  
## Frameworks, Libraries & Tools

  -  [**Heroku**](https://dashboard.heroku.com/apps) is used for deploying this project
- [**Github**](https://github.com/) is used to store the project.
- [**Codeanywhere**](https://codeanywhere.com/) is used as a development environment. 
- [**Django**](https://docs.djangoproject.com/) that is a python framework.
- [**Cloudinary**](https://cloudinary.com/)is used for media and static files.
- [**Database-URL**](https://pypi.org/project/dj-database-url/0.5.0/)is used to represent database settings
- [**Gunicorn**](https://pypi.org/project/gunicorn/20.1.0/) is used to run Django on heroku.
- [**Psycopg2**](https://pypi.org/project/psycopg2/2.9.3/) to connect Postgre SQL
- [**Bootstrap**](https://getbootstrap.com/) used for the frontend
- [**allauth**](https://docs.allauth.org/en/latest/release-notes/recent.html)
- [**Am I responsive**](https://ui.dev/amiresponsive) is used to check if the website is responsive to different devices.
- [**Github issues & Kennan Board**](https://github.com/users/Saleha-m14/projects/3/views/1) is used to track the progress of the project.

## Testing

   - ### Bugs
     - #### Fixed Bugs

| Bug | Solution | Status |
| ---| ---| ---|
|The Success and error messages were not displaying | I had forgotten to add an html template for displaing the message. The issue were solved by adding the HTML template for messages. | Fixed |
|There was not any success or error message after booking a table | I removed the message HTML template from booking page and added to manage bookings page because the user was redirected to managebooking after reservation. | Fixed |
| When the user filled in the booking form and clicked submit button nothing was happening due to an error. | I removed the validate.js that was comming from bootrstrap template that I used and the issue were solved. | Fixed |

    
- #### Remaining Bugs


## Deployment

### Github Deployment

    -  Login to your github account and navigate to your repositories and click on New.
    -  Select a template(the Code Institute full template is used for this project).[Code-Institute-Org/python-essentials-template](https://github.com/Code-Institute-Org/p3-template)
    -  Write a name for your repository
    -  Select public
    -  Click on create to create your repository.
    -  Copy the link of your repository
    -  log in to your cloudinary using github
    -  click on crete new workspace and paste the github url.
    -  Run the commands first "git add .", then "git commit -m "commit message" and finally "git push" to push the files to github.


### Deploying with heroku

This project is deployed using [Heroku](https://id.heroku.com/) and following the instruction of deployment video of Course Institue. These are the deployment steps:

    1. Open Heroku and click on "Create New App".
    2. Write your app name and select region. You should give your app a unique name.
    3. On the new page click on "settings" and select Config Var, type PORT in key with a value of 8000.

    4. Click "Add buildpack", select Python and click "Save Changes".
    5. Select NodeJS and click save again. The order is important the Python should be on the top of NodeJS.
    6. Click on "Deploy" tab.
    7. Select "Github" as deployment method.
    8. Search for your repository name and click connect.
    9. Make sure that "main" branch is selected and click on "Enable Automatic Deploys" then, click on "Deploy Branch".
    10. When your project is deployed you can open it simply by clicking "View".

