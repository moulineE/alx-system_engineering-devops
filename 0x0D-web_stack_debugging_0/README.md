---

# 0x0D. Web Stack Debugging #0 - Project README

Hey there! Welcome to the exciting world of web stack debugging! This project is all about mastering the art of debugging web stacks, an essential skill for any Full-Stack Software Engineer. Let's dive in!

## Project Details

- **By:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Project Start:** Sep 25, 2023 4:00 AM
- **Project End:** Sep 27, 2023 4:00 AM
- **Checker Release:** Sep 26, 2023 4:00 PM
- **Auto Review:** Will be launched at the deadline

## Concepts

In this project, we're expected to understand the following concepts:

- Network basics
- Docker
- Web stack debugging

## Background Context

Webstack debugging is an art! Computers and software rarely work perfectly, and that's where debugging comes in. As Full-Stack Software Engineers, it's crucial to master the skill of debugging web stacks.

In this debugging series, we'll be given broken or bugged web stacks, and our ultimate goal is to come up with a Bash script that, once executed, will bring the web stack back to a working state. But before we write that Bash script, we need to figure out what's going wrong and fix it manually.

Let's start with a simple example: our server must have a copy of the `/etc/passwd` file in `/tmp`, and it must have a file named `/tmp/isworking` containing the string "OK." Without these two elements, our web application cannot work.

The provided example:

```shell
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
# ... (output shortened)
vagrant@vagrant:~$ docker exec -ti <container_id> /bin/bash
root@<container_id>:/# ls /tmp/
root@<container_id>:/# cp /etc/passwd /tmp/
root@<container_id>:/# echo OK > /tmp/isworking
root@<container_id>:/# ls /tmp/
isworking  passwd
```

Our answer file should contain:

```shell
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```

Note: As we cannot use interactive software like emacs or vi in our Bash script, everything needs to be done from the command line, including file editing.

## Installing Docker

For this project, we'll be given a container to work with. If you want to experiment or solve this problem locally, you can install Docker on your machine, Ubuntu 14.04 VM, or Ubuntu 16.04 VM if you upgraded.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)

## Resources

I'll be using the `curl` command for debugging.

## Requirements

**General:**
- Allowed editors: vi, vim, emacs
- All my files will be interpreted on Ubuntu 14.04 LTS
- All my files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- All my Bash script files must be executable
- My Bash scripts must pass Shellcheck without any error
- My Bash scripts must run without error
- The first line of all my Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all my Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Give me a page! (mandatory)

In this first debugging project, our task is to get Apache to run on the container and return a page containing "Hello Holberton" when querying the root of it.

Example:

```shell
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
# ... (output shortened)
vagrant@vagrant:~$ docker ps
# ... (output shortened)
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
```

We can see that after starting the Docker container, curling port 8080 mapped to the Docker container port 80 initially returns an error message. After connecting to the container and fixing whatever needed to be fixed (that's our mission), curling port 80 returns a page that contains "Hello Holberton."

I'll paste the command(s) I used to fix the issue in my answer file.

That's it for this debugging adventure! Let's get started and bring the web stack back to life.

---

*Copyright © 2023 ALX, All rights reserved.*
