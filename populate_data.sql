CREATE DATABASE ticketing;
USE ticketing;
CREATE TABLE ticket_sales (
    ticket_id INT,
    trans_date DATE,
    event_id INT,
    event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL,
    num_tickets INT
);

CREATE USER 'steven'@'localhost' IDENTIFIED BY 'springboard';
GRANT ALL PRIVILEGES ON ticketing.* TO 'steven'@'localhost' WITH GRANT OPTION;