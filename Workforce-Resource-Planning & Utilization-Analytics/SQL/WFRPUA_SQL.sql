-- create database WFRPUA;

use WFRPUA;


-- =====================================================
-- Q1. Total Employees
-- =====================================================

SELECT COUNT(*) AS Total_Employees
FROM employees_clean;


-- =====================================================
-- Q2. Total Projects
-- =====================================================

SELECT COUNT(*) AS Total_Projects
FROM projects_clean;


-- =====================================================
-- Q3. Total Allocated Hours
-- =====================================================

SELECT SUM(AllocatedHours) AS Total_Allocated_Hours
FROM allocations_clean;


-- =====================================================
-- Q4. Total Workforce Capacity
-- =====================================================

SELECT SUM(CapicityHours) AS Total_Capacity_Hours
FROM employees_clean;


-- =====================================================
-- Utilization View
-- =====================================================

CREATE VIEW employee_utilization AS
SELECT e.Employee_Id, e.Employee_Name, e.Department, e.CapicityHours, SUM(a.AllocatedHours) AS Allocated_Hours,
ROUND(SUM(a.AllocatedHours) * 100.0 /e.CapicityHours,2) AS Utilization_Percentage FROM employees_clean e
JOIN allocations_clean a
    ON e.Employee_Id = a.Employee_Id
GROUP BY
    e.Employee_Id,
    e.Employee_Name,
    e.Department,
    e.CapicityHours;

 
 -- =====================================================
-- Q5. Employee Utilization Rate
-- =====================================================

select* from employee_utilization;


-- =====================================================
-- Q6. Overutilized Employees (>100%)
-- =====================================================

SELECT* FROM employee_Utilization WHERE Utilization_Percentage > 100;


-- =====================================================
-- Q7. Underutilized Employees (<70%)
-- =====================================================

SELECT* FROM employee_utilization WHERE Utilization_Percentage < 70;


-- =====================================================
-- Q8. Department-wise Utilization
-- =====================================================

SELECT Department, SUM(Allocated_Hours) AS Total_Allocated_Hours, SUM(CapicityHours) AS Total_Capacity_Hours,
ROUND(SUM(Allocated_Hours) * 100.0 / SUM(CapicityHours),2) AS Department_Utilization_Percentage FROM employee_utilization
GROUP BY Department
ORDER BY Department_Utilization_Percentage DESC;


-- =====================================================
-- Q9. Department-wise Employee Count
-- =====================================================

SELECT Department, COUNT(*) AS Employee_Count FROM employees_clean
GROUP BY Department
ORDER BY Employee_Count DESC;


-- =====================================================
-- Q10. Average Capacity by Department
-- =====================================================

SELECT Department, ROUND(AVG(CapicityHours),2) AS Avg_Capacity FROM employees_clean GROUP BY Department;


-- =====================================================
-- Q11. Project-wise Resource Allocation
-- =====================================================

SELECT p.Project_ID, p.Project_Name, SUM(a.AllocatedHours) AS Total_Allocated_Hours FROM projects_clean p
JOIN allocations_clean a
ON p.Project_ID = a.Project_Id
GROUP BY p.Project_ID, p.Project_Name
ORDER BY Total_Allocated_Hours DESC;

-- =====================================================
-- Project Variance View
-- =====================================================

CREATE VIEW project_variance AS
SELECT p.Project_ID, p.Project_Name, p.Required_Hours,
SUM(a.AllocatedHours) AS Actual_Allocated_Hours, SUM(a.AllocatedHours) - p.Required_Hours AS Variance_Hours
FROM projects_clean p
JOIN allocations_clean a ON p.Project_ID = a.Project_Id
GROUP BY p.Project_ID, p.Project_Name, p.Required_Hours;


-- =====================================================
-- Q12. Project Demand vs Actual Allocation
-- =====================================================

SELECT* from project_variance 
ORDER BY Variance_Hours DESC;


-- =====================================================
-- Q13 Projects Exceeding Demand
-- =====================================================

SELECT* FROM project_variance WHERE Variance_Hours > 0;


-- =====================================================
-- Q14 Projects Below Demand
-- =====================================================

SELECT* FROM project_variance WHERE Variance_Hours < 0;


-- =====================================================
-- Q15. Skill Distribution
-- =====================================================

SELECT Skill, COUNT(*) AS Skill_Count FROM skills_clean
GROUP BY Skill
ORDER BY Skill_Count DESC;


-- =====================================================
-- Q16. Skill Level Distribution
-- =====================================================

SELECT Level, COUNT(*) AS Employee_Count FROM skills_clean
GROUP BY Level
ORDER BY Employee_Count DESC;


-- =====================================================
-- Q17. Skill Distribution by Level
-- =====================================================

SELECT Skill, Level, COUNT(*) AS Count_Employees FROM skills_clean
GROUP BY Skill, `Level`
ORDER BY Skill, `Level`;


-- =====================================================
-- Q18. Employees with Multiple Skills
-- =====================================================

SELECT Employee_Id, COUNT(*) AS Skill_Count FROM skills_clean
GROUP BY Employee_Id
HAVING COUNT(*) > 1
ORDER BY Skill_Count DESC;


-- =====================================================
-- Q19. Top 10 Most Utilized Employees
-- =====================================================

SELECT* from employee_utilization
ORDER BY Utilization_Percentage DESC
LIMIT 10;


-- =====================================================
-- Q20 Bottom 10 Utilized Employees
-- =====================================================

SELECT* FROM employee_utilization
ORDER BY Utilization_Percentage ASC
LIMIT 10;


-- =====================================================
-- Q21. Total Demand Hours
-- =====================================================

SELECT SUM(Required_Hours) AS Total_Demand_Hours
FROM projects_clean;


-- =====================================================
-- Q22. Available Capacity
-- =====================================================

SELECT SUM(CapicityHours) AS Available_Capacity FROM employees_clean;


-- =====================================================
-- Q23. Capacity Gap Analysis
-- =====================================================

SELECT
    (SELECT SUM(Required_Hours) FROM projects_clean) AS Demand_Hours,
    (SELECT SUM(CapicityHours) FROM employees_clean) AS Capacity_Hours,
    (SELECT SUM(CapicityHours) FROM employees_clean) - (SELECT SUM(Required_Hours) FROM projects_clean)
    AS Capacity_Gap;


-- =====================================================
-- Q24. Average Project Duration
-- =====================================================

SELECT ROUND(AVG(DATEDIFF(End_Date,Start_Date)),2) AS Avg_Project_Duration_Days FROM projects_clean;


-- =====================================================
-- Q25. Longest Duration Projects
-- =====================================================

SELECT Project_ID, Project_Name, DATEDIFF(End_Date,Start_Date) AS Duration_Days FROM projects_clean
ORDER BY Duration_Days DESC;