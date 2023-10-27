# A'Bakes
<img src=#>
[Live Page: ] <br>

# Project Overview

A'kitchen is a web application that allows the target audience to browse & create recipes and engage in conversations with other users who are also authenticated on the website. A'Kitchen allows users to like and comment on recipes. 
This project's goal was to create a full-stack Django application using the computer languages Python, HTML, CSS, JavaScript, and Bootstrap. It makes use of CRUD capability so that authorised users may add expedition reviews to the website and create, browse, amend, and delete them. User registration and sign-in are implemented using the allauth Django package.

<br>

# Table of Contents
1. [User Experience (UX)](#user-experience)<br>
    1. [Strategy](#strategy)<br>
    2. [Scope](#scope)<br>
    3. [Structure](#struture)<br>
    4. [WireFrame](#wireframe)<br>
    5. [Surface](#surface)<br>
2. [Features](#feature)
3. [Testing](#testing)<br>
    - [User Stories](#user-stories)
    - [Automated Testing](#automated-testing)
    - [Validation testing](#validation)
4. [Deployment](#deployment)
5. [Tecnologies Used](#tecnology-used)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

# 1. User Experience (UX)
###  Project Goals:
- The project's objective is to provide a platform that will enable the website owner to share her recipes with the entire world. Bring together a community that enjoys baking. A forum where they can converse, exchange recipes, and express their passion for baking.

### Site owner goal:
- Provide a platform that is user-friendly and open to everyone.
- A website that needs to look good across all screen sizes.
- Allows the website owner to change the existing or previous recipes
- Allows the site owner the ability to view the likes and comments to determine which content is the most popular.

### User goals:
- The platform should be simple to use and straightforward for users.
- User who love to Bake
- Users who enjoy talking to others about recipes they've tried out from posts.
- User looking for a kind and supportive community that recently took up baking.

## 1. Strategy 
## User Stories- Agile Methodology 
### Account & Registration <hr>
1.1 **As a** Site user **I can** Register for a account **so that** I can have the      ability to comment on post, like posts and share my recipe<br>
1.2 **As a** Site user **I can** Login with my username and password **so that** I can utilise all of the website's features.<br>
1.3 **As a** Site user **I can** Log-out of my account **so that** other users cannot access my account. <br>
1.4 **As a** Site user **I can** Recover my password if i have forgotten **so that** I can recover my account and access the site features.<br>

### Navigation <hr>
2. **As a** Site user **I can** access Nav Bar from any page **so that** I can choose go anywhere on the site<br>

### Post <hr> 
3.1 **As a** Site user/ Guest user **I can** View a list of post/ recipes **so that** I am able to choose which recipes/post I would like to view<br>
3.2 **As a** Site user/ Guest user **I can** View a paginated list of posts **so that** It doesn't get overpopulated with post<br>
3.3 **As a** Site user/ Guest user **I can** Click on a post **so that** I can read the full recipe and see If would like to create it<br>
3.4 **As a** Logged-In user **I can** post my recipes **so that** I can share my recipe on the site for other user to view<br>
3.5 **As a** Logged-In user **I can**Like a post/ recipe **so that** I can show my love to recipe<br>
3.6 **As a** Logged-In user **I can** leave a comment on a post/ recipe **so that** I can be involoved in the converation and express my opnion on the recipe<br>

### Site Admin <hr>
4.1 **As a** Site admin **I can** create, edit and delete post on the Django admin **so that** I can manage the site for the best User Experiene<br>
4.2 **As a** Site admin **I can** approve and delete comments the Django admin **so that**I can filter out the comment for best  User Experience<br>
4.3 **As a** site admin **I can** edit and delete recipe/post **so that** if there any repeat and if there are any error that can be solved. 
4.4 **As a** Site admin **I can** manage user  account **so that** create new users, update current user details or deactive user status**<br>

## 2.Scope
---

## 3. Structure 

### Code Structure <hr>
I have split the code in different Apps, FoldersFiles and Files using the Django framework. 

- ### Abakes -app- 
    This folder contains the main project files:-
    * Setting.py - Setting 
    * Urls.py - Website urls 

- ### Blog -app- 
    This folder conatins all the functuionallty file for the app:-
    * Admin.py - The models are seen in the Django admin panel due to this file. It's also used in admin panel customization.
    * Forms.py - The fields on the form that are utilised in the app are customized in this file. 
    * Models.py - This file contain all the attribute details and models. 
    * Test.py - Automated testing for forms, models, and views is contained in this file. 
    * urls.py - This file containe all the Website urls
    * views.py - This file contains Python functions and classes that return a web page response after receiving a request.  

- ### Folder 
    * Static - This folder contain CSS and JaveScript files
    * Templates - This folder contains all the HTML templates and AllAuth(Django authentication)

- ### Files 
    * Db.sqlite3 - This file contain the Database for development
    * Manage.py - This is the main Python file for starting the website
    * Procfile - This file allows to run the App
    * Readme.md - This file contain read me documention
    * Requriement.txt - This file contains all the Python libraries that have been installed for this app. 

<hr>

### Website Structure 

--- 
## Database

Relational databases was used to complete the coding for this application. During development, I used SQLite DB in production, Postgres was the primary database, and for deployment, all data was moved to Heroku Postgres.  

### Data Schema 

### Models
<hr> 
    * User Model
    * Like Model
    * Comment Model  

### 4. WireFrame

### 5. Surface 
* Font    
* Color Palette 
* Images

---

# 2. Features
- Logo & Navigation Bar
    The logo and navigation bar are always present at the top of the screen and can be accessed from any page. so that the user does not need to scroll up in order to view the logo and navigation bar at the top of the page. 

- Footer
    The social media account can be accessed through the footer, which is located at the bottom of the website. Upon selecting the preferred social media platform, a new page will open with the user's customizable application. 

- Home Page 
    The welcome text and background on the home page provide a brief introduction to the site administrator and her passion for baking.  

- Blog Page
    The blog page has all the list of uploaded recipe that are approved for the admin is available.  Every post is displayed on a card that includes a header, an image, a recipe, the amount of likes and comments, the time and date it was uploaded, and more.  

- Recipe Page
   The recipe page lets users look at the recipe. It greets them with the recipe's image and title at the top, followed by the amount of likes and comments. The user is then prompted to the ingredient section, with another image appearing immediately below. Then comes a instructions on how to bake or prepare the dish, along with an another Image. Then the comment box, where users can share their thoughts on the recipe, is located directly beneath it.
   
- Gallary page
    The Gallary Page has a few desserts that have been created, some that have been uploaded, and others that will be uploaded soon are all shown in the gallery page. 

- Contact Us page 
    If a site visitor wants to get in touch with the admin, they can do so via the Email JS form on the contact page.
- Log in Page 
    Using the Django allauthentication user can use the Login page to enter username and password to log in 
- Log out Page
    The sign-out page asks the user if they are sure they want to log out, and if they are, they just click the sign-out button.
- Registation Page
    The user can access the registration form by clicking the "sign up" option on the login page if they do not have any login details. 

--- 
# 3. Testing 
### user Stroies 
### Automated testing
### Validation testing 

# 4. Deploment 
### Installing Django and Libraries
Before I start developing the project, I need to install Django and its dependencies on GitPod in order for it to function.
Once you've launched GitPod, proceed as follows in the Terminal:-
1. pip3 install 'django<4’ gunicorn : This will install Django & Gunicorn 
2. pip3 install dj_database_url==0.5.0 psycopg2 : This will install database
3. pip3 install dj3-cloudinary-storage : This will install Cloudinary library 
4. In order to avoid having to reinstall them, you must now add them to the required file. you can do that by : pip3 freeze --local > requirement.txt. This will create a new file and save that data. 
5. Now you can create the project by : django-admin startproject abakes.
6. Now you need to create the app : python3 manage.py startapp blog. 
7. python3 manage.py migrate : this will migrate the project and app. 
8. To test if everything is working run: python3 manage.py runserver. 

### Heroku App
For the project your need Heroku and you need to make an account on [Heroku](https://www.heroku.com/platform). 

1. To create a new app you would need to 
    - Go on Heroku dasboard
    - Click 'New' 
    - Then 'Create New App'
2. Enter a name for you Heroku app and select the region
3. To add the database to the Heroku app: 
    - Go to the Resources tab and in the add-ons sections, search for 'Heroku Postgres' and click it. 
    - Then click 'Hobby Dev - Free' from the plan name drop-dwon menu. 
    - Then Submit Order Form. 
4. To get the database URL, you would need to go to setting tab and then click 'Reveal Config Vars'. Copy the database URL. 

### Attaching the Database 
1. Make "env.py" a new file inside the Django application.
2. The os library needs to be imported into the "env.py" file. in order for you to save information. Add : "import os" 
3. Set the Environmet variable : Add "os.environ["DATABASE_URL"] = (Paste the database key from Heroku)
4. Then add the secret key : Add "os.environ["DATABASE_URL"] = (As hsi is your project you can create your own key) 
for example: 
    ----------------------------------------------------
    |os.environ["DATABASE_URL"] = (your database key )|
    |os.environ["SECRET_KEY"] = (your secretkey )|
    ----------------------------------------------------

### Enviroment and Setting Files
1. For getting our file setup and evenironemtn ready for the project  Add the following snippet at the top of the settings.py file:
    --------------------------
    | from pathlib import Path |
    | import os |
    | import dj_database_url |
    | if os.path.isfile('env.py'): |
    |    import env |
    --------------------------------

2. Just below that look for : SECURITY WARNING: keep the secret key used in production secret! and then enter following snippet:

    SECRET_KEY = os.environ.get('SECRET_KEY')

3. We would need to comment out the previous Database section  in order for the project to link to our database.To accomplish that, use # before the text:
     
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
4. Once that been comment out  add the updated database details: 
    
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

5. After it is finished, we need make migrations : python3 manage.py makemigrations. 
6. If everything is okay then migrate : python3 manage.py migrate.

### Cloudinary 
For the project your need cloudinary and you make a account on [Cloudinary](https://cloudinary.com/). 
1. From Cloudinary dashbaord you can copy the CLOUDINARY_URL and then paste in to env.py file. 
    for example:
    ---------------
    | os.environ["CLOUDINARY_URL"] = (your copied key from cloudinary dashbaord) |
    ---------------
2. Add the same copied cloudinary key to Heroku config var, your would just need to enter CLOUDINARY_URL in the config section and as the key would be the same key you enter in env.py file. 
3. Now we need to add the cloudinary key in the setting.py file.
    - Firstly add the cloudinary libararies under the installed apps you have to make sure you enter the order correctly like below:

        1. 'cloudinary_storage',
        2. 'django.contrib.staticfiles',
        3. 'cloudinary',

4. Enter the following code to let Django use Cloudinary to store media and static files:

    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

5. Enter the following code to link the Templates directory:

    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

7. Change the directory for templates to TEMPLATES_DIR (from TEMPLATES array): 

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]   

8. For the Website to run we need to add Heroku Hostname to Allowed_Hosts array: 

    ALLOWED_HOSTS = ["ci-pp4-a-abakes.herokuapp.com", "localhost"]. 


### Local Deployment
### Manual Deployment 



# 5. Tecnologies Used
## Languages 
- HTML : The foundational language utilised to create the project's templates is HTML.
- CSS : To add my personal styling to the project, custom CSS was written. Additionally, media queries were added to provide responsiveness across various viewport sizes.
- Javascript
- Python 
- Django

## Applications, Platforms, Resources 
- Bootstrap: The project's overall content structure, footer, and navbar were all implemented using the Bootstrap framework.
- GitPod: IDE used for the development.
- GitHub: Used to create a repository where the project's files are stored. 
- Balsamiq Wireframe: The wireframes for this project were made using this, and they were displayed in the Skeleton Plane. 
- Am I Responsive: Used to make user the website was responsive. 
- Google Font : To make it more unique, Google Font was utilised to create the text. 
- Heroku : Utilised this cloud-based platform to deploy the website and make it public.
- Heroku PostgreSQL : Utilised as the project's database of choice while it was being developed.   
- Cloudinary : Used to store project media images and static files. 
- Django AllAuth: Utilised to carry out user authentication on websites
- Font Awesome : Used to get soicla medial icons. 


### Future Improvements
I would like to implement a number of functionality upgrades in the future. I was unable to complete my project because of a personal situation. But here is what I would have added:
1. The capability of recovering a user's password in the event that it has been lost, stolen, or corrupted.
2. Give the user the option to rate the recipe once they tried.
3. The opportunity to let users vote on the upcoming recipe.

## Credits

## Acknowledgements