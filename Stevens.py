import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student_courses')
def student_courses():
    # sqlite_file = '/Users/jrr/Documents/Stevens/810/Assignments/HW11.db'
    sqlite_file = 'C:\\workspace\\UniversityDatabase\\810_startup.db'
    query = """select s.cwid, s.name, s.major, count(g.Course) as complete
               from HW11_students s join HW11_grades g on s.cwid=g.Student_CWID
               group by s.cwid, s.name, s.major"""

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(query)
    results = c.fetchall()

    # convert the query results into a list of dictionaries to pass to the template
    data = [{'cwid': cwid, 'name': name, 'major': major, 'complete': complete}
            for cwid, name, major, complete in results]

    conn.close()  # close the connection to close the database

    return render_template('student_courses.html',
                           title='Stevens Repository',
                           table_title="Number of completed courses by Student",
                           students=data)

@app.route('/instructor')
def instructor():
    # sqlite_file = '/Users/jrr/Documents/Stevens/810/Assignments/HW11.db'
    sqlite_file = 'C:\\workspace\\UniversityDatabase\\810_startup.db'
    query = """select CWID, Name, Dept, Course, count(Student_CWID) as Students
               from HW11_instructors join HW11_grades 
               on HW11_instructors.CWID = HW11_grades.Instructor_CWID group by Course"""

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(query)
    results = c.fetchall()

    # convert the query results into a list of dictionaries to pass to the template
    data = [{'cwid': cwid, 'name': name, 'dept': dept, 'course': course, 'student': student}
            for cwid, name, dept, course, student in results]

    conn.close()  # close the connection to close the database

    return render_template('instructor.html',
                           title='Stevens Repository',
                           table_title="Instructors information",
                           instructors=data)

app.run(debug=True)