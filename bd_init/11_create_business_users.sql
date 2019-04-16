USE glo_2005;

CREATE USER 'businessman'@'%' IDENTIFIED BY 'businessman1234';
GRANT SELECT ON users_view TO 'businessman'@'%' ;
GRANT SELECT ON products_view TO 'businessman'@'%' ;
GRANT SELECT ON invoices_view TO 'businessman'@'%' ;
