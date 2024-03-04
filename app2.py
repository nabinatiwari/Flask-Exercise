from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = "Even" if number % 2 == 0 else "Odd"
        except ValueError:
            result = "Not an integer"
        return render_template('result.html', result=result)
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
