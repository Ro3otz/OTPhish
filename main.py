from flask import Flask, request

app = Flask(__name__)

sms_messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sms_input = request.form['sms_input']
        print(sms_input)
        sms_messages.append(sms_input)
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            .container {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
                border-radius: 5px;
            }
            label {
                display: block;
                margin-bottom: 5px;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
            input[type="submit"] {
                background-color: #007BFF;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 3px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SMS Kodu:</h1>
            <form method="POST">
                <label for="sms_input">SMS Kodu:</label>
                <input type="text" id="sms_input" name="sms_input">
                <input type="submit" value="Gönder">
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
