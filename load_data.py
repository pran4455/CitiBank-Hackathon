import sys
import csv
import os
from database import Base, Accounts, Customers, Users, CustomerLog, Transactions
from sqlalchemy import create_engine, text  # Import text
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))
bcrypt = Bcrypt(app)

def accounts():
    usern = 'C00000001'
    name = 'ramesh'
    usert = 'executive'
    passw = 'Ramesh@001'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    
    # Wrap raw SQL query in text()
    db.execute(text("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)"), 
               {"u": usern, "n": name, "t": usert, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    
    usern = 'C00000002'
    name = 'suresh'
    usert = 'cashier'
    passw = 'Suresh@002'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    
    db.execute(text("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)"), 
               {"u": usern, "n": name, "t": usert, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    
    usern = 'C00000003'
    name = 'mahesh'
    usert = 'teller'
    passw = 'Mahesh@003'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    
    db.execute(text("INSERT INTO users (id,name,user_type,password) VALUES (:u,:n,:t,:p)"), 
               {"u": usern, "n": name, "t": usert, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
def get_maheshs_customer_id():
    # Query to find Mahesh's customer ID
    maheshs_customer = db.execute(text("SELECT cust_id FROM customers WHERE name = :name"), {"name": "mahesh"}).fetchone()
    
    if maheshs_customer:
        print(f"Mahesh's customer ID is: {maheshs_customer[0]}")
    else:
        print("Mahesh not found in the customers table.")

if __name__ == "__main__":
    #accounts()
    usern = 'C00000003'
    name = 'mahesh'
    usert = 'teller'
    passw = 'Mahesh@003'
    passw_hash = bcrypt.generate_password_hash(passw).decode('utf-8')
    address = '123 Main Street'
    age = 30
    state = 'State1'
    city = 'City1'
    status = 'active'
    db.execute(text("INSERT INTO customers (cust_ssn_id, name, address, age, state, city, status) VALUES (:ssn, :n, :a, :ag, :st, :c, :status)"), 
               {"ssn": 123456789, "n": name, "a": address, "ag": age, "st": state, "c": city, "status": status})
    
    db.commit()
    print("Mahesh added to both users and customers tables.")
    get_maheshs_customer_id()