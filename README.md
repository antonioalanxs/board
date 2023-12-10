# board

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Features](#features)
4. [What have I learned?](#what-have-i-learned)

## Overview

board is a minimalist notice board built using [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [Tailwind CSS](https://tailwindcss.com/), [Django](https://www.djangoproject.com/), [MySQL](https://www.mysql.com/) and [Docker](https://www.docker.com/). This web application was used to give a lecture on the operation of Django and its security mechanisms.

### Demonstration

<video src="https://github.com/antonioalanxs/board/assets/79718376/a3d8ddd6-486b-4007-bb52-db1aba3a1e6f" alt="Demonstration"></video>

## Installation

### Prerequisites

Have [Docker](https://docs.docker.com/engine/install/) installed on your machine.

### Cloning the Repository

```shell
git clone https://github.com/antonioalanxs/board
cd board
```

### Run the application

```shell
cd docker
docker compose up --build
```
The application is now running on your [localhost:8000](http://localhost:8000).

### Sample users

| User               | Username      | Password             |
| :----------------: | :-----------: | :------------------: |
| **@antoniomanuel**         | antoniomanuel         | `a`        |
| **@teresavrod**          | teresavrod          | `a`             |
| **@antonioalanxs** | antonioalanxs | `a` |

### Stop the application

```shell
docker compose down
```

The application was turned off.

## Features

### Functional Requeriments

- **Registration**: New users can easily register by providing essential information.
  
- **Login**: Users can log in securely to access their shopping list.
  
- **Skip Login (Auto-Login)**: For returning users, the application provides a convenient option to skip the login process.
  
- **Logout**: Users can log out at any time to secure their account and data.

- **Read a Notice**: Users can view the contents of a notice in a readable format, enabling them to stay informed about important information or updates shared within the application.

- **Publish a Notice**: Users can write a notice in a very simple manner.
  
- **Delete a Notice**: Users can remove notices with a single click.

- **Edit a Notice**: Users have the flexibility to modify their notices, allowing them to update information or make corrections as needed.

### Non-functional Requirements

- **Minimalistic and User-Friendly Interface:** The application boasts a clean and intuitive design, providing an exceptional user experience (UX).

- **Responsive Design**: Ensured optimal viewing and interaction across various devices, enhancing accessibility.

- **Legal Compliance:** The application strictly follows the laws and regulations of each country in which it is used.

- **Scalability:** Built to handle a growing user base and data efficiently.

- **Availability:** Ensures the application is available and accessible to users when needed.

- **Data Durability with SQL Database:** Guarantees the persistence and reliability of user data by leveraging a SQL database, ensuring robust storage and retrieval capabilities.

## What have I learned?

- **Better understanding and management of Docker**: Gained proficiency in handling Docker containers, enhancing the distribution of applications.

- **Usage of phpMyAdmin**: Acquired skills in utilizing phpMyAdmin for MySQL database management, facilitating data visualization and administration.

- **Seeder usage for database initialization**: Learned to use seeders to populate and initialize the database with test data, aiding in development and testing phases.

- **Improved understanding of Django architecture**: Enhanced comprehension of Django's framework architecture for more effective and scalable web application development.

- **Middleware utilization**: Learned how to use middlewares in the context of Django, allowing customization and extension of web application's behavior.

- **Enhanced communication skills**: Strengthened communication abilities through giving the lecture, enhancing my ability to communicate ideas effectively.
