alter table products
Add CONSTRAINT fk_categories_products
FOREIGN KEY (Categoryid) REFERENCES categories(id)