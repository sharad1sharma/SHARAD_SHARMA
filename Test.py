                                                # AI SOFTWARE ENGINEERING
                                                
                                            # 5th Semester – Training Assessment
                                            
                                               # Time: 1 Hour Maximum Marks: 50

# Instructions: Attempt all questions. Select one option for each MCQ. Write clear code and complete SQL queries.


                                             # SECTION A – MCQs (10 × 1 = 10 Marks)

# ----------------------------------------------------------------------------------------------------------

# 1. Which OOP concept allows a child class to reuse parent class features? 
#    B. Inheritance

# 2. Which file mode appends content?
#    C. 'a'

# 3. Output of [x*x for x in range(1, 4)]? 
#    B. [1,4,9]

# 4. Which function applies a function to each iterable item? 
#    C. map()

# 5. Which keyword defines a CTE? 
#    B. WITH

# 6. Which window function gives each row a unique sequential number? 
#    C. ROW_NUMBER()

# 7. Which JOIN returns every possible row combination? A. INNER B. LEFT C. CROSS D. RIGHT
#    C. CROSS

# 8. In a variable-size sliding window, what is commonly moved when its condition is violated? 
#    A. Left pointer 

# 9. Which Python structure is commonly used for frequency counts?
#    B. Dictionary

# 10. In two pointers on a sorted array, if sum is below target, generally move:
#    A. Right pointer left

# ----------------------------------------------------------------------------------------------------------


                                          
                                        # SECTION B – PYTHON PROGRAMMING (2 × 4 = 8 Marks)
                                        # ------------------------------------------------
                                          

# 11. Create a Student class with private name and marks, constructor, getter/setter methods, and a display method. Create and use an
# object.

# ----------------------------------------------------------------------------------------------------------


from sqlite3 import Time


class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

   
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    
    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    
    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

s1 = Student("Rahul", 85)
s1.display()
s1.set_marks(90)

print("Updated Details:")
s1.display()

# ----------------------------------------------------------------------------------------------------------



# 12. Read students.txt, count lines and words, and handle a missing file using exception handling.

# ----------------------------------------------------------------------------------------------------------


try:
    with open("students.txt", "r") as file:
        data = file.read()

        lines = data.splitlines()
        words = data.split()

        print("Total Lines:", len(lines))
        print("Total Words:", len(words))

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An error occurred:", e)
    
# ----------------------------------------------------------------------------------------------------------

    
    
    
                                              # SECTION C – SQL (3 × 4 = 12 Marks)
                                              #  -----------------------------------


# Tables: 

# students(student_id PK, student_name, city, course_id FK); 
# courses(course_id PK, course_name, course_fee);
# results(result_id PK, student_id FK, subject, marks).



# 13. Multiple-table JOIN: Display student name, city, course name, subject and marks by joining all three tables. Include students who
# have not yet received a result, wherever applicable.

# ----------------------------------------------------------------------------------------------------------


# SELECT
#     s.student_name,
#     s.city,
#     c.course_name,
#     r.subject,
#     r.marks
# FROM students s
# INNER JOIN courses c
#     ON s.course_id = c.course_id
# LEFT JOIN results r
#     ON s.student_id = r.student_id;

# ----------------------------------------------------------------------------------------------------------


# 14. JOIN + Aggregates: Display course name, total students enrolled and average marks per course. Show only courses with average
# marks above 70. Use JOIN, COUNT(), AVG(), GROUP BY and HAVING.

# ----------------------------------------------------------------------------------------------------------


# SELECT
#     c.course_name,
#     COUNT(DISTINCT s.student_id) AS total_students,
#     AVG(r.marks) AS average_marks
# FROM courses c
# INNER JOIN students s
#     ON c.course_id = s.course_id
# INNER JOIN results r
#     ON s.student_id = r.student_id
# GROUP BY c.course_id, c.course_name
# HAVING AVG(r.marks) > 70;

# ----------------------------------------------------------------------------------------------------------



# 15. CTE + Window Function: Using a CTE, calculate each student's average marks across subjects. Display student name, average
# marks and rank within their course by average marks descending, using PARTITION BY.

# ----------------------------------------------------------------------------------------------------------


# WITH StudentAverage AS (
#     SELECT
#         s.student_id,
#         s.student_name,
#         s.course_id,
#         AVG(r.marks) AS average_marks
#     FROM students s
#     JOIN results r
#         ON s.student_id = r.student_id
#     GROUP BY
#         s.student_id,
#         s.student_name,
#         s.course_id
# )

# SELECT
#     student_name,
#     average_marks,
#     RANK() OVER (
#         PARTITION BY course_id
#         ORDER BY average_marks DESC
#     ) AS student_rank
# FROM StudentAverage;

# ----------------------------------------------------------------------------------------------------------




                                    # SECTION D – DSA / PROBLEM SOLVING (5 × 4 = 20 Marks)
                                    # ----------------------------------------------------
                                    

# 16. Pattern Recognition: For [2, 4, 6, 8, 10, 12], identify the pattern and write a function checking whether a sequence has a constant
# difference. Return True or False.

# ----------------------------------------------------------------------------------------------------------


# arr = [2, 4, 6, 8, 10, 12]

# difference = arr[1] - arr[0]
# result = True

# for i in range(len(arr) - 1):
#     if arr[i + 1] - arr[i] != difference:
#         result = False
#         break

# print(result)

# ----------------------------------------------------------------------------------------------------------


# 17. Sliding Window: For [2, 1, 5, 1, 3, 2], window size 3, find the maximum sum of a contiguous subarray. Show each window sum.

# ----------------------------------------------------------------------------------------------------------


# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# window_sum = sum(arr[:k])
# maximum = window_sum

# print("Window Sum:", window_sum)

# for i in range(k, len(arr)):

#     window_sum = window_sum + arr[i] - arr[i-k]

#     print("Window Sum:", window_sum)

#     maximum = max(maximum, window_sum)

# print("Maximum Sum:", maximum)

# ----------------------------------------------------------------------------------------------------------


# 18. Two Pointers + Hashing: For sorted array [1, 2, 4, 6, 8, 9] and target 10, find a pair using two pointers and state complexity. Briefly
# explain how a set/dictionary can solve pair-sum for an unsorted array.

# ----------------------------------------------------------------------------------------------------------


# Two Pointers (Sorted Array)

# arr = [1, 2, 4, 6, 8, 9]
# target = 10

# left = 0
# right = len(arr) - 1

# while left < right:

#     total = arr[left] + arr[right]

#     if total == target:
#         print("Two Pointers Pair:", arr[left], arr[right])
#         break

#     elif total < target:
#         left += 1

#     else:
#         right -= 1

# ----------------------------------------------------------------------------------------------------------


# Hashing (Unsorted Array)

# ----------------------------------------------------------------------------------------------------------

# arr = [4, 7, 2, 8, 3]
# target = 10

# seen = set()

# for num in arr:

#     complement = target - num

#     if complement in seen:
#         print("Hashing Pair:", complement, num)
#         break

#     seen.add(num)

# ----------------------------------------------------------------------------------------------------------





# 19. Hashing – Frequency Count: For [4, 2, 4, 3, 2, 4, 1], write a Python function using a dictionary to count each number's frequency.
# Display the most frequent number and its frequency.

# arr = [4, 2, 4, 3, 2, 4, 1]

# freq = {}

# for num in arr:

#     if num in freq:
#         freq[num] += 1

#     else:
#         freq[num] = 1

# print("Frequency:", freq)

# most_frequent = max(freq, key=freq.get)

# print("Most Frequent Number:", most_frequent)
# print("Frequency:", freq[most_frequent])

# ----------------------------------------------------------------------------------------------------------

# Time Complexity: O(n) average

# Space Complexity: O(n)

# ----------------------------------------------------------------------------------------------------------


# 20. Sliding Window – Maximum Sum: For [3, 1, 4, 2, 5, 1, 6] and window size 3, find the maximum contiguous window sum using
# sliding window. State the time complexity.

# arr = [3, 1, 4, 2, 5, 1, 6]
# k = 3

# window_sum = sum(arr[:k])
# maximum = window_sum

# for i in range(k, len(arr)):

#     window_sum = window_sum + arr[i] - arr[i-k]

#     maximum = max(maximum, window_sum)

# print("Maximum Window Sum:", maximum)

# ----------------------------------------------------------------------------------------------------------

# Maximum subarray: [5, 1, 6]

# Time Complexity: O(n)

# Space Complexity: O(1)

# ----------------------------------------------------------------------------------------------------------


                                                        # — End of Question Paper —