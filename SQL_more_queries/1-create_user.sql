-- create User

CREATE USER if not exists "user_0d_1"@"localhost";
SET PASSWORD FOR "user_0d_1"@"localhost" = "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
FLUSH PRIVILEGES;