from flask import Flask, render_template

app = Flask(__name__, template_folder='templates') # templates dir를 templetes root로 지정

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<id>')
def find(id):
    return f'id: {id}'

if __name__ == '__main__':
    app.run()

