DROP DATABASE IF EXISTS megaPass;

CREATE DATABASE megaPass;

USE megaPass;

DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (appName varchar(100), encPass varchar(1024), dkey varchar(1024), userEmail varchar(100),userName varchar(100), url varchar(100));