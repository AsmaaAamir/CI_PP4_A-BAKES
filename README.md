# A'Bakes
<img src=#>
[Live Page: ] <br>
# Project Overview <hr>
A'kitchen is a web application that allows the target audience to browse & create recipes and engage in conversations with other users who are also authenticated on the website. A'Kitchen allows users to like and comment on recipes. 
This project's goal was to create a full-stack Django application using the computer languages Python, HTML, CSS, JavaScript, and Bootstrap. It makes use of CRUD capability so that authorised users may add expedition reviews to the website and create, browse, amend, and delete them. User registration and sign-in are implemented using the allauth Django package.

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

## 1. Strategy <hr>
---
## User Stories- Agile Methodology 

### Account & Registration <hr>
1.1 As a **Site user** I can **Register for a account** so that **I can have the ability to comment on post, like posts and share my recipe**<br>
1.2 As a **Site user** I can **Login with my username and password** so that **I can utilise all of the website's features.** <br>
1.3 As a **Site user** I can **Log-out of my account** so that **other users cannot access my account.** <br>
1.4 As a **Site user**  I can **Recover my password if i have forgotten** so that **I can recover my account and access the site features.**<br>

### Navigation <hr>
2. As a **Site user**  I can **I can access Nav Bar from any page** so that **I can choose go anywhere on the site**<br>

### Post <hr> 
3.1 As a **Site user/ Guest user**  I can **View a list of post/ recipes** so that **I am able to choose which recipes/post I would like to view**<br>
3.2 As a **Site user/ Guest user**  I can **View a paginated list of posts** so that **It doesn't get overpopulated with post**<br>
3.3 As a **Site user/ Guest user**  I can **Click on a post** so that **I can read the full recipe and see If would like to create it**<br>
3.4 As a **Logged-In user**  I can **post my recipes** so that **I can share my recipe on teh site for other user to view**<br>
3.5 As a **Logged-In user**  I can **edit my post/ recipe** so that **I can make any change if I made a error or update a recipe**<br>
3.6 As a **Logged-In user**  I can **delete my post/ recipe** so that **I can remove the reciped If i dont wish to shre it anymore**<br>
3.7 As a **Logged-In user**  I can **Like a post/ recipe** so that **I can show my love to recipe**<br>
3.8 As a **Logged-In user**  I can **leave a comment on a post/ recipe** so that **I can be involoved in the converation and express my opnion on the recipe**<br>

### Site Admin <hr>
4.1 As a **Site admin**  I can **create, edit and delete post on the Django admin** so that **I can manage the site for the best User Experiene**<br>
4.2 As a **Site admin**  I can **approve and delete comments the Django admin** so that **I can filter out the comment for best  User Experience**<br>
4.3 As a **Site admin**  I can **manage user  account** so that **create new users, update current user details or deactive user status**<br>


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
- Logo
- Navigation Bar
- Footer
- Home Page
- Blog Page
- Recipe Page
    - main Image 
    - Heading
    - Like 
    - Comments 
    - Ingredient 
    - Image
    - Instruction
    - Image
    - Edit and Delet option 
    - Comment Section 
- Gallary page
- Contact Us page 
- Log in Page 
- Log out Page 

--- 
# 3. Testing 
### user Stroies 
### Automated testing
### Validation testing 

# 4. Deploment 


# 5. Tecnologies Used
## Languages 
- Django 
- HTML
- CSS 

## Applications, Platforms
- Bootstrap:
- Git Pod:
- GitHub:
- Postgres:
- Balsamiq Wireframe: This was used to create the wireframes for this rpoject diplaying in the Skeleton Plane. 
- Am I Responsive: 
- Google Font:
- 

### Future Improvements
I would like to implement a number of functionality upgrades in the future. I was unable to complete my project because of a personal situation. But here is what I would have added:
1. A few of the user tales are unfinished.
2. The capability of recovering a user's password in the event that it has been lost, stolen, or corrupted.
3. Providing the option for users to share their recipes so that others can try them.
4. Give the user the option to rate the recipe once they tried.
5. Allow users to save a recipe to their favourites so that they may return to it without having to hunt for it after logging in.
6. The opportunity to let users vote on the upcoming recipe.
7. Complete the read-me file.
