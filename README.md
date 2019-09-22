[![Build Status](https://travis-ci.org/GILLIANMCD/graphic-design-services-m4.svg?branch=master)](https://travis-ci.org/GILLIANMCD/graphic-design-services-m4)

# Graphic Design Services

Graphic Design Services provides an online shop for individual bepoke products for individuality and print Graphic Design Services to clients.

## UX
 The color scheme of the site is bright and strong in color to give a modern theme and reflect that Graphic Design Services inject a strong presence with use of bold colors to promote indivuality. 

- As a user type, I want to perform an action, so that I can achieve a goal.
- As a site user I want to be able to purchase products online
- As a site owner I want to be able to sell products online
- As a site user I want to be able to send information in order to get a personal quotation for my needs
- As a site owner I want to be able to showcase my work through portfolios
- As a site ower I want to promote potential client activity on the site to promote awareness through a blog
- As a site user I want to be able to get tips on the latest marketing and branding techniques and trends


## Features

The site existingly has 8 app consisting of accounts, cart, checkout, portfolio, posts, search, quote, contact. The first 6 apps I was guided through the code institute tutorials and for quote and contact I created with the same process in mind but individualised apps for their required needs.
 
### Existing Features
- Users can Register and Log in to the site allowing access to the blog. 
- Users can reset their password 
- Users can purchase products as a logged in user or not. 
- Blog only appears for logged in users 
- I would like to implement setting where logged in users could have a history of their purchases quotations and blog activity on their account
- I would also like to implement where the user can recieve an automatic email when someone replys to any comments made by the user in the blog.



### Features Left to Implement
- Automatic Quotation where potential customer can adjust, confirm and pay for a project.
- App views imported to home page view, selection of products and sample portfolios. 
- Cart facility needs to reset back to zero on pae refresh when user is not logged in.
- Cart Facility needs to retain cart items when user is logged in.
- Email facility does not work. Existingly set to email backend with email settings noted out. Problem with gmail even with settings in accounts in google configured correctly. 
- When a user enters wrong password 2 messages appear 1 success and another with "Your username or password is incorrect" this needs to be fixed through form validation.
- Happy Clients Club where users can register for discounts for the provision of a testimonial which can be promoted in Portfolios. 
- Blog has to be complete at present there is only test blog showing and form to send blog post is not set up. 
- Images not showing on Portfolio 
- 


## Technologies Used

- [AWS Cloud9](https://aws.amazon.com/education/awseducate/)
    -   IDE for integrating Django to install libraries stated in requirements.txt file  

- [S3 Management Console](https://s3.console.aws.amazon.com)
    - Supports AWS Cloud 9 for Simple Storage of media files 
- [JQuery](https://jquery.com)
    - Run home page carousel.
- [Travis](https://travis-ci.org/)
    - Ensure testing on a continuous basis

- [Heroku](https://dashboard.heroku.com/apps)
    - Live deployment of site for testing. 


## Testing

Testing was complete through google chrome inspect for css views as changes were introduced to the site. Once site was deployed to heroku travis intigration was introducted to ensure build padding in [Travis](https://travis-ci.org). 

- Database Testing
    - Print forms to console to test connection to database
    - Complete forms on front end and check to ensure all data sent to admin section.  

- CSS Testing 
    - Google Chrome Inspect tool to ensure responsive design. 

- Form Validation Testing 
    - Enter correct information to forms to ensure all information and images are sent 
    - Enter incorrect information in forms to make sure no bugs exist and user cannot break forms. 

- Email Testing 
    - Register as a user to test emails are sent and user can reset their password - This function is currently not working. 


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- About us page 3rd paragraph [blackbreardesign](https://www.blackbeardesign.com/services/graphic-design-company/)

### Media
- Logo used was created from [Logo Maker App for iphone](https://apps.apple.com/us/app/logo-maker-create-a-design/id1143390028) 
- I placed am embos effect of the logo with Photoshop to create the background image for the Bootstrap Jumbotron.
- The photos used in this site were obtained from [Pexels](https://www.pexels.com/), [Pinterest](https://www.pinterest.ie/) and [Unsplash](https://unsplash.com/)

### Acknowledgements

- Bootstrap 2 row navbar [codeply](https://www.codeply.com/go/05hEHoiUvv)

- Colorscheme of site inspired from Artsy and Creative on [VISME](https://visme.co/blog/website-color-schemes/)

