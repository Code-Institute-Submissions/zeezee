# ZeeZee Bijoux

## Fourth Milestone Project

## Code Institute / Full Stack Frameworks

ZeeZee Bijoux is an e-commerce site, where the shopper can browse for handmade, unique jewellery. This project was built as my final milestone project for the Code Institute Full Stack Web Development diploma.
The purpose of ZeeZee Bijoux online shop is to provide a nice, intuitive platform for the artist to share her bijoux with potential shoppers, so they can easily buy them, and become a part of ZeeZee Community.
![AmIresponsive]( "Responsive Image")
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
The scope for this application was to create an e-commerce site using Django and providing the checkout system using Stripe payment system.
As this is my last milestone project, I wanted to work with a "real" client, so I reached out an artist aquiantance to create a webshop for her handmade jewelleries.
The target audience of the page is woman around 15-40, preferring to wear something special, handmade and unique. All products are unique, can not be reproduced.

### User Stories

As a User I would like to:

- [x] easily access the webshop from different kind of devices.
- [x] have an easy and logical method to buy a product.
- [x] have the opportunity to buy a product even if you don't want to sign up.
- [x] browse bijouxs by categories.
- [x] find bijouxs or type of bijouxs.
- [x] get informations about products and the creator.
- [x] sign up.
- [x] easily add or remove products to my bag.
- [x] get an email about my order.
- [x] place an order.
- [x] save the order informations to their profile.
- [x] create a profile.
- [x] edit my shipping information if it's needed.
- [x] have an easy way to contact the webshop if I have problem.
- [x] get success or error message to know my feedback was successfully submitted.
- [x] leave feedback and read about other shoppers feedback.
- [x] follow the status of my order.

As a SuperUser (Products Owner) I would like to:

- [x] easily add, edit and delete orders.
- [x] have a nice product managment page which is easy to use even if you don't have any experience in admin platforms.

### Developer Goals

### Design

#### Color Scheme

Two of the most important colors are purple and grey. To make the site consistent and easy to read, I used these two colors for almost everything.
To find out, what colors would match with the bijouxs's feeling and style, I used [ColorSpace](https://mycolor.space/).

Colors I used:

- ![#6A0848](https://placehold.it/15/6A0848/000000?text=+) `##6A0848 - purple, primary color`
- ![#A8A8A8](https://placehold.it/15/A8A8A8/000000?text=+) `#A8A8A8 - grey, secondary color`
- ![#84d5ff](https://placehold.it/15/84d5ff/000000?text=+) `#84d5ff - light blue (info-blue) for making the login system easier to read and navigate in`
- ![##FF0000](https://placehold.it/15/#FF0000/000000?text=+) `#FF0000 - red used once at the Delete button`

#### Fonts

The font I selected to this page is Baloo 2 from [GoogleFonts](https://fonts.google.com/), because it fits perfectly to the elegant, bohemian and playful design the bijouxs and their creator represent.

### Wireframes

I created my wireframes during the Scope Plane of this project.
I made wireframes for each page of the site from three different type of devices:

1. [Desktop](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/desktop)

2. [Tablet](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/tablet)

3. [Mobile](https://github.com/krisztinatxt/zeezee/tree/master/media/wireframes/mobile)

The implementation ended up slightly different.

## Features

### Existing Features

### Features Left to Implement

## Testing

The site compatibility was checked with devtools, the AmIresponsive site, Responsive Viewer Chrome extension and also tested by friends from different devices and browsers.

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

All of the codes are validated and beatufied.

- [HTMLValidation](https://validator.w3.org/):
  - Unfortunatelly the HTML validator doesn't understand the Jinja templating syntax, so I got a bunch of errors because of this.
    No other error found.
- [CSSValidation](https://jigsaw.w3.org/css-validator/):
  - No error found, valid.
- [JavaScript Validation](https://esprima.org/demo/validate.html):
  - No error found, code is syntactically valid.
- [PythonCodeChecker](https://extendsclass.com/python-tester.html):
  - No syntax errors detected. Couple of errors saying that the line is too long, but in Django project Chris advised to avoid those if doesn't effect the code itself.


## Deployment

### How to deploy the site

### How to deploy locally


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

- I learned a lot from the Code Institute Full Stack Frameworks Boutique Ado Project, I used that as a shell of my project.
- Threads from [Stackoverflow](https://stackoverflow.com/) about how to fix diverse bugs.
- The base of the code for back to top button [W3Schools](https://www.w3schools.com/).
- The base of the code for main functionalites are from [Django Official Documentation](https://docs.djangoproject.com/en/3.1/).

## Acknowledgements

Special thanks to:

- Code Institute Tutor Team, they helped a lot during this project.
- My mentor, [Aaron Sinnott](https://github.com/aaronsnig501) for his advices.
- Everybody who did take time to test this page, and gave me feedback.
This site is for educational use.

Krisztina Szabó

Code Institute
2020