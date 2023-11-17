---

# 0x1B. Web stack debugging #4

## Overview

This project is part of the ALX System Engineering & DevOps curriculum and focuses on web stack debugging. The goal is to analyze and fix issues related to a web server setup featuring Nginx, specifically addressing a high rate of failed requests.

## Project Details

- **Start Date:** November 13, 2023, 4:00 AM
- **End Date:** November 17, 2023, 4:00 AM
- **Checker Release Date:** November 16, 2023, 4:00 AM

## Requirements

### General

- All files are interpreted on Ubuntu 14.04 LTS.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining what the manifest is about.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

### Install `puppet-lint`

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

### 0. Sky is the limit, let's bring that limit higher

**Description:** In this web stack debugging task, we are testing the performance of our web server setup featuring Nginx. The current setup is experiencing a significant number of failed requests. The benchmarking is done using ApacheBench to simulate HTTP requests. The goal is to fix the stack to reduce failed requests to 0. Logs are emphasized as valuable tools for debugging.

#### Benchmarking Before Fix

```bash
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
```

#### Puppet Apply

```bash
root@0a62aa706eb3:/# puppet apply 0-the_sky_is_the_limit_not.pp
```

#### Benchmarking After Fix

```bash
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
```

---

**Copyright © 2023 ALX. All rights reserved.**
