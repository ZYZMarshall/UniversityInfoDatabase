select Name from HW11_students where CWID='11461';

select Major, count(CWID) from HW11_students GROUP BY Major;

select Grade, count(Grade) from HW11_grades group by Grade;

select Name from HW11_students JOIN HW11_grades
      ON HW11_students.CWID = HW11_grades.Student_CWID WHERE Course = 'SSW 540';

select Name,CWID,Major,Grade from HW11_students join HW11_grades
      on HW11_students.CWID = HW11_grades.Student_CWID;

select CWID, Name, Dept, Course, count(Student_CWID) as Students from HW11_instructors join HW11_grades
      on HW11_instructors.CWID = HW11_grades.Instructor_CWID group by Course;