from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home - Hritesh Kumar Patro")

@app.route('/about')
def about():
    return render_template('about.html', title="About - Hritesh Kumar Patro")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title="Contacts - Hritesh Kumar Patro")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects - Hritesh Kumar Patro")

if __name__ == '__main__':
    app.run(debug=True)
