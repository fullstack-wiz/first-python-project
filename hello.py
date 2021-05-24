from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>SHOEPLUG WEBSITE</h1><p>Hello World</p>"

@app.route("/services")
def services():
    return "<p>We are a fashion company that specializes in styling and selling fashion acessories</p>"

@app.route("/about")
def about():
    return "<h1>We offer free delivery to customers</h1><p>You can buy your items online and we will deliver the product to you. </p>"

@app.route("/product")
def prroduct():
    return "<p>We Sell Diferent kinds of shoes</p> <br> <ol><li>Sneakers</li><li>Boots</li><li>Loafers</li><li>Sandals</li></ol>"

@app.route("/call")
def call():
    return "<p>Reach us on Whatsapp and our social media account:</p><ul> <li>0808124695</li><li> @shoeplug</li><li>www.shoeplug.com</li></ul>"