-- SQL script that creates a trigger that decreases qty
CREATE TRIGGER dec_q AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.quantity WHERE name=NEW.item_name;
