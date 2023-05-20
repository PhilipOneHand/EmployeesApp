from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL
app = Flask(__name__,template_folder="../templates")
mysql = MySQL()


# Set Mysql credentials
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "19591204"
app.config["MYSQL_DATABASE_DB"] = "EmployeesApp"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)

@app.route("/test")
def test():
    connection = mysql.connect()
    return "Healthy"
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/addEmployee', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        age = request.form['age']
        job = request.form['job']

        # Insert new employee into database
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, gender, email, age, job) VALUES (%s, %s, %s, %s, %s)",
                       (name, gender, email, age, job))
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('EmployeeAddedSuccessfully.html')
    else:
        return render_template('addEmployee.html')

@app.route("/delete_employee/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    # Connect to the database
    conn = mysql.connect()
    cursor = conn.cursor()

    # Execute the SQL query to delete the employee record
    cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Redirect back to the employee list page
    return redirect(url_for('showemplist'))

@app.route("/Show_employee_list", methods=['GET','POST'])
def showemplist():
    # Connect to the database
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == 'POST':
        if 'emp_id' in request.form:
            # Get the employee ID entered in the form
            emp_id = request.form['emp_id']

            # Execute the SQL query to retrieve employee by ID
            cursor.execute("SELECT * FROM employees WHERE id=%s", (emp_id,))
            data = cursor.fetchall()

        elif 'emp_name' in request.form:
            # Get the employee name entered in the form
            emp_name = request.form['emp_name']

            # Execute the SQL query to retrieve employee by name
            cursor.execute("SELECT * FROM employees WHERE name LIKE %s", ('%' + emp_name + '%',))
            data = cursor.fetchall()

    else:
        # Execute the SQL query to retrieve all employees
        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Render the template with the employee data
    return render_template("showEmployeeList.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)