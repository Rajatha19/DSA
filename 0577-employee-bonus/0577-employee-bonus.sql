# Write your MySQL query statement below
Select e.name , b.bonus
from Employee e
Left Join bonus b
ON e.empId = b.empId
Where b.bonus<1000 or b.bonus is null
