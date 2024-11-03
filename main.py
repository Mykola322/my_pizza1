from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Пепероня", "ingradients": "Ковбаса пепероні, сир моцарела, соус", "price":150},
        {"name": "Класична", "ingradients": "Помідори, сир сулугуня, соус", "price": 120},
        {"name": "4 сири", "ingradients": "Сир моцарела, сир солугуня, сир фета, соус", "price": 200}
    ]
    return render_template("menu.html", pizzas=pizzas)

if __name__ == "__main__":
    app.run(debug=True, port=6500)

