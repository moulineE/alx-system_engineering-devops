# 0x17. Web Stack Debugging #3

This project is part of the ALX System Engineering & DevOps curriculum. It focuses on debugging a web server running a WordPress website on a LAMP (Linux, Apache, MySQL, and PHP) stack. You will use `strace` to identify and fix issues causing Apache to return a 500 error and then automate the fix using Puppet.

## Table of Contents

1. [Project Description](#project-description)
2. [Project Tasks](#project-tasks)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Contributors](#contributors)
6. [License](#license)

## Project Description

The "Web Stack Debugging #3" project involves troubleshooting and resolving an issue where Apache is returning a 500 Internal Server Error. You will use `strace` to trace system calls made by Apache to identify the problem, fix it, and then create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix.

## Project Tasks

1. **Strace Is Your Friend**
    - Use `strace` to identify the root cause of Apache returning a 500 error.
    - Fix the issue.
    - Create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix.
    - You can use any Puppet resource type for the fix.

## Requirements

- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4
- Install `puppet-lint` using the following commands:
  ```shell
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
