from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registered users
registered_users = {}

# List of hardcoded organizations
organizations = ['Organization 1', 'Organization 2', 'Organization 3', 'Organization 4', 'Organization 5']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']

        # Backend validation
        if name.strip() == '' or organization not in organizations:
            return render_template('register.html', organizations=organizations, error=True)

        registered_users[name] = organization
        return redirect(url_for('registered_users'))

    return render_template('register.html', organizations=organizations)

@app.route('/registered_users')
def registered_users():
    return render_template('registered_users.html', registered_users=registered_users)

if __name__ == "__main__":
    app.run(debug=True)
