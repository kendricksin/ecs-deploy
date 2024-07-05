from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with a simple form
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Form</title>
</head>
<body>
    <h1>Simple Web Form</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = f"Thank you, {name}! We've received your submission with email: {email}"
    return render_template_string(html_template, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
