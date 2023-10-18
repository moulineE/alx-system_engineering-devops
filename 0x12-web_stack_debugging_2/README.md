---

# 0x12. Web stack debugging #2 - Project README

Welcome to the Web stack debugging #2 project! In this project, you will continue to explore web stack debugging techniques on Ubuntu 20.04 LTS. This project aims to help you practice identifying and fixing web server issues.

## Project Details

- **By:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Project Duration:** Oct 16, 2023 4:00 AM to Oct 18, 2023 4:00 AM
- **Checker Release:** Oct 17, 2023 11:12 AM
- **Auto Review:** An auto review will be launched at the deadline

## Concepts

For this project, we expect you to focus on the following concept:

- Web stack debugging

## Requirements

### General

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the project folder is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Run software as another user (mandatory)

The user root is, on Linux, the "superuser." It can do anything it wants, which is both a good and a bad thing. A good practice is that one should never be logged in as the root user because running certain commands can have severe consequences. In this task, you need to write a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument.

#### Requirements:

- Write a Bash script that accepts one argument.
- The script should run the `whoami` command under the user passed as an argument.
- Make sure to try your script by passing different users.

#### Example:

```shell
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

### 1. Run Nginx as Nginx (mandatory)

The root user is a superuser that can do anything on a Unix machine, and it's the top administrator. Security-wise, it's essential not to run web servers as root (which is the default for most configurations) and instead run the process as a less privileged user, like the `nginx` user. Fix this container so that Nginx is running as the `nginx` user.

#### Requirements:

- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- You cannot use `apt-get remove`.
- Write a Bash script that configures the container to fit the above requirements.

#### After debugging:

```shell
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#

root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```
