-- Task four
-- updates inventory of items after orders are made
UPDATE items
JOIN orders ON items.name = orders.item_name
SET items.quantity = items.quantity - orders.number;
