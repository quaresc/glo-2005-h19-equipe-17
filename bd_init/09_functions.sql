USE glo_2005;

delimiter //
CREATE FUNCTION GetTotalCart (userId INTEGER)
RETURNS  DECIMAL(5, 2) 
DETERMINISTIC
READS SQL DATA
BEGIN 
    DECLARE total DECIMAL(5,2); 

    SELECT SUM(p.price)
    INTO total
    FROM  products p, carts c
    WHERE c.user_id = userId && p.id = c.product_id;

    RETURN total; 
END;//
delimiter ;
