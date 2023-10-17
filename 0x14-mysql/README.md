---

# 0x14. MySQL - Project README

Welcome to the MySQL project! In this project, you will work with MySQL, a popular open-source relational database management system. You'll set up MySQL on two servers, configure primary-replica infrastructure, and create a backup strategy for your databases.

## Project Details

- **By:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Project Duration:** Oct 17, 2023 4:00 AM to Oct 18, 2023 4:00 AM
- **Checker Release:** Oct 17, 2023 10:00 AM
- **Auto Review:** An auto review will be launched at the deadline

## Concepts

For this project, we expect you to focus on the following concepts:

- Database administration
- Web stack debugging
- [How to] Install MySQL 5.7

## Learning Objectives

By the end of this project, you should be able to explain to anyone:

### General

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks yourself to meet the above learning objectives.
- You will not meet the objectives of this or any following project by copying and pasting someone else's work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the project folder, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Install MySQL (mandatory)

First, let's get MySQL installed on both your web-01 and web-02 servers.

- MySQL distribution must be 5.7.x
- Make sure that task #3 of your SSH project is completed for web-01 and web-02. The checker will connect to your servers to check MySQL status.

### 1. Let us in! (mandatory)

In order to verify that your servers are properly configured, you need to create a user and password for both MySQL databases, which will allow the checker access to them.

- Create a MySQL user named `holberton_user` on both web-01 and web-02 with the hostname set to localhost and the password `projectcorrection280hbtn`. This will allow access to the replication status on both servers.

### 2. If only you could see what I've seen with your eyes (mandatory)

To set up replication, you'll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database, create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has SELECT permissions on your table to check that the table exists and is not empty.

### 3. Quite an experience to live in fear, isn't it? (mandatory)

Before setting up your primary-replica synchronization, create a new user for the replica server on your primary MySQL server (web-01).

- The new user should be named `replica_user` with the host name set to `%` and any password you'd like.
- `replica_user` must have the appropriate permissions to replicate your primary MySQL server.

### 4. Setup a Primary-Replica infrastructure using MySQL (mandatory)

Having a replica member on for your MySQL database has two advantages: redundancy and load distribution. Set up replication for the MySQL database named `tyrell_corp`.

- MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter.
- MySQL replica must be hosted on web-02.
- Provide your MySQL primary configuration as the answer file (my.cnf or mysqld.cnf) with the name `4-mysql_configuration_primary`.
- Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`.

### 5. MySQL backup (mandatory)

Backups are crucial in ensuring the safety and availability of your data. Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

- The MySQL dump must contain all your MySQL databases.
- The MySQL dump must be named `backup.sql`.
- The MySQL dump file has to be compressed to a `tar.gz` archive.
- This archive must have the following name format: `day-month-year.tar.gz`.
- The user to connect to the MySQL database must be root.
- The Bash script accepts one argument, which is the password used to connect to the MySQL database.
