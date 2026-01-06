
INSERT INTO users (name,email) VALUES ('Alice','alice@mail.com');
INSERT INTO orders (user_id,amount,status) VALUES (1,120,'CREATED');
UPDATE orders SET status='PAID' WHERE id=1;
DELETE FROM users WHERE id=1;
