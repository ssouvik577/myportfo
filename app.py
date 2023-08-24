from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lost')
def lost():
    return render_template("blank.html")

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data["name"]
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('contact.html')
    else:
        return "Something Went wrong try again!"

# @app.route('/<string:page_name>')
# def pages(page_name):
#     return render_template(page_name)

app.run(debug=True)