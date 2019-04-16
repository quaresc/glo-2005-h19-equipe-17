USE glo_2005;

delimiter //
CREATE PROCEDURE UpdateProductsRating()
DETERMINISTIC
READS SQL DATA
BEGIN 
    DECLARE avg_rating INTEGER;
	DECLARE productId INTEGER;
	DECLARE reading_complete integer DEFAULT FALSE;
	DECLARE curs CURSOR FOR SELECT id FROM products;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET reading_complete = TRUE;

	CREATE TABLE IF NOT EXISTS liste (nom char(20), moyenne double);
	OPEN curs;
	reader: LOOP
		FETCH curs INTO productId;
		IF reading_complete THEN
		   LEAVE reader;
		END IF;

		SELECT AVG(rating)
		INTO avg_rating
		FROM reviews
		WHERE product_id = productId;

		UPDATE products
		SET rating = avg_rating
		WHERE id = productId;

	END LOOP reader;
	CLOSE curs;
END;//
delimiter ;
