# OverTheWire

## Bandit

### Level 0

### Goal
Log into the game using SSH.

### Connection
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
Password: `bandit0`

### What does each part mean?

| Part | Meaning |
|---|---|
| `ssh` | protocol to connect remotely to another machine |
| `bandit0@` | the username you log in with |
| `bandit.labs.overthewire.org` | the server you are connecting to |
| `-p 2220` | the port (SSH uses 22 by default, here it is different) |

### Capure:
![Login screenshot](images/login_bandit.png)

### Level 1
### Goal
Find the password for the next level.

### Steps
1. Run `ls` to list all files. There is only one file: `README`.
2. Run `cat README` to print the content in the console. The new password appears there.

### Capure:
![Paasword in README screenshot](images/password1.png)

### Level 2
### Goal
Find the password for the next level.
### Steps
1. Run `ls` to list all files. There is only one file: `-`.
2. Run `cat ./-` to print the file content in the console and reveal the password.

Why `./-`?
Using only `-` can be interpreted as a special option by commands. Prefixing it with `./` tells the shell this is a file in the current directory, so `cat` reads the file correctly.

### Capure:
![Paasword in README screenshot](images/password2.png)

### Level 3
### Goal
Find the password stored in a file called `--spaces in this filename--`
located in the home directory.

### Steps
1. Run `ls -la` to list all files and see the exact filename.
2. Run `cat -- "--spaces in this filename--"` to print the file content
and reveal the password.

**Why quotes `" "`?**
The filename contains spaces. Without quotes, bash interprets each word
as a separate file. Wrapping the filename in quotes tells bash
this is ONE single filename.

**Why `--` before the filename?**
The filename starts with `-`, which bash normally interprets as a
command flag/option. The `--` tells bash:
"stop reading flags, everything after this is a filename."
Without it, bash gets confused and throws a "No such file" error.

### Capture
![Password screenshot](images/password3.png)

### What I learned
- How to handle filenames with spaces using quotes `" "`
- How to handle filenames starting with `-` using `--`
- How to use `ls -la` to inspect files in detail
