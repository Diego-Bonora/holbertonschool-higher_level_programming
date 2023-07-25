-- create User

CREATE USER if not exists "user_0d_1"@"localhost" IDENTIFIED BY "user_0d_1_pwd";
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
FLUSH PRIVILEGES;