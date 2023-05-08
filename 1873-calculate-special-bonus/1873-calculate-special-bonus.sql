# Write your MySQL query statement below
SELECT employee_id, salary * ( employee_id%2 ) * ( name NOT LIKE 'M%') AS bonus FROM employees
ORDER BY employee_id;




  