fsociety
========

The service is an SSH server that uses a MySQL database as backend (given its output).
After playing a little bit around, it turns out that there is a SQL injection in both, the username and the password.
The challenge description contains a hint that the password of user `elliot` is the flag.

Thus, with the `LIKE` operand one can leak the password of `elliot` byte by byte (just add another constraint to the SQL injection and check for the password).
There are two little pitfalls: One needs to use something like `COLLATE utf8mb4_bin` to make the match case-sensitive and be aware that the `_` character matches any character.

I guessed the `password` and `username` columns of the database table correctly, however, one can also extract them from the database scheme the same way.

Flag: `midnight{BA053FFB-CC3C-4AB7-9A85-15A594CC43E9}`
