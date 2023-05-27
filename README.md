Roger

# Patient Details Management System

The Patient Details Management System is a web application that allows hospitals to store and manage patient information. It provides a portal for patients to access their checkup details, including prescriptions and reports. The application is built using Django and uses SQLite as the database.

## Features

- **Patient Registration**: Patients can register by providing their social security number (SSN) and other required details.

- **Login and Authentication**: Registered patients can securely log in to access their personal information and checkup details.

- **Checkup Details**: Patients can view their checkup details, including prescription details and medical reports, in a user-friendly interface.

- **Hospital Data Entry**: Authorized hospital staff can add and update patient information, including medical records and checkup details.

- **Secure Storage**: Patient data is securely stored in an SQLite database, ensuring data privacy and confidentiality.

## Installation

To set up the Patient Details Management System locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/jagadeeshkumar007/Roger.git
2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
3. Set up the SQLite database:
   ```shell
   python manage.py migrate
4. Start the Django development server:
   ```shell
   python manage.py runserver

 


