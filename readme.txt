• install package
pip install -U flask-cors

• 測試時使用postman
http://localhost:5000/login 
Post 
Parameters: Body Content Type -> Raw Input -> JSON 
{"username":"skillchen","password":"aq"}



•Create table

drop table useraccount
CREATE TABLE useraccount (
	id serial PRIMARY KEY,
	username VARCHAR ( 100 ) NOT NULL,
	password VARCHAR ( 300 ) NOT NULL
);

Insert data

INSERT INTO useraccount (username, password) VALUES ('tutorial101', 'pbkdf2:sha256:150000$KxxiGerN$4c37a656baa0034035a6be2cd698b5da8b036ae63eef3ab0b08b9c18b9765648');
INSERT INTO useraccount (username, password) VALUES ('skillchen'  , 'pbkdf2:sha256:260000$9lv3PyExtU2c2Yb8$8009c625f55c646f4060d17a86910143a0df221d6254dcdcc3812b14014b106c');

{"username":"tutorial101","password":"cairocoders"}
{"username":"skillchen","password":"aq"}

select * from useraccount;


Username : tutorial101
password : cairocoders