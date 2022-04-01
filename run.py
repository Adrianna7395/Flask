# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 1},
        {"name": "Birne", "amount": 4}
    ]

    for item in items:
        item["amount"] = item["amount"] * 2

    person = ("Max", "Mustermann")

    return render_template("start.html", person=person, items=items)

@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)

@app.route("/currency")
def currency():
    currency1 = request.args.get("currency1", "EUR")
    currency2 = request.args.get("currency2", "KN")
    rate = float(request.args.get("rate", 7.57))

    table1 = []
    for x in range(1, 50):
        table1.append((x, round(x * rate, 2)))

    table2 = []
    for x in range(1, 50):
        table2.append((x, round(x / rate, 2)))

    return render_template("currency.html",
                           rate=rate,
                           currency1=currency1,
                           currency2=currency2,
                           table1=table1,
                           table2=table2)



'''@app.route("/test")
def test():
    paragraph = "<p>Hallo Welt</p>"     # Variable definieren
    return "Hello <strong>Test</strong>!" + paragraph'''