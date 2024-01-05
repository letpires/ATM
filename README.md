<p align="center">
  <img src="https://github.com/letpires/ATM/blob/main/atm_image.png" >
</p>

## 🏦 Description
This project is an automated teller machine (ATM) simulator implemented in Python. It offers an interactive experience, allowing users to simulate basic banking operations.

## 📄 Repository structure

- ATM project without database connection [ATM WITHOUT DB](https://github.com/letpires/ATM/blob/main/atm_bank_%7BNO_db_%20connection%7D.py);
- ATM project with database connection [ATM WITH DB CONNECTION](https://github.com/letpires/ATM/blob/main/atm_bank_%7Bdb_%20connection%7D.py);
- Script SQL para conexão do simulador [SCRIPT SQL](https://github.com/letpires/ATM/blob/main/script_sql.sql).

## 🚀 Features

- **User Options Menu:** allows the user to carry out various banking operations;
- **Admin options menu:** administrative access for advanced settings (Admin account: 211001; PIN: 123);
- **Account Operations:** account balance, deposit, withdrawal;
- **History of banking transactions;**
- **Generation of number of transactions:** each transaction receives a unique number;
- **Data visualization:** graphs to represent the account balance over time;
- **Number of fixed accounts:** predefined accounts for simulation.

  
## ⚡️ Requirements

To run this ATM simulator project in Python, you need to have **Python 3** installed on your machine. Furthermore, the project depends on some specific libraries. It is essential to have the `mysql-connector-python` library installed to manage the connection to the MySQL database. For calculation and data visualization functionalities, the **numpy** and **matplotlib** libraries are equally important. Make sure you have all of these dependencies installed to ensure the simulator works correctly.

## Configuration

1. Clone the repository;
2. Install dependencies;
3. Execute ATM simulator.

## Database access

To configure the database for the ATM simulator, follow these steps:

### 1. Running the Configuration SQL Script

Before using the simulator, you must configure the database by running an SQL script. This script will create the necessary tables and structures in your database.

- Open your database management system (such as MySQL Workbench, pgAdmin, etc.).
- Connect to your local database.
- Run the SQL script available in this repository - [CLICK HERE TO ACCESS](https://github.com/letpires/ATM/blob/main/script_sql.sql).

### 2. Changing Database Credentials in Simulator Code

- Open the [ATM file](https://github.com/letpires/ATM/blob/main/atm_bank_%7Bdb_%20connection%7D.py) and look for the function **CreateConnection()**;
- Change the connection information to match your local database credentials.
- Save the file with the new settings.

## ⚡ Contribution

Your contribution is very welcome in this project! If you have ideas to improve the ATM simulator or want to add new features, feel free to suggest changes.

## 🔥 Challenge Coming Soon!

Stay tuned: in the next few days, I will launch a challenge related to this project. It will be an excellent opportunity to test your skills, collaborate and possibly see your ideas being implemented. More details will be shared soon on my social media and GitHub.

-- 

Made with 💜 by Letícia Pires :wave: 
