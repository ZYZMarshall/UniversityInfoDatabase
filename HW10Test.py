import unittest
import os
from HW10 import Repository
from HW10 import Student
from HW10 import Instructor
from HW10 import Major
  
class RepositoryTest (unittest.TestCase):
    """Checks that the repository class is working correctly"""
    
    def test_good_input(self):
        """Tests some good input values and the corresponding results from each from the repository"""
        directory = r'C:\workspace\SSW810\Data_Repository_Files'   #change the directory to where the test files saved
        test_file = os.path.join(directory, 'Good_Test')
        student_test = {'12345': Student('12345', 'Lebron,J', 'SFEN'), '12346': Student('12346', 'AFK,A', 'SFEN')}
        instructor_test = {'66666': Instructor('66666', 'Einstein, A', 'SFEN'), '77777': Instructor('77777', 'Feynman, R', 'SFEN')}
        majors_test = {'SFEN': Major('SFEN'), 'SYEN': Major('SYEN')}
        self.assertTrue(student_test.keys() == Repository(test_file).students.keys())               #tests that students holds a dictionary with key:cwid and value: instance of student
        self.assertTrue(instructor_test.keys() == Repository(test_file).instructors.keys())         #tests that instructors holds a dictionary with key:cwid and value: instance of instructor
        self.assertTrue(majors_test.keys() == Repository(test_file).majors.keys())                  #tests that majors  holds a dictionary with key:major and value: instance of major class
                                                                                                    #major class is individually tested below
        self.assertTrue

    def test_bad_input(self):
        """Tests all bad inputs and their corresponding Errors that they raise"""
        #ValueErrors:
        directory = r'C:\workspace\SSW810\Data_Repository_Files'
        with self.assertRaises(ValueError):
            Repository(os.path.join(directory, "Bad_Student"))                  #doesn't contain proper format for a student
        with self.assertRaises(ValueError):    
            Repository(os.path.join(directory, "New_Student_from_grade"))       #has grades for someone who isn't a student
        with self.assertRaises(ValueError):
            Repository(os.path.join(directory, "Major_not_offered"))            #gives a student a major not offered at university
        #FileNotFoundErrors:
        with self.assertRaises(FileNotFoundError):    
            Repository(os.path.join(directory, "Folder_has_no_files"))          #no file in this folder^
        with self.assertRaises(FileNotFoundError):
            test = Repository(directory)
            test.open_stud_file("not_a_real_file.txt", '\t')                    #file doesnt exist
        #NotADirectoryErrors:
        with self.assertRaises(NotADirectoryError):
            Repository(r'\This\is\an\error')                                  #Not a vaild directory
        with self.assertRaises(NotADirectoryError):    
            Repository(os.path.join(directory, "Not_A_Real_Folder"))            #I dont know where this folder is hints:not in my laptop

class TestMajor(unittest.TestCase):
    
    def test_majors_class(self):
        """Checks that the major class is working properly"""
        CS = Major('CS')
        CS.add_course('SSW 810', 'R')
        CS.add_course('SSW 555', 'E')
        req_courses = {'SSW 810'}
        ele_courses = {'SSW 555'}
        self.assertTrue(CS.required_courses == req_courses)
        self.assertTrue(CS.elective_courses == ele_courses)
        #ValueError
        with self.assertRaises(ValueError):
            CS.add_course('CS 123', 'NA')   #Invalid flag for a major - must be either elective ('E') or required ('R')
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)