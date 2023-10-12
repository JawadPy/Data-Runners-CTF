# Data Runners CTF
Exploit the exe file to get the real flag, while the source code got only a fake flag.

`Level:` Easy

# Solution Explained
It's SQLi, when you run the program choose `1`, then enter username = `flag`, then the password would be sql payload: `' OR 1=1 --`.
when you enter the account successfully, you have to change the username, so you change it with this payload: `', username = password --`.

The payload takes advantage of `UPDATE users SET username = '{newuser}' WHERE id = {result[0]}"` in line 18, because you can update more than one column with one `UPDATE` statement.
