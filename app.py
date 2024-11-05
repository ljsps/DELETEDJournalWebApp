from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# # About route
# @app.route('/about')
# def about():
#     return render_template('about.html')

# # Services route
# @app.route('/services')
# def services():
#     return render_template('services.html')

# # Contact route
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
