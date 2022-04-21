from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'nikhilspatil2622.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'nikhilspatil2622'
app.config['MYSQL_PASSWORD'] = 'nikhil@123'
app.config['MYSQL_DB'] = 'nikhilspatil2622$Hostel_Management_System'


mysql = MySQL(app)

app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'



@app.route('/',methods=['GET'])
def hello():
    cur = mysql.connection.cursor()
    # cur.execute("Select * from student_details")
    # data = cur.fetchall()
    return jsonify("Hey")

if __name__ == '__main__':
    app.run(debug=True)