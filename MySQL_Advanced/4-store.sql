-- Task four
-- updates inventory of items after orders are made
CREATE TRIGGER update_inventory
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name