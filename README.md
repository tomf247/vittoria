# Vittoria Ecommerce

![alt text](docs/pp5_readme-splash.png "Vittoria App mockup")

## Introduction

Vittoria Ecommerce is an online store written using the Python Django Framework. It allows an individual to easily browse a catalog of clothing and household furnishings, select items to purchase, and to pay and arrange delivery, all in a secure and convenient manner. Throughout the process the individual can visibly track items in their shopping cart and see the amount due. Upon purchase, a confirmation email is sent.

For the store owner, a means is provided to edit and maintain the store catalog.

[Here is a link to the application](https://tf-vittoria.herokuapp.com/)
## Purpose and Value Proposition

Vittoria Ecommerce Our has been developed to provide our customers with a convenient and enjoyable shopping experience. We offer a wide selection of high-quality products at competitive prices, and provide fast and responsive customer service and support.

We seek to be the go-to destination for customers seeking a diverse range of products, from fashion and beauty to home and electronics. We believe that shopping should be easy and stress-free, and we are committed to creating a user-friendly online platform that meets the needs of all customers.

We establish trust with our customers, by providing transparency, honesty, and integrity in all aspects of our business. We believe that building trust with our customers is essential to our success, and we work tirelessly to earn and maintain that trust.

We are dedicated to continuously improving our website and offerings, and to staying on the cutting edge of ecommerce technology to ensure our customers have the best possible experience.

### Key Distinguishers

- Customer-centric approach: Vittoria eCommerce provides a positive and convenient shopping experience for our customers.

- Wide range of products: Our product offerings are selected to attract our target customer's needs and wishes.

- High-quality products: Our products stand out from competitors who may focus more on quantity than quality.

- Competitive pricing: We offer competitive pricing without sacrificing product quality.

- Exceptional customer service: In order to  prioritize the needs of our customers we recognize the need for strong and reliable customer service.

- Trust and transparency: The importance of trust and transparency in our business is a core value, allowing us to build credibility with our customers.

- Ongoing improvement: We continuously improve and refine our offering to reflect market trands and directions.


## Planning & Design Process

Several key factors were considered to ensure that the final product met the needs of the target audience. These factors included:

- User experience: The design process prioritized creating an intuitive and easy-to-use platform that would provide a seamless shopping experience for customers.

- Accessibility: The website had to be accessible to all users, regardless of their abilities or devices. This involved considering factors such as font size, color contrast, and keyboard navigation.

- Brand identity: The design process emphasized creating a visual identity that would communicate the brand's values and personality, and differentiate the website from competitors.

- Performance: Performance optimization was at the forefront throughout the design process, ensuring that the website was fast and responsive, with quick load times and minimal lag.

- Security: Security measures were considered, such as encryption and secure login systems, to protect user data and ensure customer trust.

## Initial Wireframe

![Wireframe](docs/vittoria_wireframe.png "Wireframe")
I used [app.diagrams.net](https://app.diagrams.net) for the initial mockup. The sketch can be re-used or modified [here](docs/vittoria_app.diagrams.drawio)


## Features
#

- User login/logout with password reset.

- Product catalog maintenance for staff.

- Purchase items without creating an account.

- Live Chat (Facebook)

- Wishlist

- Add items to a favorites list.

- Newsletter

- Email confirmations.

- Responsive layout.

## Usage

![alt text](docs/showcase.png "Vittoria Showcase")

Upon landing on the site main page, the shopper is presented with a carousel called the Showcase, to highlight items the shop is promoting. From there a user may click on a product so get more detail, add to the shopping cart or select one of the options to view items by category.

![alt text](docs/popular.png "Vittoria Popular Items")

Similarly, a secondary feature shows up to nine items that are popular with shoppers, agin allowing them to select or add an item.

## Navigation

![alt text](docs/topnav.png "Vittoria Nav Bar")

The following features sit in the top navigation area: 

- Proceed directly to the shop. 

- View products by category. 

- Add Product (N.B. visibly only to the shop Admin).

- Search for Product.

- View Favorites List.

- View Shopping Cart.

- Log in/out.

## Shopping Cart

![alt text](docs/cart.png "Vittoria Shopping Cart")

The shopping cart displays a list of items that have been added for purchase. A shopper can remove items, change the quantity and proceed to checkout if desired.

## Checkout

![alt text](docs/checkout.png "Vittoria Checkout")

On this page, the shopper confirms the amount payable, the shipping address, and the credit card information. This is passed securely to the Stripe Payment Processor, without any financial information saved in the store.

The above represents the basic workflow of the site. There are other features such as adding items to the favorites list, which is achieved by clicking on the heart symbol on the top right of each image, as well as a quick add to shopping cart, denoted by the cart symbol on each image.

A full login log out system, with password reset is provided.

A chat page, with a link to the store page is provided.

## Catalog Maintenance

If an Administrator logs in, a new category called 'Add Product' appears in the top navigation bar.
Additionally, an edit symbol is displayed over each existing item image, to allow the Admin, to edit or delete an item.

## Business Model

The objective of the store is to generate sales in the young adult market, by featuring products that are appealing to them, moderately priced, and delivering them in a timely fashion.

Social media such as Facebook, Twitter and Instgram are used to spread brand awareness.

Specials and promos are prominently featured.

A mailing list is maintaintained, kept relevant and regularly sent. Comments and feedback are actively sought.

Print media is used occasionaly in varying markets.

Goodie bags, promo items (stash) are given out at social events, such as night clubs, shopping malls etc.

Frequent meetings with suppliers and logistics firms to avail of new markets and opportunities.
## Facebook Page
#
[The Facebook page is here ](https://facebook.com/tf-vittoria)

## Platform

- AWS to store static files

- Elephant SQL for Postgres Database

- Stripe for payment system

- Heroku for Deployment

- Github, Gitpod, VS Code, Django


## Deployment

The project was deployed to Heroku, and in order to remain within the Free Tier,  the Postgres Database was hosted at Elephant SQL. Additionally, static and media files were hosted on Amazon Cloud. This combination allows for a free website, provided usage rates are not exceeded.

1. Create an [AWS S3 Bucket](https://aws.amazon.com/s3/) (For media)
2. Create an account at [Heroku](https://heroku.com) (For the Django App)
3. Create an account at [ElephantSQL](https://elephantsql.com) (Select "Tiny Turtle" for PostgreSQL tier).
4. Create an account at [Stripe](https://stripe.com) (Obtain Developer Keys)
5. When these elements are added, you will need to point the app to the correct values. This is done by setting the Config Variables (Reveal Config Vars) in Heroku:

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | your AWS bucket ID
 AWS_SECRET_ACCESS_KEY | your AWS secret key
 DATABASE_URL | your ElephantSQL Postgres database url
 EMAIL_HOST_PASS | your password to use your gmail account for emails
 EMAIL_HOST_USER | your email address
 SECRET_KEY | secret key used for your Django project
 STRIPE_PUBLIC_KEY | obtained through your Stripe account
 STRIPE_SECRET_KEY | obtained through your Stripe account
 STRIPE_WH_SECRET | obtained through your Stripe account
 USE_AWS | True

6. In you Git root folder, create a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
7. Create a Procfile as follows:
```
echo web: gunicorn vittoria.wsgi:application > Procfile
```
8. The Postgres database is initialised and sync'd with these commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
9. Create a superuser.
```
python3 manage.py createsuperuser
```
10. Log in to Heroku from the terminal using this command and enter your details when prompt:
```
heroku login -i
```
11. Once logged in, link your Heroku app created above as the remote repository with this command:
```
heroku git:remote -a <your app name here>
```
12. Complete the deployment by pushing the projekt to Heroku:
```
git push heroku main
```

## Testing

### General

- Overview:
Vittoria eCommerce was tested to evaluate its user experience, functionality, and performance. The website offers a wide range of products, including fashion, beauty, home, and electronics, and aims to provide a convenient and enjoyable shopping experience for customers.

- Testing Methodology:
The website was tested using manual testing methods on both desktop and mobile devices. The testing process involved evaluating the website's functionality, user interface, navigation, content, and performance.

- Functionality:
All features and functionalities of the website were tested to ensure that they are working as intended. Testing involved adding products to the shopping cart, checking out, creating an account, logging in and out, and contacting customer support. No significant issues were found during the testing process.

- User Interface:
The user interface of the website was evaluated for its ease of use, navigation, and aesthetics. The testing process involved assessing the layout, font size, color scheme, and button placement. The website's user interface was found to be intuitive, well-organized, and visually appealing.

- Navigation:
The website's navigation was tested to ensure that it is easy to use and that all pages are accessible. Testing involved assessing the site's menu structure, page links, and search functionality. The website's navigation was found to be straightforward, and all pages and features were easily accessible.

- Content:
The website's content was evaluated for accuracy, completeness, and relevance. Testing involved reviewing product descriptions, prices, and customer reviews. The website's content was found to be accurate, complete, and relevant to the products offered.

Certain products lack a full size image for display, but can be amended by the Admin as soon as better images are available.

- Performance:
The website's performance was tested to ensure that it is responsive and fast-loading. Testing involved assessing page load times, server response times, and overall website speed. The website's performance was found to be fast and responsive, with quick page load times and server response times.

- Conclusion:
Overall, Vittoria eCommerce performed well during testing, with no significant issues found. The website's functionality, user interface, navigation, content, and performance were all evaluated and found to be satisfactory. The website provides a convenient and enjoyable shopping experience for customers, with a wide range of products, competitive pricing, and exceptional customer service.

### Logical Testing

- The Home folder contains a tests.py containing the following validation test cases. They completed satisfactorily.

```
class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        response = self.client.post("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

class SignupFormTest(TestCase):
    def test_form_validation(self):
        form = SignupForm({
            'email': 'test@example.com',
            'username': 'admin',
            'password1': 'vittoria@user',
            'password2': 'vittoria@user',
        })
        
        self.assertTrue(form.is_valid())
      
        
    def test_form_invalid_missing_email(self):
        form = SignupForm({
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

class EditProductFormTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='test product',
            description='test description',
            price=10.99,
        )

    def test_form_validation(self):
        form = EditProductForm(data={'name':'test product', 'description':'test description', 'price':10.99}, instance=self.product)
        self.assertTrue(form.is_valid())
    
    def test_form_invalid_missing_name(self):
        form = EditProductForm({
            'description': 'test description',
            'price': 10.99,
        }, instance=self.product)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

class NewsletterFormTest(TestCase):
    def test_form_validation(self):
        form = NewsletterForm({
            'emails': 'test@example.com',
        })
        self.assertTrue(form.is_valid())

```
### CSS Testing

- Running the site through [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftf-vittoria.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) produces only one error message related to Font Awsome, and a bug report exists on Github at https://github.com/FortAwesome/Font-Awesome/issues/19423

### HTML Testing

- The site was run through [The W3C HTML Validation Service](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftf-vittoria.herokuapp.com%2F) 

- HTML errors have been noted and investigated. Although not desirable they have been found to have no functional impact in the website, as curently implemented. Nonetheless, a [Github Issue](https://github.com/tomf247/vittoria/issues/8) has been generated and will be addressed in the next fix cycle.

### Linting

- Flake8, a module that is used in Gitpod was used to check and format the Python code. Changes were written back to each app.

## Compatibility Testing
### Using different browsers

The project has been  tested on the following web browsers, checking that all aspects worked as planned:

    Google Chrome
    Mozilla Firefox
    Apple Safari

### Using different devices

I tested this project on these devices:

    Acer Desktop on KDE Linux
    Apple iPhone 6
    Android 12 Poco Phone
    Android 11 Tablet 
    Lenove Laptop using Windows 10

## Data and Security

Data and security are crucial aspects of any website, and Vittoria eCommerce takes these matters seriously. The website has several measures in place to ensure the security of user data and protect against unauthorized access.

The website requires users to create an account and login to access certain features, such as the user profile and order history. User data is stored securely in a Postgres database hosted on Heroku, a trusted and reliable cloud hosting service. This database is encrypted and protected by a secure login system to prevent unauthorized access to user data.

In addition to protecting user data, the website also uses Stripe for payment processing. Stripe is a widely used and trusted payment processing platform that provides robust security measures to protect user payment information. The website does not store credit card information, further enhancing the security of user data.

To further enhance security, the website uses industry-standard SSL/TLS encryption to encrypt all data transmitted between the user's device and the website's servers. This ensures that all sensitive data, including login credentials and payment information, is protected from interception by unauthorized third parties.

The website also has a comprehensive security policy in place, including regular security audits and testing, to ensure that all security measures are up-to-date and effective. This policy covers all aspects of website security, from data storage and transmission to user authentication and access control.

In summary, Vittoria eCommerce takes data and security seriously and has implemented several measures to ensure the protection of user data. These measures include secure login systems, encryption of user data, use of trusted hosting and payment processing platforms, and a comprehensive security policy. Customers can be confident that their data is secure when using this website to make purchases.


# Marketing Plan
## Target Audience


Age: 21-35 years old

Gender: Male and Female

Location: United States (but other Englidh speaking countries also).

Income: $30,000 - $75,000 annually

Interests: Fashion, Technology, Health and Wellness, Social Media

By pursuing this target audience, the Vittoria ecommerce will tailor its marketing efforts to speak directly to this group's interests and needs, and create content that will resonate with them. This will increase the chances of driving traffic to the website and converting that traffic into sales.

## Marketing Goals
#

- Increase website traffic by 25% in the next quarter through SEO optimization, paid search ads, and content marketing.

- Increase sales revenue by 20% within the next six months through email marketing campaigns and social media advertising.

- Boost customer engagement by 15% by the end of the year through social media engagement, influencer partnerships, and user-generated content and reviews.

By setting these specific goals, Vittoria ecommerce can better measure the success of its marketing efforts and make informed decisions about future strategies. Each of these goals is measurable, has a set timeline, and is designed to help the business achieve its overall objectives.

## Competitors
#

- Identify key competitors in the same niche and research their marketing strategies, including the channels they use to reach their target audience and the types of content they create.

- Analyze the strengths and weaknesses of each competitor's marketing efforts and identify areas where the ecommerce store can differentiate itself from the competition.

- Monitor competitors' pricing strategies, promotions, and customer reviews to better understand how they are meeting the needs of their customers and where they may be falling short.


## Brand Identity
#

- Vittoria ecommerce store's brand identity will reflect its mission, values, and personality.

- The brand will have a clear and consistent message that resonates with the target audience.

- Vittoria ecommerce will have a unique and recognizable logo and color scheme that distinguishes it from competitors.

- The brand's messaging will be consistent across all channels, including social media, email marketing, and the website.

## Marketing Channels
#

## Social Media Marketing

- Vittoria ecommerce will use social media platforms such as Instagram, Facebook, and Twitter to promote its products and connect with its target audience.

## Email Marketing 
- The store will create an email list of subscribers and send out weekly newsletters featuring new product releases, promotions, and other updates.

## Content Marketing 
- The store will create blog posts and video content to provide valuable information and engage its audience, driving traffic to the website.

## Influencer Marketing
- The store will partner with relevant influencers on social media platforms to promote its products to their followers.

## Paid Advertising 
- The store will invest in paid search ads and social media ads to reach a wider audience and drive traffic to the website.


## Marketing Budget
- The budget in year one is $50,000, to be spent as follows:

### Social Media Marketing: $15,000
- The store will allocate the largest portion of its budget to social media marketing. This will include paying for sponsored posts and ads on Facebook, Instagram, and Twitter to promote its products and reach a wider audience.

### Email Marketing: $5,000
- The store will also invest in email marketing to promote its products and keep subscribers engaged. This will include creating a weekly newsletter featuring new products, promotions, and other updates.

### Content Marketing: $10,000 
- The store will create high-quality blog posts, product videos, and other content to engage its audience and attract new customers. This will include contracting a content team to produce the content.

### Influencer Marketing: $10,000 
- The store will partner with relevant influencers to promote its products to their followers. This will include paying for sponsored posts and product reviews on social media platforms.

### Paid Advertising: $10,000 
- The store will invest in paid search ads and social media ads to drive traffic to the website and reach a wider audience.

## Measurement and Optimization

- Usage of web analytics and conversion tracking to measure website traffic, customer engagement, and sales conversions. This will help to determine the effectiveness of each marketing channel and identify areas for improvement.

- Review of marketing plan on a regular basis, and making adjustments based on performance data to optimize the marketing efforts. This may involve shifting budget allocations to the most effective channels, adjusting the messaging or creative used in ads, or trying new marketing tactics.

- Usage A/B testing to test different marketing messages and tactics to determine the most effective strategies for reaching the target audience and driving sales.

- Monitoring of customer feedback, including reviews and comments on social media and other platforms, to identify areas for improvement and adjust the marketing plan accordingly.
#

## Assistance & Attribution

The first source of help and assistance is Code Institute, whose ecommerce tutorial was indispensible.
In addition, I had the benefits of a mentor Ashit, and a fellow student Atit, who provided useful guidelines and hints.
Google, Slack, Stack Overflow were geat sources of specific code snippets and examples which aided me.
I would like to thank all who assisted me in this project.
