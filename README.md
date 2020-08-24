# ZeeZee Bijoux

## Fourth Milestone Project

## Code Institute / Full Stack Frameworks

ZeeZee Bijoux is an e-commerce site, where the shopper can browse for handmade, unique jewelry. This site was built as my final milestone project for the Code Institute Full Stack Web Development diploma.
The purpose of ZeeZee Bijoux online shop is to provide a nice, intuitive platform for the artist to share her bijoux with potential shoppers, so they can easily buy them, and become a part of ZeeZee Community.
![AmIresponsive](https://github.com/krisztinatxt/zeezee/blob/master/media/amiresponsive.PNG "Responsive Image")

## Table of Contents

1. [UX](https://github.com/krisztinatxt/zeezee#ux)
    - [Project Goals](https://github.com/krisztinatxt/zeezee#project-goals)
    - [User Stories](https://github.com/krisztinatxt/zeezee#user-stories)
    - [Developer Goals](https://github.com/krisztinatxt/zeezee#developer-goals)
    - [Design](https://github.com/krisztinatxt/zeezee#design)
        - [Color Scheme](https://github.com/krisztinatxt/zeezee#color-scheme)
        - [Fonts](https://github.com/krisztinatxt/zeezee#fonts)
        - [Wireframes](https://github.com/krisztinatxt/zeezee#wireframes)
2. [Features](https://github.com/krisztinatxt/zeezee#features)
    - [Existing Features](https://github.com/krisztinatxt/zeezee#existing-features)
    - [Features Left to Implement](https://github.com/krisztinatxt/zeezee#features-left-to-implement)
3. [Testing](https://github.com/krisztinatxt/zeezee#testing)
4. [Deployment](https://github.com/krisztinatxt/zeezee#deployment)
    - [How to deploy the site](https://github.com/zeezee#how-to-deploy-the-site)
    - [How to deploy locally](https://github.com/zeezee#how-to-deploy-locally)
5. [Technologies Used](https://github.com/krisztinatxt/zeezee#technologies-used)
6. [Credits](https://github.com/krisztinatxt/zeezee#credits)
    - [Content](https://github.com/krisztinatxt/zeezee#content)
    - [Media](https://github.com/krisztinatxt/zeezee#media)
    - [Code](https://github.com/krisztinatxt/zeezee#code)
    - [Acknowledgements](https://github.com/krisztinatxt/zeezee#acknowledgements)

## UX

### Project Goals

ZeeZee Bijoux is part of my Code Institute Full Stack Software Development studies, the Full Stack Development with Django module.
The scope for this application was to create an e-commerce site using Django and providing the checkout system using the Stripe payment system.
As this is my last milestone project, I wanted to work with a "real" client, so I reached out to an artist acquaintance to create a webshop for her handmade jewellery.
The target audience of the page is women around the age 15-40, preferring to wear something special, handmade, and unique. All products are unique, can not be reproduced.

### User Stories

As a User I would like to:

- [x] easily access the webshop from different kinds of devices.
- [x] have an easy and logical method to buy a product.
- [x] have the opportunity to buy a product even if you don't want to sign up.
- [x] browse bijoux by categories.
- [x] find bijouxs or type of bijouxs.
- [x] get pieces of information about products and the creator.
- [x] sign up.
- [x] easily add or remove products to my bag.
- [x] get an email about my order.
- [x] place an order.
- [x] save the order information to their profile.
- [x] create a profile.
- [x] edit my shipping information if it's needed.
- [x] have an easy way to contact the webshop if I have a problem.
- [x] get success or error message to know my feedback was successfully submitted.
- [x] leave feedback and read about other shoppers' feedback.
- [x] follow the status of my order.

As a SuperUser (Products Owner) I would like to:

- [x] easily add, edit and delete orders.
- [x] have a nice product management page which is easy to use even if you don't have any experience in admin platforms.

### Developer Goals

- Provide a nice, easy to use webshop where the user can browse, add to bag, order, and checkout.
- Learn Django framework, and try to use as much as I can from things I learned during the course.
- Get an insight into Amazon AWS and Stripe Payment's platform.

### Design

I used Bootstrap, and FontAwesome to make an integrated design for this site
The best-used components are cards. I chose cards for products, categories because I think cards helps me to organize the information in a user-friendly way.
For providing feedback, editing, and adding products or shipping informations I used forms.

![ContactForm](https://github.com/krisztinatxt/zeezee/blob/master/media/contact_mobile.PNG "Responsive Image")

#### Color Scheme

Two of the most important colors are purple and grey. To make the site consistent and easy to read, I used these two colors for almost everything.
To find out, what colors would match with the bijouxs's feeling and style, I used [ColorSpace](https://mycolor.space/).

Colors I used:

- ![#6A0848](https://placehold.it/15/6A0848/000000?text=+) `#6A0848 - purple, primary color`
- ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) `#FFFFFF- white, secondary color`
- ![#A8A8A8](https://placehold.it/15/A8A8A8/000000?text=+) `#A8A8A8 - grey, text color for small paragraphs, and color for hovers`
- ![#84d5ff](https://placehold.it/15/84d5ff/000000?text=+) `#84d5ff - light blue (info-blue) for making the login system easier to read and navigate in`
- ![##FF0000](https://placehold.it/15/#FF0000/000000?text=+) `#FF0000 - red used once at the Delete button`

#### Fonts

The font I selected for this page is Baloo 2 from [GoogleFonts](https://fonts.google.com/), because it fits perfectly with the elegant, bohemian, and playful design the bijoux and their creator represent.

### Wireframes

I created my wireframes during the Scope Plane of this project.
I made wireframes for each page of the site from three different types of devices:

1. [Desktop](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/desktop)

2. [Tablet](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/tablet)

3. [Mobile](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/mobile)

The implementation ended up slightly different.

## Features

### Existing Features

#### Get all Products, Sort, Filter and Search

- The user can load all of the products or browse products sorting by categories. Filtering is available by Price (low to high or high to low) and by Name (A-Z or Z-A).
- The product page is split using Django Pagination to provide a transparent list of products.

#### Edit, Update and delete Products

- The superuser can easily edit or delete a product using the adequate button on the Product Detail page.
- They can add products on Product Management Page.In order to make it easy to upload a collection of products, when the superuser adds one product, they get redirected to the Add Product Page instead of All Product Page.

#### Send feedback

- The user can write reviews, send some feedback about the product or the shop itself.
- The visitor can read these feedbacks so they can have an image of the shop.

#### Get in touch

- The user can send an email using the Contact Form.
- The contact form is using emailJS.

#### Sign up, Sign in, login

- The shopper can easily sign up, sign in, and reach their profile with the shipping and order information.
- I built the authentication system using Django Allauth.

#### Product returning

- If the shopper is not happy with the product, they can return it.
The link to this return form is a part of the footer, so the user doesn't have to sign in, or sign up (as they can place order without authentication too).
The idea is that the dissatisfied shopper provides some information about the problem, they give the order number, and contact details, and the owner gets this data in Django Admin, so she can answer, and start the process.
![Request](https://github.com/krisztinatxt/zeezee/blob/master/media/request.PNG "Responsive Image")

### Features Left to Implement

- I would like to build Facebook Login and Sharing-Like system later on. I was working on it, and on the development side everything was working fine, so I could login with Facebook, share a product, and like it.
but I couldn't find the way to make it work in the deployed version. I tried a couple of ways to fix it, but it seems that I have a problem with my CallBack URI.
I haven't sorted it out yet, but I definitely want to add those features in the future to the deployed version too.

- To have a unified view, I would like to change all Product Previews to a white background picture of the product. Currently the artist could provide me white background pictures for all products, and I didn't want to mix the natural and studio photos up, so I chose to use 'natural' pictures as previews.

## Testing

Basic testing files to check if the page is correctly loading are in ``` test.py ``` in regarding app's folders.

### Homepage

- On the Homepage, you can see a navbar that is consistent on each page. It contains a menu and a User Menu with authentication and shopping bag.
The navbar is collapsable on mobile devices.
- Under the navbar, there is a responsive hero image.
- On the Homepage, you can find a small introduction textbox to tell the user a little bit about the scope of the page.
Inside that field, there is a MailChimp form, where the user can find the Facebook page of ZeeZee Bijoux.
The form loads in a new tab.
- To show users some products on the Homepage, I chose to use cards. Each card leads the user to a category. I used an overlay on cards, so when the user ```hover```, they can see which category belongs to that card.
- The footer is another returning component on the page.
The footer contains two FontAwesome icons leading to the Instagram and Facebook page of the artist, and the return product link.
All links are working, Instagram and Facebook links load in a new tab.

### Products Page

- When the user wants to see Products, they can choose between browsing by categories or loading all products.
- If the user chooses to load product categories, they can see a badge telling which category is loaded.
- I used count() to let the user know how many products they can find on that page.
- I built Django Pagination to split the page and make it easier to navigate on.
- There is a search bar to let the shopper search for categories, components, materials they are interested in.
- Besides sorting by categories, there is a SortBy function loading the products sorting them by the price or the name.
- On Detailed Product Page, there is a Bootstrap carousel to show the product images.
- Product details are visible for anyone, Edit and Delete buttons are available only for SuperUsers.
Edit and delete functions works without a problem.
- The quantity is set to one because each product is unique.
- When the user adds a product to their bag, a Bootstrap toast pops up to display a success message.
These bootstrap messages appear after every operation. I used toast to display success, error, info, and warning.

![Orders](https://github.com/krisztinatxt/zeezee/blob/master/media/profile.PNG "Responsive Image")

### About Page

- The About Page contains a small introduction about the creator of ZeeZee Bijoux and a responsive image of her.

### Contact Page

- The Contact Page is built with a form where the user can provide some information and send the message to the developer.
I used emailJS for this page. After submitting the form, they get redirected to a success page.
The form is tested, test email successfully received.

### Feedback Page

- For the GuestBook, I used Django comments to provide a platform where the user can add reviews and see other people's feedback about the shop or the products.
These reviews can be removed from the Django Admin only. Comments are tested.

### Bag

- The default status of the bag is empty. When a user adds an item to it, they can see the product details, the bag total, the delivery cost, and the grand total.
If they hit on Secure Checkout, a form appears where the user has to provide some information regarding the delivery and the payment.
All fields are required to be filled out. After the checkout, they get redirected to a success page which contains an order summary and a button back to all product pages.
The whole checkout process was tested from different devices. Everything worked well. After the checkout, the admin can see the order in Django Admin and Stripe dashboard as well.

![Checkout](https://github.com/krisztinatxt/zeezee/blob/master/media/checkout_form.PNG "Responsive Image")

### Authentication

- Authentication is provided by using Django Allauth. The user can sign up by setting a username, a password, and a valid email address.
After clicking on Sign Up, they receive an email with a link to activate the profile. By clicking on the link, the user created a profile, so they can log in.
Signed in users have a profile with delivery information (if they choosed to save it), and an order history with details about the product, and an order status.
The order status has two mode: Processed and Awaiting, telling the user if their order is already seen by the shop owner. The status of the order can be changed in Django Admin.
- SuperUser can click on Product Managment page where they can add new products. This page is only available for the shop owner.
The whole sign up, sign in, sign out process was tested, everything worked well.

### Compatibility

The site compatibility was checked with devtools, the AmIresponsive site, Responsive Viewer Chrome extension, and also tested by friends from different devices and browsers.

The site is responsive when you are browsing with:
    - [x] Google Chrome.
    - [x] Mozilla Firefox.
    - [x] Opera.  

Tested devices:

- [x] laptop, laptop with touch (width 1440px);

- [x] Moto G4;

- [x] Galaxy S5;

- [x] Pixel2, Pixel 2XL;

- [x] Iphone 5/SE, Iphone 6/7/8;

- [x] Iphone 6/7/8 Plus, IphoneX;

- [x] Ipad and Ipad Pro;

- [x] Xiaomi Redmi 4A.

- [x] Xiaomi Redmi Note5.

All of the codes are validated and beautified.

- [HTMLValidation](https://validator.w3.org/):
  - Unfortunately the HTML validator doesn't understand the Jinja templating syntax, so I got a bunch of errors because of this.
    No other error found.
- [CSSValidation](https://jigsaw.w3.org/css-validator/):
  - No error found, valid.
- [JavaScript Validation](https://esprima.org/demo/validate.html):
  - No error found, code is syntactically valid.
- [PythonCodeChecker](https://extendsclass.com/python-tester.html):
  - No syntax errors detected. A couple of errors saying that the line is too long, but in Django project, Chris advised to ignore those if don't affect the code itself.

### Bugs

- When I added media and static files to AWS S3 bucket, the deployed version couldn't load any of my pictures from the homepage, although my product images were loaded correctly.
The solution was to change the path to  ```{{ MEDIA_URL }}background_hand.jpg```.

- After I added something to my bag and proceeded secure checkout, the price of the product turned to 0.00. I saw that payment succeeded in my stripe account, but in Django Admin I couldn't see the order summary properly.
The problem was caused by an indentation error in my ```signals.py```.

## Deployment

### How to deploy the site

To deploy ZeeZee Bijoux webshop to heroku, take the following steps:

1. Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

2. Create a Procfile with the terminal command echo web: python app.py > Procfile.

3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.

- Add ```echo web: gunicorn main.wsgi:application > Procfile```

4. Create a new app on the Heroku website by clicking the "New" button in your dashboard.

5. From the heroku dashboard of your application, click on "Deploy" > "Deployment method" and select GitHub.

6. Link heroku and GitHub repository.

7. In the Heroku Resources tab, navigate to the Add-Ons section and search for Heroku Postgres. Make sure to select the free Hobby level.

8. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars". And set the followings config vars:

- AWS Access Key,
- AWS Secret Key,
- S3 Bucket Name,
- Database URL,
- Hostname,
- Secret Key,
- Stripe Secret Key.

9. In your heroku dashboard, deploy the application.

10. When the building is finished, you can check it by clicking View App.
If you want to access admin, just add ```/admin``` at the end of your site.

11. To create storage for the deployed site, you can use AWS S3 bucket and IAM. To learn more about that, click [here](https://docs.aws.amazon.com/).

### How to deploy locally

In order to run this project locally on your own system, you will need the followings:

- an IDE like GitPod or VS Code;
- Python3;
- PIP;
- GIT.

If you have these things up and running, then the next steps are:

1. Clone this GitHub repository by clicking the green "Clone or download" button above in order to download the project as a zip-file. Download it, and unzip it.

2. Create a .env file with your own credentials.

3. Create a requirements.txt file, then free requirements with this command:
```pip freeze > requirements.txt```

4. To launch your project on an IDEA, type this in your terminal:

```python manage.py runserver```

5. After exposing the port, you should see the local server running.

6. In order to access the Django Admin Panel, you must generate a superuser:
```python manage.py createsuperuser``` then assign an admin username, email, and secure password.

7. Now you can login as a superuser on Django Admin. Add ```/admin``` to the end of the local port address, and login.

## Technologies Used

- [GitHub](https://github.com/);

- [GitPod](https://gitpod.io/);

- [Heroku](https://dashboard.heroku.com/);

- [HTML](https://en.wikipedia.org/wiki/HTML5);

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript);

- [Django](https://www.djangoproject.com/);

- [Jquery](https://jquery.com/);

- [Materialize](https://materializecss.com/);

- [Python](https://www.python.org/download/releases/3.0/);

- [EmailJS](https://www.emailjs.com/);

- [Gmail](https://mail.google.com/);

- [MarkDownLit](https://dlaa.me/markdownlint/);

- [Balsamiq](https://balsamiq.com/);

- [HTMLValidator](https://validator.w3.org/);

- [CSSValidator](https://jigsaw.w3.org/css-validator/)

- [JavaScriptValidator](https://esprima.org/demo/validate.html);

- [HTMLFormatter](https://htmlformatter.com/);

- [CSSBeautifier](https://www.freeformatter.com/css-beautifier.html);

- [JSHint](https://jshint.com/);

- [PythonCodeChecker](https://extendsclass.com/python-tester.html);

- [Favicon](https://www.favicon-generator.org/);

- [GoogleFonts](https://fonts.google.com/);

- [AmIResponsive](http://ami.responsivedesign.is/);

- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/);

- [PyMongo](https://pymongo.readthedocs.io/en/stable/);

- [PEP8](http://pep8online.com/);

- [Bootstrap](https://getbootstrap.com/);

- [FontAwesome](https://fontawesome.com/);

- [Stripe](http://stripe.com/);

- [MailChimp](https://mailchimp.com/);

- [SqLite](https://www.sqlite.org/index.html);

- [AWS Amazon](https://aws.amazon.com/);

## Credits

### Content

Product names, descriptions and introduction text was written by jewelry maker, Bekő-Fóri Zenkő.

### Media

All pictures are owned by Bekő-Fóri Zenkő.

### Code

- I learned a lot from the Code Institute Full-Stack Frameworks Boutique Ado Project, I used that as a shell of my project.
- Threads from [Stackoverflow](https://stackoverflow.com/) about how to fix diverse bugs.
- The base of the code for back to top button [W3Schools](https://www.w3schools.com/).
- The base of the code for main functionalities is from [Django Official Documentation](https://docs.djangoproject.com/en/3.1/).

## Acknowledgements

Special thanks to:

- Code Institute Tutor Team, they helped a lot during this project.
- [Tutor Tim](https://github.com/TravelTimN), who is always helpful, professional, devoted and patient. Thanks a lot for this year, Tim!
- My mentor, [Aaron Sinnott](https://github.com/aaronsnig501) for his advices.
- Everybody who did take time to test this page, and gave me feedback.
This site is for educational use.

Krisztina Szabó

Code Institute
2020
