# # Answer question.
# import torch
# from queue_structure import Queue
# from softmax import Softmax, SoftmaxStable
# from stack_structure import Stack
# from ward import Student, Teacher, Doctor, Ward
#
# # Q1
# data = torch.Tensor([1, 2, 3])
# softmax_function = torch.nn.Softmax(dim=0)
# output = softmax_function(data)
# assert round(output[0].item(), 2) == 0.09
# print(f"Question 1: {output}")
#
# # Q2
# data = torch.Tensor([5, 2, 4])
# my_softmax = Softmax()
# output = my_softmax(data)
# assert round(output[-1].item(), 2) == 0.26
# print(f"Question 2: {output}")
#
# # Q3
# data = torch.Tensor([1, 2, 300000000])
# my_softmax = Softmax()
# output = my_softmax(data)
# assert round(output[0].item(), 2) == 0.0
# print(f"Question 3: {output}")
#
# # Q4
# data = torch.Tensor([1, 2, 3])
# my_softmax_stable = SoftmaxStable()
# output = my_softmax_stable(data)
# assert round(output[-1].item(), 2) == 0.67
# print(f"Question 4: {output}")
#
# # Q5
# student = Student(name="studentZ2023 ", yob=2011, grade="6")
# assert student._yob == 2011
# print("Question 5: ")
# student.describe()
#
# # Q6
# teacher = Teacher(name="teacherZ2023", yob=1991, subject="History")
# assert teacher._yob == 1991
# print("Question 6: ")
# teacher.describe()
#
# # Q7
# doctor = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
# assert doctor._yob == 1981
# print("Question 7: ")
# doctor.describe()
#
# # Q8
# student1 = Student(name="studentA", yob=2010, grade="7")
# teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
# teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
# doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
# ward1 = Ward(name="Ward1")
# ward1.add_person(student1)
# ward1.add_person(teacher1)
# ward1.add_person(teacher2)
# ward1.add_person(doctor1)
#
# assert ward1.count_doctor() == 1
#
# doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
# ward1.add_person(doctor2)
#
# print(f"Question 8: {ward1.count_doctor()}")
#
# # Q9
# stack = Stack(capacity=5)
# stack.push(1)
# assert stack.is_full() is False
# stack.push(2)
# print(f"Question 9: {stack.is_full()}")
#
# # Q10
# stack = Stack(capacity=5)
# stack.push(1)
# assert stack.is_full() is False
# stack.push(2)
# print(f"Question 10: {stack.top()}")
#
# # Q11
# queue = Queue(capacity=5)
# queue.enqueue(1)
# assert queue.is_full() is False
# queue.enqueue(2)
# print(f"Question 11: {queue.is_full()}")
#
# # Q12
# queue = Queue(capacity=5)
# queue.enqueue(1)
# assert queue.is_full() is False
# queue.enqueue(2)
# print(f"Question 12: {queue.front()}")
