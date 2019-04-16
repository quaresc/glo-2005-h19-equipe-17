USE glo_2005;

delimiter //
CREATE DEFINER = CURRENT_USER TRIGGER invoice_products__update_quantity___AFTER_INSERT
AFTER INSERT ON invoice_products
FOR EACH ROW
BEGIN
	DECLARE product_quantity BIGINT DEFAULT 0;

	SELECT quantity
	INTO product_quantity
	FROM products
	WHERE id = NEW.product_id;
	
   	SET product_quantity = product_quantity - cast(NEW.quantity AS SIGNED);
    
	IF product_quantity < 0 THEN
	   SIGNAL SQLSTATE '45000'
	   SET MESSAGE_TEXT='Can not have a negative quantity for a product.';
	END IF;

	UPDATE products
	SET quantity = product_quantity
	WHERE id = NEW.product_id;
END;//
delimiter ;

delimiter //
CREATE DEFINER = CURRENT_USER TRIGGER reviews__update_rating__AFTER_INSERT
AFTER INSERT ON reviews
FOR EACH ROW
BEGIN
	DECLARE avg_rating INTEGER;

	SELECT AVG(rating)
	INTO avg_rating
	FROM reviews
	WHERE product_id = NEW.product_id;
	
	UPDATE products
	SET rating = avg_rating
	WHERE id = NEW.product_id;
END;//
delimiter ;

delimiter //
CREATE DEFINER = CURRENT_USER TRIGGER cart__quantity_zero__BEFORE_INSERT
BEFORE INSERT ON carts
FOR EACH ROW
BEGIN
	DECLARE product_quantity INTEGER DEFAULT 0;

	SET product_quantity = NEW.quantity;

	IF product_quantity <= 0 THEN
	   SIGNAL SQLSTATE '45000'
	   SET MESSAGE_TEXT='Can not have a quantity 0 for a product in a cart';
	END IF;
END;//
delimiter ;


delimiter //
CREATE DEFINER = CURRENT_USER TRIGGER cart__quantity_zero__BEFORE_UPDATE
BEFORE UPDATE ON carts
FOR EACH ROW
BEGIN
	DECLARE product_quantity INTEGER DEFAULT 0;

	SET product_quantity = NEW.quantity;

	IF product_quantity <= 0 THEN
	   SIGNAL SQLSTATE '45000'
	   SET MESSAGE_TEXT='Can not have a quantity 0 for a product in a cart.';
	END IF;
END;//
delimiter ;
