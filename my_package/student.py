from my_package.library import Library
class Student:
    def __init__(self,studid=1001,studname=None,classname=None,libid=None,is_any_book_issued=None):
        Library.__init__(self,libid,is_any_book_issued)
        self.student_set={}
        self.studid=studid
        self.studname=studname
        self.classname=classname
        
    def __str__(self):
        return f"Student Id : {self.studid}\nStudent Name : {self.studname}\nLibrary Id : {self.libid}\nAny book issued ? : {self.is_any_book_issued}"
    
    
    def create_student(self):
        self.student_set[self.studid]=self.studname
        return self.student_set
       
    def remove_student(self,studid):
        self.student_set.pop(studid)
        # return self.student_set
        
       



