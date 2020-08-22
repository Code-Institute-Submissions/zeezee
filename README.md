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

- Provide a nice, easy to usewehsbop where the user can browse, add to bag, order, and checkout.
- Learn Django framework, and try to use as much as I can from things I learnt during the course.
- Get an insight into Amazon AWS and Stripe Payment's platform.

### Design

To make an integrated design for this site, I used Bootstrap, and FontAwesome.
The best-used components are cards. I choosed cards for products, categoriesure because I think cards helps me to organize the information in a user-friendly way.
For providing feedback, editing and adding products or shipping informations I used forms.

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

#### Get all Products, Sort, Filter and Search

- The user can load all of the products or browse products sorting by categories. Filtering is available by Price (low to high or high to low) and by Name (A-Z or Z-A).
- Product page is splitted using Django Pagination to provide an transparent list of products.

#### Edit, Update and delete Products

- The superuser can easily edit or delete a product using the adequate button on the Product Detail page.
- They can add products on Product Management Page. To make it easy to upload a collection of products, when the superuser add one product, they get redirected to the Add Product Page instead of All Product Page.

#### Send feedback

- The user can write reviews, send some feedback about the product or the shop itself.
- The visitor can read these feedbacks so they can have an image about the shop.

#### Get in touch

- The user can send an email using the Contact Form.
- The contact form is using emailJS.

#### Sign up, Sign in, login

- The shopper can easily sign up, sign in and reach their profile with the shipping and order information.
- I built the authentication system using Django Allauth.

### Features Left to Implement

- I would like to build Facebook Login and Sharing-Like system in the future. I was working on it, and on the development side everything was working fine, so I could login with facebook, share a product and like it, 
but I couldn't find the way to make it work in deployed version. I tried a couple of ways to fix it, but it seems that I have problem with my CallBack URI.
I haven't sorted it out, but I definitely want to add those features in the future to the deployed version too. 

- To have a unified view, I would like to change all Product Previews to a white background picture about the product. Currently the artist could provide me white background pictures for all products, and I didn't want to mix the natural and studio photos up, so I choosed to use 'natural' pictures as previews.

## Testing

Basic testing files to check if the page is correctly loading are in ``` test.py ``` in regarding app's folders.

### Homepage

- On the Homepage you can see a navbar which is consistent on each pages. It contains a menu and a User Menu with authentication and shopping bag.
The navbar is collapsable on mobile devices. 
- Under the navbar there is a responsive hero image. 
- On the Homepage you can find a small introduction textbox to tell the user a little bit about the scope of the page.
Inside that field there is a MailChimp form, where the user can find the Facebook page of ZeeZee Bijoux. 
The form loads in a new tab.
- To show user some products on the Homepage, I choosed to use cards. Each card leads the user to a category. I used overlay on cards, so when the user ```hover```, they can see which category belongs to that card.
- The footer is an other returning component on the page. 
The footer contains two FontAwesome icons leading to the Instagram and Facebook page of the artist, and the developers name leading to the GitHub page of mine.
All links are working, they load in new tab.

### Products Page

- When the user want to see Products, they can choose between browsing by categories or loading all products.
- If the user choose to load product categories, they can see a badge telling which category is loaded.
- I used count() to let the user know how many product they can find in that page.
- I built Django Pagination to split the page and make it easier to navigate on.
- There is a searcbar to let the shopper search for categories, components, materials they are interested in.
- Besides sorting by categories, there is a SortBy function loading the products sorting them by the price or the name.
- On Detailed Product Page there is a Bootstrap carousel to show the product images.
- Product details are visible for anyone, Edit and Delete buttons are available only for SuperUsers.
Edit and delete functions works without problem.
- The quantity is set to one, because each product is unique.
- When the user add a product to their bag, a Bootstrap toas pops up to display a success message.
These bootstrap messages appear after every operation. I used toast to display success, error, info, and warning.

### About Page

- The About Page contains a small introduction about the creator of ZeeZee Bijoux, and a responsive image of her.

### Contact Page

- The Contact Page is built with a form where the user can provide some information and send the message to the developer.
I used emailJS for this page. After submitting the form, they get redirected to a success page.
Form is tested, test email successfully received. 

### Feedback Page

- For the GuestBook I used Django comments to provide a platform where the user can ad reviews, and see other people's feedback about the shop or the products.
These reviews can be removed from the Django Admin only. Comments are tested. 

### Bag 

- The default status of the bag is empty. When a user adds an item to it, they can see the product details, the bag total, the delivery cost and the grand total.
If they hit on Secure Checkout, I form appears where the user has to provide some information regarding the delivery and the payment.
All fields are required. After the checkout, they get redirected to a success page which contains an order summary and a button back to all product page.
The whole checkout process was tested from different devices. Everything worked well. After the checkout, the admin can see the order in Django Admin and Stripe dashboard as well.

### Authentication

- Authentication is provided by using Django Allauth. The user can sign up by setting a username, a password and a valid email address.
After clicking on Sign Up, they receive an email with a link to activate the profile. By clicking on the link, the user created a profile, so they can login.
Signed in users have a profile with delivery information (if they choosed to save it), and an order history with details about the product, and an order status.
The order status has two mode: Processed and Awaiting, telling the user if their order is already seen by the shop owner.
The status of the order can be changed in Django Admin.
- SuperUser can click on Product Managment page where they can add new products. This page is only available for the shop owner.

### Compatibility
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

### Bugs

- When I added media and static files to AWS S3 bucket, the deployed version couldn't load any of my pictures from homepage, altough my product images were loaded correctly.
The solution was to change the path to  ```{{ MEDIA_URL }}background_hand.jpg```.

- After I added something to my bage and proceedeed secure checkout, the price of the product turned to 0.00. I saw that payment succeeded in my stripe account, but in Django Admin I couldn't see the order summary properly.
The problem was caused by an identation error in my ```signals.py ```.

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