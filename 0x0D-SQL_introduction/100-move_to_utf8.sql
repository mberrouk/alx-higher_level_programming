-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- For each database:
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- For each table:
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER COLLATE utf8mb4_unicode_ci;
-- For each column:
ALTER TABLE hbtn_0c_0.first_table CHANGE name name VARCHAR(256) CHARACTER COLLATE utf8mb4_unicode_ci;
