from bursary.models import *

students = Student.objects.all()

firstStudent = Student.objects.first()

lastStudent = Student.objects.last()

studentByName = Student.objects.get(name='Stan')

studentById = Student.objects.get(id=1)

firstStudent.order_set.all()

applications = Applications.objects.first()
parentName = applications.student.name

bursary = Bursary.objects.filter(category="Pending")

leastToGreatest = Bursary.objects.all().application_by('id')
greatestToLeast = Bursary.objects.all().application_by('id')

applications = Student.application_set.all()
