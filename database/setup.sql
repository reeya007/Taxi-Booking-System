CREATE DATABASE TaxiBooking;

USE TaxiBooking;

CREATE TABLE Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Drivers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    license_number VARCHAR(15) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    pickup_location VARCHAR(255) NOT NULL,
    dropoff_location VARCHAR(255) NOT NULL,
    trip_date DATETIME NOT NULL,
    driver_id INT DEFAULT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(id)
);
