# Web Infrastructure Design

This repository contains a series of tasks focused on designing web infrastructures. The project aims to provide a comprehensive understanding of various components and concepts related to web infrastructure design, such as servers, load balancers, databases, security measures, monitoring, and more.

## Team Members
- Mohamed Ezghoudi
- El mahdi Mouline

## Project Timeline
- Start: Aug 24, 2023, 4:00 AM
- End: Aug 28, 2023, 4:00 AM

## Concepts Covered
Throughout this project, you will explore and understand the following concepts:

- DNS (Domain Name System)
- Monitoring and Metrics
- Web Servers
- Network Basics
- Load Balancers
- Server Redundancy and High Availability
- HTTPS and SSL/TLS Encryption
- Firewalls
- Database Clustering (Primary-Replica)
- Server Security
- Single Point of Failure (SPOF)

## Learning Objectives
Upon completing this project, you should be able to:

- Create diagrams illustrating various web infrastructures.
- Explain the purpose and role of each component in the designed infrastructure.
- Understand system redundancy and high availability concepts.
- Identify potential issues in a web infrastructure and propose solutions.
- Interpret acronyms such as LAMP, SPOF, and QPS.

## Task 0: Simple Web Stack
Design a basic web infrastructure that consists of a single server hosting a LAMP (Linux, Apache, MySQL, PHP) stack. The infrastructure includes:

- 1 Server
- 1 Nginx Web Server
- 1 Application Server
- 1 Set of Application Files (Code Base)
- 1 MySQL Database
- 1 Domain Name (www.foobar.com) configured with DNS

Explain the roles of each component, the purpose of the domain name, DNS record types, and communication between the server and user's computer. Identify issues such as SPOF, downtime during maintenance, and scaling limitations.

## Task 1: Distributed Web Infrastructure
Design a more complex web infrastructure with distributed components. The infrastructure includes:

- 2 Servers
- 1 Nginx Web Server
- 1 Application Server
- 1 HAProxy Load Balancer
- 1 Set of Application Files (Code Base)
- 1 MySQL Database

Explain the purpose of adding each new component. Discuss the load balancer's distribution algorithm and Active-Active vs. Active-Passive setup. Explain how a Primary-Replica (Master-Slave) database cluster works and the differences between the nodes.

## Task 2: Secured and Monitored Web Infrastructure
Design an enhanced web infrastructure with security and monitoring measures. The infrastructure includes:

- 3 Firewalls
- SSL Certificate for HTTPS
- 3 Monitoring Clients (Sumologic or other services)

Explain the need for firewalls, SSL certificates, and monitoring. Describe the data collection process by monitoring tools. Address issues like SSL termination at the load balancer, limited write-capable MySQL servers, and uniform server components.

## Copyright
This project is protected by the ALX license. All rights reserved.
