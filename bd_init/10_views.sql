USE glo_2005;

CREATE VIEW users_view AS
	SELECT first_name, last_name, username, email, activated
    FROM users;

CREATE VIEW products_view AS
	SELECT p.ean, p.name, p.description, t.name as product_type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
    FROM products p, product_types t
    WHERE p.product_type_id = t.id;

CREATE VIEW invoices_view AS
		SELECT u.username as user, p.name, ip.quantity, i.transaction_date
		FROM users u, invoices i, products p, invoice_products ip
		WHERE i.user_id=u.id && ip.product_id=p.id && i.id=ip.invoice_id;