
class Student(db.Model):
	__tablename__  = "students_info"
	id = db.Column(db.Integer, primary_key = True )
	name = db.Column(db.Sting(50), nullable = False, unique = True)
	course_code = db.Column(db.String(10), nullable = False, unique = True)
	course_name = db.Column(db.String(20),nullable = False, unique = True)

class Lecturer(db.Model):
	"""docstring for Lecturer"""
	__tablename__ = "lecturers_info"
	staffID = b.Column(db.Integer, primary_key = True )
	name = db.Column(db.Sting(50), nullable = False, unique = True)
	course_code = db.Column(db.String(10), nullable = False, unique = True)
		

