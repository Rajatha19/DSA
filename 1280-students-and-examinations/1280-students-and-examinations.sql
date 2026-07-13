# Write your MySQL query statement below
Select s.student_id, s.student_name, su.subject_name , COUNT(e.student_id) as attended_exams
FROM Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND su.subject_name=e.subject_name
Group by s.student_id, s.student_name, su.subject_name
Order by s.student_id, s.student_name, su.subject_name;