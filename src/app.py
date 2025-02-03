from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():

    username = os.getenv('USERNA')
    password = os.getenv('PASS')
    email = os.getenv('EMAIL')

    print(username, password, email)

    return '<h1>Mi primera APP Flask deployeada en render.<br>{}<br>{}<br>{}</h1>'.format(username, email, password)

def status_404(error):
    return '<h1> PAGINA NO ENCONTRADA</h1>'

if __name__ == '__main__':
    app.register_error_handler(404, status_404)
    app.run(debug=True)