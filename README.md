# Inventory management system

## About

Youtube : [Project Overview](https://youtu.be/cMA1q_wHJv4)

This project aims covers application with Database, models, Views, templates with CRUD functionality.

I have implemented an inventory management system using Django to efficiently manage products, stock levels, suppliers and sales the system should support crud operations for product and suppliers, facilitate stock management and enable tracking of sales order.

I have used django as a backend and for front-end it involves HTML CSS JavaScript with the django template that is jinja. For the database I have used mysql or sqlite 

## Database model parameters

- product which consists of name description category price stock quantity and supplier
- supplier table which contains name email phone number and address
- sales order that contains product quantity total price sales data and status
- stock movement that contains product quantity movement type movement date and notes

## Tasks

The application is allows you to add product ,list product, add supplier, list supplier, add stock movements ,create sales order, cancel sales order ,complete sales order, list sales order and stock level check.

## Run project

*Note: Recommended to use virtual environment for the application.*

### From Project

1. Install dependecy : `pip install -r requirements.txt`
2. Run the django application : `python manage.py runserver`
3. check project on `http://localhost:8000/`

### From Docker

1. Build the application image : `docker-compose build`
2. Create container out of the image: `docker-compose up -d`
3. check project on `http://localhost:8000/`
