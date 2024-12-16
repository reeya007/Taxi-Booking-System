CREATE DATABASE TaxiBooking;

USE TaxiBooking;

CREATE TABLE Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(15),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Drivers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    license_number VARCHAR(15),
    phone_number VARCHAR(15),
    is_available BOOLEAN DEFAULT TRUE
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    pickup_location VARCHAR(255),
    dropoff_location VARCHAR(255),
    trip_date DATETIME,
    driver_id INT DEFAULT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(id)
);
