# Vittoria Ecommerce
![alt text](docs/pp5_readme-splash.png "Vittoria App mockup")

## Introduction

Vittoria Ecommerce is an online store written using the Python Django Framework. It allows an individual to easily browse a catalog of clothing and household furnishings, select items to purchase, and to pay and arrange delivery, all in a secure and convenient manner. Throughout the process the individual can visibly track items in their shopping cart and see the amount due. Upon purchase, a confirmation email is sent.

For the store owner, a means is provided to edit and maintain the store catalog.

[Here is a link to the application](https://tf-vittoria.herokuapp.com/)

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
#

![alt text](docs/showcase.png "Vittoria Showcase")

Upon landing on the site main page, the shopper is presented with a carousel called the Showcase, to highlight items the shop is promoting. From there a user may click on a product so get more detail, add to the shopping cart or select one of the options to view items by category.

![alt text](docs/popular.png "Vittoria Popular Items")

Similarly, a secondary feature shows up to nine items that are popular with shoppers, agin allowing them to select or add an item.

## Navigation
#

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
#
![alt text](docs/cart.png "Vittoria Shopping Cart")
#
The shopping cart displays a list of items that have been added for purchase. A shopper can remove items, change the quantity and proceed to checkout if desired.

## Checkout
#
![alt text](docs/checkout.png "Vittoria Checkout")
#
On this page, the shopper confirms the amount payable, the shipping address, and the credit card information. This is passed securely to the Stripe Payment Processor, without any financial information saved in the store.


The above represents the basic workflow of the site. There are other features such as adding items to the favorites list, which is achieved by clicking on the heart symbol on the top right of each image, as well as a quick add to shopping cart, denoted by the cart symbol on each image.

A full login log out system, with password reset is provided.

A chat page, with a link to the store page is provided.


## Catalog Maintenance
#
If an Administrator logs in, a new category called 'Add Product' appears in the top navigation bar.
Additionally, an edit symbol is displayed over each existing item image, to allow the Admin, to edit or delete an item.

## Business Model
#
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
#

- AWS to store static files

- Elephant SQL for Postgres Database

- Stripe for payment system

- Heroku for Deployment

- Github, Gitpod, VS Code, Django

## Testing
#

- Tested for responsiveness on desktop and mobile platforms.

- Automated Python tests in the application.

- Multiple purchases made during testing, to check input validation, arithmetic calculations, and credit card processing. No errors were found.

## Attribution
#

The first source is Code Institute, whose ecommerce tutorial was indispensible.
In addition, I had the benefits of a mentor Ashit, and a fellow student Atit, who provided useful guidelines and hints.
Google, Slack, Stack Overflow were geat sources of specif code snippets and examples which aided me.
I would like to thank all who assisted me in this project.

