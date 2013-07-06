import pymongo
import sys

client = pymongo.MongoClient("localhost", 27017)
db = client.school
students = db.students

try:
    grades = None
    
    for student in students.find().sort('_id', pymongo.ASCENDING):
        print 'Processing: {0}'.format(student['name'])
        lowest = None
        grades = student['scores']
        for grade in grades:
            if ((grade['type'] == 'homework') and (lowest is None or grade['score'] < lowest['score'])):
                lowest = grade
        
        if not lowest is None:
            print '\tRemoved : ' + str(lowest['score'])        
            students.update({'_id' : student['_id']}, {'$pull' : {'scores' : lowest }})
        else:
            print '\tNo homework found'

except:
    print "Unexpected error:", sys.exc_info()[0]