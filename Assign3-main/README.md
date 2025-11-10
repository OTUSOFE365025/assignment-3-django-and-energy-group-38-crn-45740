## Responsibility Matrix
| Name | ID | Responsibility |
| :--- | :---: | :---: |
| Tavan Mohammed | 100906916 |  Code |
| William Lévesque | 100916180 | Energy efficiency |
| Saif Siddiqui | 100862747 | Energy efficiency  |


# Assignment 3 — Cash Register using Django ORM

This project implements part of a Cash Register system using the Django ORM without running a full Django web server. The goal is to demonstrate how Django’s database layer can be used in a standalone Python application.

The system supports:

- Populating the database with product UPC codes, names, and prices  
- Scanning (entering) a UPC through a Django Form  
- Looking up the product using the Django ORM  
- Displaying the product name and price to the user  

This work is based on the Django-ORM starter template provided by GitHub Classroom.

---

## 📂 Project Structure

project/
├── db/
│ ├── models.py # Product model (UPC, name, price)
│ └── init.py
├── forms/
│ └── scan_form.py # Django Form for UPC input
├── main.py # Program entry point (scan + lookup logic)
├── manage.py # Django migration tool
├── settings.py # Django configuration
└── README.md

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-38-crn-45740.git
cd assignment-3-django-and-energy-group-38-crn-45740
```
### 2. Create & Activate Virtual Environment
Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```
Windows
```
python -m venv venv
venv\Scripts\activate
```
Install Django
```
pip install django
```
### 3. Run Migrations
```
python manage.py makemigrations db
python manage.py migrate
```
### 4. Add Sample Products (Example)
```
from db.models import Product
Product.objects.create(upc="012345678905", name="Milk", price=3.99)
```
### 5. Run the Program
```
python main.py
source venv/bin/activate
```
Example Output
Enter UPC: 012345678905
Product Found:
Name: Milk
Price: $3.99
