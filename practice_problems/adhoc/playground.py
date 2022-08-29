# table 1 - employee (1M records)
#
# emp_id first_name last_name manager_id
# 1   Richard      Park      null
# 2   Neel        Gala        1
#
# select e.first_name, e.last_name, m.first_name, m.last_name
# from employee e
# join employee m on e.manager_id = m.emp_id
#
#
# department
# department_id   department_name
# 1                  abc
# 2                   xyz
#
# employee
# emp_id first_name last_name department_id function score
# 1   Richard      Park      1              hr       12
# 2   Neel        Gala        1               hr         45
#
#
# select e.first_name, e.last_name, x.department_name
# from employee e
# join (
#     select
#         department_id, function, max(score)
#     from employee e
#     group by department_id, function
# )d on d.department_id = e.department_id
# join department x on x.department_id = e.department_id

# st = 'abacaba'
# new_st = ''
# for i in range(len(st)-1, -1, -1):
#     new_st += st[i]
# print('palindrome' if st == new_st else 'Not Palindrome')

# st = 'abacaba'
# for i in range(int(len(st)/2)):
#     if st[i] == st[-i-1]:
#         continue
#     else:
#         print('Not palindrome')
#         break
# print('Palindrome')
# # 1, 2, 3, 4, 5, 6, 7