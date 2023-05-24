import os
import csv
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Stu.html")

@app.route("/add_student", methods=["GET" , "POST"])
def add_student():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        enroll = request.form.get('enrollment')
        phone = request.form.get('phone')
        branch = request.form.get('branch')
        department = request.form.get('department')

        with open("registrations.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([fname, lname, enroll, phone, branch, department])

        csv_file_path = os.path.join(os.getcwd(), "SMS", "registrations.csv")
    return render_template("result.html", fname=fname, lname=lname, enroll=enroll, phone=phone, branch=branch, department=department)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)