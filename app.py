from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy

import csv
from datetime import datetime

app = Flask(__name__)

# DATABASE CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# INITIALIZE DATABASE
db = SQLAlchemy(app)


# BUDGET LIMITS
DAILY_BUDGET = 2000
MONTHLY_BUDGET = 50000
YEARLY_BUDGET = 600000


# DATABASE TABLE
class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float)

    category = db.Column(db.String(100))

    description = db.Column(db.String(200))

    date = db.Column(db.String(50))

    time = db.Column(db.String(50))

    is_over_limit = db.Column(db.Boolean, default=False)


# HOME PAGE
@app.route('/')
def home():

    expenses = Expense.query.all()

    total_expense = 0

    for expense in expenses:
        total_expense += expense.amount

    daily_remaining = DAILY_BUDGET - total_expense

    monthly_remaining = MONTHLY_BUDGET - total_expense

    yearly_remaining = YEARLY_BUDGET - total_expense

    return render_template(
        'index.html',

        total_expense=total_expense,

        daily_budget=DAILY_BUDGET,
        monthly_budget=MONTHLY_BUDGET,
        yearly_budget=YEARLY_BUDGET,

        daily_remaining=daily_remaining,
        monthly_remaining=monthly_remaining,
        yearly_remaining=yearly_remaining
    )


# ADD EXPENSE
@app.route('/add', methods=['GET', 'POST'])
def add_expense():

    if request.method == 'POST':

        amount = request.form['amount']

        category = request.form['category']

        description = request.form['description']

        current_datetime = datetime.now()

        current_date = current_datetime.strftime("%d-%m-%Y")

        current_time = current_datetime.strftime("%I:%M %p")


        expenses = Expense.query.all()

        current_total = 0

        for expense in expenses:
            current_total += expense.amount

        new_total = current_total + float(amount)

        over_limit = False

        if new_total > DAILY_BUDGET:
            over_limit = True


        new_expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=current_date,
            time=current_time,
            is_over_limit=over_limit
        )

        db.session.add(new_expense)

        db.session.commit()

        if over_limit:
            return redirect('/expenses?warning=1')

        return redirect('/expenses')

    return render_template('add_expense.html')


# VIEW EXPENSES
@app.route('/expenses')
def view_expenses():

    expenses = Expense.query.all()

    warning = request.args.get('warning')

    return render_template(
        'view_expenses.html',
        expenses=expenses,
        warning=warning
    )


# DELETE EXPENSE
@app.route('/delete/<int:id>')
def delete_expense(id):

    expense = Expense.query.get(id)

    db.session.delete(expense)

    db.session.commit()

    return redirect('/expenses')


# EXPORT CSV REPORT
@app.route('/export')

def export_csv():

    expenses = Expense.query.all()

    with open('expense_report.csv',
              mode='w',
              newline='') as file:

        writer = csv.writer(file)

        writer.writerow([
            'ID',
            'Amount',
            'Category',
            'Description',
            'Date',
            'Time',
            'Status'
        ])

        for expense in expenses:

            status = "Over Limit" if expense.is_over_limit else "Normal"

            writer.writerow([
                expense.id,
                expense.amount,
                expense.category,
                expense.description,
                expense.date,
                expense.time,
                status
            ])

    return send_file(
        'expense_report.csv',
        as_attachment=True
    )


# CREATE DATABASE
with app.app_context():
    db.create_all()


# RUN APPLICATION
app.run(debug=True)