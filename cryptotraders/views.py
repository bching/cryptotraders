from flask import render_template
from cryptotraders import app 

@app.route('/')
def index():
    strategies = get_raw_info()

    return render_template('base.html', strategies=strategies)
