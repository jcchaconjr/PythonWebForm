from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        dob = request.form['dob']

        """ message = "Try again when you are 18"
        if age > 18:
            message = "Welcome to our site!" """

        # Validate City input
        if not email.isalpha():
            message = "Please enter a valid email"

        welcome_message = f"Hello {first_name} {last_name}, keep an eye on your inbox for {email} around {dob} for a special Birthday treat!"

        return render_template('result.html', welcome_message=welcome_message, message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
