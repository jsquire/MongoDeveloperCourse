import pymongo
import sys

client = pymongo.MongoClient("localhost", 27017)
db = client.students
grades = db.grades

try:
    current_id = None

    for student in grades.find().sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]):
        if current_id is not student['student_id']:
            print 'Removing: {0}'.format(student['student_id'])
            grades.remove({ '_id' : student['_id']})

        current_id = student['student_id']

except:
    print "Unexpected error:", sys.exc_info()[0]