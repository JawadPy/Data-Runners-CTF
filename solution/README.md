# Data Runners
This challenge was easy at early development, and it's still easy if you don't miss around with debuggers.

First time you run the challenge you will get this output:
```cmd
Welcome to Accounts Management DB System
1. Manage Accounts
2. Exit
>>
```
This means we are dealing with a database, and since there is no database files anywhere then it's in our computer's memory.
Choosing option number 1 will output this:
```cmd
Current users are:
1 - flag
2 - user
```
This info can be useful if the usernames are comming from the database directly, but we have to discover the app for now and move on with `user` user.

```cmd
Username: user
```
But, since it's a database we are dealing with, let's try some ... you know '
```cmd
Username: user '
```
for the password i'd enter anything to see the result..


AAAaand Ops, the app crashed. Maybe there is some sort of protection for sqli or it's unhandled error, let's find out.
instead of adding `'` I'll add `' OR 1=1 --` to the username this time with any password.

![image](https://github.com/JawadPy/Data-Runners-CTF/assets/98477272/702d38a6-c251-432c-97db-3910a4de7502)

It doesn't feel alright... I passed the login and now it reqire a new username. I'd go with `ducky` as a new username .

When trying accessing option number 1 again after changing the username i got an intersting result..
![image](https://github.com/JawadPy/Data-Runners-CTF/assets/98477272/20ffa072-1bf4-4b49-a52c-2a1ac72799d7)

This means the app is selecting usernames and display them from database directly.
This is really useful in one case, if the username is the flag its self. since we cannot display the flag in any other way using any sql query.

Now remember, we are dealing with database, so when the app updated the username we will force the app to make the username = password.

Imagine this query:
```sql
UPDATE username = "XX" WHERE id = 0
```

`UPDATE` statment can update more than one column in database using a `,` like this:

```sql
UPDATE username = 'xx', username = 'YY' WHERE id = 0
```

So, when changing the username we use this payload:

```sql
', username = password --
```

Notice that I told the database to change all username to be the thier passwords, and `--` to comment `WHERE id =`.

![image](https://github.com/JawadPy/Data-Runners-CTF/assets/98477272/6002f105-972d-4533-9fd8-becadc347ca9)

After accessing `Manage Accounts` again we now can see the flag.


