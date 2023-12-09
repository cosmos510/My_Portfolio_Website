import smtplib
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import os

myemail=os.environ.get("myemail")
password=os.environ.get("password")
your_email = os.environ.get("your_email")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('flask_key')
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=myemail, password=password)
        connection.sendmail(from_addr=myemail, to_addrs=your_email, msg=email_message)


if __name__ == '__main__':
    app.run(debug=True, port=5001)