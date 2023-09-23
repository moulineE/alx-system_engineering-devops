# 0x0B. SSH - Project README

![DevOps](https://img.shields.io/badge/DevOps-SSH-blue)
![Network](https://img.shields.io/badge/Network-SysAdmin-brightgreen)
![Security](https://img.shields.io/badge/Security-SSH-yellow)

### Project Information
- **Author:** Sylvain Kalache
- **Weight:** 1
- **Project Start:** Sep 22, 2023 4:00 AM
- **Project End:** Sep 25, 2023 4:00 AM
- **Checker Release:** Sep 22, 2023 10:00 PM
- **Auto Review:** Will be launched at the deadline

## Background Context

In this project, you will be working with an Ubuntu server located in a remote datacenter. You will connect to this server using SSH, specifically utilizing an RSA key instead of a password. The server has already been configured with the public key that you created in a previous project, which can be found in your intranet profile.

Please note that the server is running Ubuntu 20.04 LTS.

### Resources

Before you begin, it's essential to familiarize yourself with the following resources:

- [What is a (physical) server - text](https://example.com)
- [What is a (physical) server - video](https://example.com)
- [SSH essentials](https://example.com)
- [SSH Config File](https://example.com)
- [Public Key Authentication for SSH](https://example.com)
- [How Secure Shell Works](https://example.com)
- [SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)](https://example.com)
- [Understanding the SSH Encryption and Connection Process](https://example.com)
- [Secure Shell Wiki](https://example.com)
- [IETF RFC 4251 (Description of the SSH Protocol)](https://example.com)
- `man` or `help` for the following commands:
  - `ssh`
  - `ssh-keygen`
  - `env`

### Learning Objectives

By the end of this project, you should be able to explain the following concepts without relying on external resources:

**General:**
1. What is a server?
2. Where do servers usually reside?
3. What is SSH?
4. How to create an SSH RSA key pair?
5. How to connect to a remote host using an SSH RSA key pair?
6. The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## Copyright & Plagiarism

**Important Note:** You must solve the project tasks independently, without copying or pasting someone else's work. Plagiarism is strictly forbidden and will result in removal from the program. Do not publish any content related to this project.

## Requirements

**General:**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Use a private key (mandatory)

Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

**Requirements:**
- Only use SSH single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase

Example:
```shell
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
```

### 1. Create an SSH key pair (mandatory)

Write a Bash script that creates an RSA key pair.

**Requirements:**
- Name of the created private key must be `school`
- Number of bits in the created key to be created is 4096
- The created key must be protected by the passphrase `betty`

Example:
```shell
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$
```

### 2. Client configuration file (mandatory)

Your machine has an SSH configuration file for the local SSH client; let's configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

**Requirements:**
- Your SSH client configuration must be configured to use the private key `~/.ssh/school`
- Your SSH client configuration must be configured to refuse authentication using a password

Example:
```shell
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
...
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
...
ubuntu@magic-server:~$
```

Replace `98.98.98.98` with the IP of your server for testing purposes.

### 3. Let me in! (mandatory)

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key provided below to your server so that we can connect using the `ubuntu` user.

```
ssh-rsa "the given alx public key"
```
---

Copyright © 2023 ALX, All rights reserved.
