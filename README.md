# **Yummy Restaurant**


![View the Yummy Restaurant Homepage](images/main-image.png)

This is my fourth project in [Code Institute](https://codeinstitute.net/de/) that is a for a Yummy fictional resturant. It is a very good place where people can go and eat the most delicious foods in Berlin, Germany. The customer can view the menu items and this webpage allows the user to sign in or sign up and book a table online if the customer wanted to do so.

[View the live project here!]()


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

The main goal for this project is to create a webpage for the customers of Yummy Restaurant that eligibles the user to view the menu item and book a table online.

## User Stories

- ### Administrator
  -  As a website admin I can log in to admin panel using the super user.
  -  As a website admin I can view the bookings and make changes to it.


 -  ### First Time User
    -  As a first time user I want to view the Yummy Restaurant webpage and see information about resturant.
    -  As a first time user I can see the menu items to know which kinds of foods I can eat at this restaurant.
    -  As a first time user I want to be able to find the relevant information to know how to contact with this restaurant.
    -  As a first time user I want to be able to book a table online bcause I want to be sure that there is an empty table for me.

 -  ### Frequent User
    - As a returning user I can create and log in it to see my bookings
    - As a returning user I can see my bookings.

- ### Returning User

    -  As a returning user I want to be able to sign in and manage my bookings.
    -  As a returning user I want to be able to make changes to my current booking or cancel it.

- ### Agile Methodology

The user stories are added to project as [issues in the Github](https://github.com/Saleha-m14/Restaurant-webpage/issues) and are prioritzed using lables. The [Kanban Board](<https://github.com/users/Saleha-m14/projects/3>) is used to implement Agile in this project.


-  ### Design


## Features

  - ### Future Features
    - As a future feature the user will be able to order food  from the menu items.
    - As a future feature I want to add some more foods to the menu.
  
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

## Testing

   - ### Bugs
     - #### Fixed Bugs
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

