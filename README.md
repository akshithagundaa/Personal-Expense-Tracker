# Personal Expense Tracker

A web-based Personal Expense Tracker developed using **Flask, SQLite, HTML, CSS, and JavaScript**. The application helps users record daily expenses, monitor spending habits, receive overspending alerts, and generate downloadable expense reports.

## Features

* Add daily expenses with category and amount
* View complete expense history
* Track personal spending patterns
* Daily spending limit alerts
* Expense categorization
* Dashboard for expense monitoring
* Export expense reports as CSV
* Simple and user-friendly interface
* Persistent data storage using SQLite

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

## Project Architecture

```text
Frontend (HTML, CSS, JavaScript)
                │
                ▼
         Flask Backend
                │
                ▼
          SQLite Database
                │
                ▼
      Expense Reports & Analytics
```

## Project Modules

### Add Expense Module

Allows users to enter expense details including category, amount, and date.

### View Expenses Module

Displays all recorded expenses in an organized format.

### Expense Monitoring Module

Tracks spending and alerts users when they exceed predefined spending limits.

### Report Generation Module

Generates downloadable CSV reports for expense analysis and record keeping.

## Database Structure

### Expenses Table

| Field       | Description         |
| ----------- | ------------------- |
| id          | Expense ID          |
| category    | Expense Category    |
| amount      | Expense Amount      |
| date        | Expense Date        |
| description | Expense Description |

## Key Functionalities

* Record daily expenses
* View spending history
* Monitor budget limits
* Receive overspending alerts
* Export expense reports
* Maintain expense records securely

## Installation

### Clone Repository

```bash
git clone https://github.com/akshithagundaa/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
```

### Install Dependencies

```bash
pip install flask
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## Screenshots

* Home Dashboard
* Add Expense Page
* Expense History Page
* Overspending Alert
* Expense Report Export

## Future Enhancements

* User Authentication
* Monthly Budget Planning
* Expense Categories with Charts
* PDF Report Generation
* Email Notifications
* Mobile Responsive Design
* Expense Forecasting
* Cloud Database Integration

## Learning Outcomes

This project demonstrates:

* Full Stack Web Development
* Flask Application Development
* SQLite Database Management
* CRUD Operations
* Expense Tracking Logic
* CSV Report Generation
* Frontend and Backend Integration

## Author

**Gunda Akshitha**

Personal Expense Tracker built using Flask and SQLite for efficient expense monitoring and reporting. 🚀
