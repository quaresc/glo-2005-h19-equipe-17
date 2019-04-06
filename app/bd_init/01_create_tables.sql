CREATE DATABASE glo_2005;
USE glo_2005;

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  username VARCHAR(45) NOT NULL,
  email VARCHAR(320) NOT NULL,
  password CHAR(64) NOT NULL,
  ip_address INT UNSIGNED NOT NULL,
  registration_date TIMESTAMP NOT NULL,
  activated TINYINT(1) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX username_UNIQUE (username ASC),
  UNIQUE INDEX email_UNIQUE (email ASC)
);


DROP TABLE IF EXISTS product_types;

CREATE TABLE IF NOT EXISTS product_types (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX name_UNIQUE (name ASC)
);

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS products (
  id INT NOT NULL AUTO_INCREMENT,
  ean VARCHAR(13) NOT NULL,
  name VARCHAR(250) NOT NULL,
  description VARCHAR(1000) NOT NULL,
  product_type_id INT NOT NULL,
  company VARCHAR(45) NOT NULL,
  price DOUBLE(5,2) NOT NULL,
  rating TINYINT(1) UNSIGNED NOT NULL,
  weight DOUBLE(5,2) NOT NULL,
  quantity INT UNSIGNED NOT NULL,
  image_url TEXT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX ean_UNIQUE (ean ASC),
  INDEX fk__products__products_types_idx (product_type_id ASC),
  CONSTRAINT fk__products__product_types
    FOREIGN KEY (product_type_id)
    REFERENCES product_types (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

DROP TABLE IF EXISTS invoices;

CREATE TABLE IF NOT EXISTS invoices (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_date TIMESTAMP NOT NULL,
  PRIMARY KEY (id),
  INDEX fk__invoices__users_idx (user_id ASC),
  CONSTRAINT fk__purchase_histories__users
    FOREIGN KEY (user_id)
    REFERENCES users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


DROP TABLE IF EXISTS carts;

CREATE TABLE IF NOT EXISTS carts (
  user_id INT NOT NULL,
  product_id INT NOT NULL,
  INDEX fk__carts__users_idx (user_id ASC),
  INDEX fk__carts__products_idx (product_id ASC),
  CONSTRAINT fk__carts__users
    FOREIGN KEY (user_id)
    REFERENCES users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk__carts__products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


DROP TABLE IF EXISTS reviews;

CREATE TABLE IF NOT EXISTS reviews (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  product_id INT NOT NULL,
  title VARCHAR(45) NULL,
  comment VARCHAR(400) NULL,
  rating INT NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  PRIMARY KEY (id),
  INDEX fk__reviews__users_idx (user_id ASC),
  INDEX fk__reviews__products_idx (product_id ASC),
  CONSTRAINT fk__reviews__users
    FOREIGN KEY (user_id)
    REFERENCES users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk__reviews__products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


DROP TABLE IF EXISTS invoice_products;

CREATE TABLE IF NOT EXISTS invoice_products (
  invoice_id INT NOT NULL,
  product_id INT NOT NULL,
  INDEX fk__invoice_products__products_idx (product_id ASC),
  INDEX fk__invoice_products__invoice_idx (invoice_id ASC),
  CONSTRAINT fk__invoice_products__products
    FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk__invoice_products__invoices
    FOREIGN KEY (invoice_id)
    REFERENCES invoices (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);