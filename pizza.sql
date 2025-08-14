CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE employees (
    employee_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50),
    role NVARCHAR(30),
    salary DECIMAL(8,2) CHECK (salary > 0)
);

CREATE TABLE pizzas (
    pizza_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50),
    price DECIMAL(5,2) CHECK (price >= 0),
    category NVARCHAR(20),
);

CREATE TABLE suppliers (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
);

CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    employee_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE order_items (
    order_id INT,
    pizza_id INT,
    quantity INT CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id)
);

IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_NAME = 'pizzas' AND COLUMN_NAME = 'supplier_id'
)
BEGIN
    ALTER TABLE pizzas ADD supplier_id INT NULL;
END

INSERT INTO customers (name, phone) VALUES ('Максим Мотев', '89610403634');
INSERT INTO customers (name, phone) VALUES ('Егор Васильев', '89123456789');
INSERT INTO customers (name, phone) VALUES ('Александр Пушкин', '89987654321');

INSERT INTO employees (name, role, salary) VALUES ('Алексей Скутин', 'Повар', 30000);
INSERT INTO employees (name, role, salary) VALUES ('Артём Попов', 'Курьер', 20000);

INSERT INTO pizzas (name, price) VALUES (N'пепперони', 450);
INSERT INTO pizzas (name, price) VALUES (N'маргарита', 750);
INSERT INTO pizzas (name, price) VALUES (N'гавайская', 650);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (1, GETDATE(), 2);
DECLARE @orderId1 INT = SCOPE_IDENTITY();

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(@orderId1, 1, 1),
(@orderId1, 2, 1);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (2, GETDATE(), 1);
DECLARE @orderId2 INT = SCOPE_IDENTITY();

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES (@orderId2, 2, 2);

UPDATE customers SET phone = '89891234567' WHERE customer_id = 3;

UPDATE pizzas SET category = N'Классическая' WHERE pizza_id = 1;
UPDATE pizzas SET category = N'Острая' WHERE pizza_id = 2;
UPDATE pizzas SET category = N'Экзотическая' WHERE pizza_id = 3;

INSERT INTO suppliers (name, phone) VALUES ('Поставщик Семён', '89991234567');
INSERT INTO suppliers (name, phone) VALUES ('Поставщик Олег', '89997654321');

IF EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_Pizzas_Suppliers'
)
BEGIN
    ALTER TABLE pizzas DROP CONSTRAINT FK_Pizzas_Suppliers;
END

UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (1);
UPDATE pizzas SET supplier_id = 2 WHERE pizza_id IN (2);
UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (3);

ALTER TABLE pizzas
ADD CONSTRAINT FK_Pizzas_Suppliers FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

DELETE FROM orders WHERE order_date < DATEADD(day, -1, CAST(GETDATE() AS DATE));

DELETE FROM customers WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM orders
);

UPDATE pizzas SET price = price * 1.15;

BEGIN TRANSACTION;

IF EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_Pizzas_Suppliers'
)
BEGIN
    ALTER TABLE pizzas DROP CONSTRAINT FK_Pizzas_Suppliers;
END

UPDATE pizzas SET supplier_id = NULL WHERE supplier_id IS NOT NULL;

TRUNCATE TABLE suppliers;

ALTER TABLE pizzas
ADD CONSTRAINT FK_Pizzas_Suppliers FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

COMMIT;

SELECT * FROM pizzas;

SELECT 
    p.name AS pizza_name,
    SUM(oi.quantity) AS total_ordered
FROM 
    order_items oi
JOIN 
    pizzas p ON oi.pizza_id = p.pizza_id
GROUP BY 
    p.name;
