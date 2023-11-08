# 0x18. Webstack Monitoring

This project is part of the ALX System Engineering & DevOps curriculum. It focuses on setting up monitoring for web servers using Datadog, a popular monitoring tool. The project includes tasks related to signing up for Datadog, installing the Datadog agent, monitoring system metrics, and creating a dashboard for visualizing data.

## Table of Contents

1. [Project Description](#project-description)
2. [Project Tasks](#project-tasks)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Contributors](#contributors)
6. [License](#license)

## Project Description

Webstack monitoring is crucial for ensuring the reliability and performance of web servers. This project involves setting up Datadog, a monitoring service, to collect and visualize various system metrics, including read and write requests. Additionally, you will create a dashboard to provide a clear overview of the monitored metrics.

## Project Tasks

1. **Sign up for Datadog and Install Datadog Agent**
   - Sign up for a free Datadog account on https://www.datadoghq.com/.
   - Use the US website (https://app.datadoghq.com) and select the US1 region.
   - Install the Datadog agent on `web-01` server.
   - Create an application key.
   - Copy and paste your Datadog API key and application key into your Intranet user profile.
   - Ensure that your `web-01` server is visible in Datadog under the hostname `XX-web-01`.

2. **Monitor Some Metrics**
   - Set up a monitor to check the number of read requests issued to the device per second.
   - Set up a monitor to check the number of write requests issued to the device per second.

3. **Create a Dashboard**
   - Create a new dashboard in Datadog.
   - Add at least 4 widgets to the dashboard, monitoring various metrics of your choice.
   - Create an answer file (`2-setup_datadog`) that contains the dashboard_id.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Usage

Follow the instructions in each task to complete the project. Make sure to check Datadog for the monitored metrics and the created dashboard.


## License

This project is licensed under the ALX License.

---

**ALX - System Engineering & DevOps Curriculum**

