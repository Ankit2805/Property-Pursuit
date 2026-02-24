Property Pursuit website is a web application that facilitates the search of properties. 
The System has features such as user registration, property
listing, property search, booking request, and admin dashboard. The user
registration feature allows users to create an account on the System and provide
their contact details. The property listing feature allows property owners to list
their properties on the System and provide details such as the property address,
price, and photos. The property search feature allows users to search for
properties on the System by specifying criteria such as location, price, and
number of bedrooms. The rental request feature allows users to submit a rental
request for a property by providing their details to request for booking property.
The admin dashboard allows the admin to manage the System, Properties and its
Users.
<br>
<br>

<h2><b>🛠️ Database Setup & Local Development</b></h2>

This project uses **Django** with an **Apache MySQL** (XAMPP/WAMP) backend. Follow these steps to initialize the database:

### 1. Create Database
Open your MySQL terminal or [phpMyAdmin](http://localhost/phpmyadmin/) and execute:
```sql
CREATE DATABASE realestate;
```
<br>

### 2. Ensure your settings.py is configured to connect to MySQL:
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'realestate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
<br>

### 3. Run the following commands in your terminal to set up the schema and start the server:
```bash
# Navigate to project directory
cd realestate

# Generate database schema based on models
python manage.py makemigrations 

# Apply migrations to Apache MySQL
python manage.py migrate

# Start the development server
python manage.py runserver
```
<br>
<br>
<h2><b>Dealer</b></h2>
<img width="1893" height="906" alt="Screenshot 2025-07-24 150453" src="https://github.com/user-attachments/assets/5ee2bc1a-1fdb-48e5-a825-3f7a19a157b0" />
<br>
<br>
<img width="1912" height="901" alt="Screenshot 2025-07-24 150553" src="https://github.com/user-attachments/assets/9af1f6c7-ee94-4ddc-a436-9349931832c0" />
<br>
<br>
<img width="1916" height="904" alt="Screenshot 2025-07-24 150707" src="https://github.com/user-attachments/assets/af53e1b4-984e-489b-9e7a-b8ef7b2e3768" />
<br>
<br>
<img width="1912" height="903" alt="Screenshot 2025-07-24 150726" src="https://github.com/user-attachments/assets/f4b6da4b-32c3-43d3-a5d6-dd9e918c0f7c" />
<br>
<br>
<img width="1895" height="894" alt="Screenshot 2025-07-24 150743" src="https://github.com/user-attachments/assets/e4c2a846-fa6c-4f80-8da6-93312bd39369" />
<br>
<br>
<img width="1911" height="896" alt="Screenshot 2025-07-24 151048" src="https://github.com/user-attachments/assets/1b5937e1-1501-4d13-9be2-bb3e124eb686" />
<br>
<br>

<h2><b>Client</b></h2>
<img width="1897" height="904" alt="Screenshot 2025-07-24 151159" src="https://github.com/user-attachments/assets/84e0ab0c-23d1-4c44-a6da-64c1f46ea47e" />
<br>
<br>
<img width="1899" height="908" alt="Screenshot 2025-07-24 151606" src="https://github.com/user-attachments/assets/222a0de6-125b-47fd-b1ae-7416da1bbf4f" />
<br>
<br>
<img width="1902" height="900" alt="Screenshot 2025-07-24 151642" src="https://github.com/user-attachments/assets/e68f70a5-fde2-433d-af2f-8c40233d2e4c" />
<br>
<br>
<img width="1918" height="900" alt="Screenshot 2025-07-24 151759" src="https://github.com/user-attachments/assets/e58bafd0-d340-4238-8b63-e170d40b6aff" />
<br>
<br>

<h2><b>Admin</b></h2>
<img width="1919" height="901" alt="Screenshot 2025-07-24 152450" src="https://github.com/user-attachments/assets/23bc81f6-a049-4ebb-abd0-ef83a62e8c61" />
<br>
<br>
<img width="1900" height="901" alt="Screenshot 2025-07-24 152507" src="https://github.com/user-attachments/assets/7cd4eb73-5c23-4c6a-a308-9e3c1a3ccb34" />
<br>
<br>
<img width="1919" height="910" alt="Screenshot 2025-07-24 152730" src="https://github.com/user-attachments/assets/5ecfdfa9-aa82-4f3c-9e0f-8519b129fa86" />
