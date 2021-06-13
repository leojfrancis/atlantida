from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route("/")
def HomeView():
    return render_template("index.html")


@app.route("/about")
def AboutView():
    return render_template("about.html")


@app.route("/services")
def ServicesView():
    return render_template("service.html")


@app.route("/products")
def ProductsView():
    return render_template("products.html")


@app.route("/career")
def CareerView():
    return render_template("career.html")


@app.route("/contact")
def ContactView():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
