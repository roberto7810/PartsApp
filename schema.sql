-- This file contains the definitions of the tables used in the application.
--
-- Items table
create table items(item_id serial primary key, resource_name varchar(20), brand varchar(10), item_latitud varchar(10), item_longitud varchar(10), expiration_date int, price float, type varchar(20), amount int);

-- Card table
create table cards(card_id serial primary key, card_number char(16), card_holder varchar(20), card_expiration_date int, card_cvv int);

-- person table
create table person(person_id serial primary key, person_name varchar(10), person_latitud varchar(10), person_longitud varchar(10), phone_num varchar(10), card references cards(card_id), gender varchar(10), age int);

-- privileges table
create table privileSges(person_id integer references person(person_id), admin boolean, requester boolean, supplier boolean);

-- inventory table
create table inventory(inventory_id serial primary key, item_id integer references items(item_id) requester_id integer references person(person_id),
supplier_id integer references person(person_id), available boolean);
