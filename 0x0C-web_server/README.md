---
# 0x0C. Web Server - Project README

Hello everyone! I'm excited to document my progress on the 0x0C. Web Server project. Let's dive into the world of DevOps and web servers together!

## Project Details

- **By:** Sylvain Kalache
- **Weight:** 1
- **Project Start:** Sep 25, 2023 4:00 AM
- **Project End:** Sep 27, 2023 4:00 AM
- **Checker Release:** Sep 25, 2023 4:00 PM
- **Auto Review:** Will be launched at the deadline

## Concepts

In this project, we'll explore the concept of "What is a Child Process?"

## Background Context

This project is unique because some tasks will be graded on two aspects:

1. Is my web-01 server configured according to the requirements?
2. Does my answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to meet the requirements (without human intervention)?

The goal here is to automate our work. Automating tasks we typically do manually can save time and help us focus on more interesting challenges. A lazy Software Engineer is often a good Software Engineer!

## Resources

Before we get started, let's make sure to check out these resources:

- [How the web works](https://example.com)
- [Nginx](https://example.com)
- [How to Configure Nginx](https://example.com)
- [Child process concept page](https://example.com)
- [Root and subdomain](https://example.com)
- [HTTP requests](https://example.com)
- [HTTP redirection](https://example.com)
- [Not found HTTP response code](https://example.com)
- [Logs files on Linux](https://example.com)
- For reference:
  - [RFC 7231 (HTTP/1.1)](https://example.com)
  - [RFC 7540 (HTTP/2)](https://example.com)
- `man` or `help` for the following commands:
  - `scp`
  - `curl`

## Learning Objectives

By the end of this project, I should be able to explain the following concepts without the help of Google:

**General:**
1. What is the main role of a web server?
2. What is a child process?
3. Why do web servers usually have a parent process and child processes?
4. What are the main HTTP requests?
5. DNS:
   - What DNS stands for?
   - What is DNS's main role?
   - DNS Record Types:
     - A
     - CNAME
     - TXT
     - MX

## Copyright & Plagiarism

I understand that I am responsible for coming up with solutions for the tasks myself to meet the learning objectives mentioned above. I will not copy and paste someone else's work, and I'm aware that any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

**General:**
- Allowed editors: vi, vim, emacs
- All my files will be interpreted on Ubuntu 16.04 LTS
- I will ensure that all my files end with a new line
- I'll include a `README.md` file at the root of the project folder
- I'll make sure that all my Bash script files are executable
- My Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all my Bash scripts will be exactly `#!/usr/bin/env bash`
- The second line of all my Bash scripts will be a comment explaining what the script is doing
- I won't use `systemctl` for restarting a process


## Tasks

### 0. Transfer a file to your server (mandatory)

For this task, I need to write a Bash script that transfers a file from our client to a server. Here are the requirements:

**Requirements:**
- It should accept 4 parameters:
  - The path to the file to be transferred
  - The IP of the server we want to transfer the file to
  - The username `scp` connects with
  - The path to the SSH private key that `scp` uses
- It should display "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY" if fewer than 3 parameters are passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`

### 1. Install Nginx web server (mandatory)

Now, let's install Nginx on my `web-01` server. Here are the requirements:

**Requirements:**
- Install Nginx on your `web-01` server
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string "Hello World!"
- As an answer file, I need to write a Bash script that configures a new Ubuntu machine to meet the above requirements (this script will be run on the server itself)
- I can't use `systemctl` for restarting Nginx


### 2. Setup a domain name (mandatory)

Let's set up a domain name for our server. Here are the requirements:

**Requirements:**
- Provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
- Configure your DNS records with an A entry so that your root domain points to your `web-01` IP address (Warning: the propagation of your records can take time, ~1-2 hours)
- Go to your profile and enter your domain in the "Project website URL" field

### 3. Redirection (mandatory)

Now, let's configure our Nginx server so that `/redirect_me` is redirecting to another page. Here are the requirements:

**Requirements:**
- The redirection must be a "301 Moved Permanently"
- My answer file should be a Bash script containing commands to automatically configure an Ubuntu machine to meet the above requirements
- I'll use what I did in `1-install_nginx_web_server` to write `3-redirection` so that it configures a brand new Ubuntu machine to meet the requirements in this task


### 4. Not found page 404 (mandatory)

Let's configure our Nginx server to have a custom 404 page that contains the string "Ceci n'est pas une page." Here are the requirements:

**Requirements:**
- The page must return an HTTP 404 error code
- The page must contain the string "Ceci n'est pas une page"
- I'll use what I did in `3-redirection` to write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to meet the requirements in this task

---

*Copyright © 2023 ALX, All rights reserved.*
