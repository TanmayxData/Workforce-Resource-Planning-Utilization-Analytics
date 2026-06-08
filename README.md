# Workforce Resource Planning & Utilization Analytics (WFRPUA)

## Project Overview

Workforce Resource Planning & Utilization Analytics (WFRPUA) is an end-to-end Data Analytics project built using Python, MySQL, and Power BI.

The project focuses on workforce planning, resource allocation, employee utilization, capacity management, project demand analysis, and skills assessment. It demonstrates the complete analytics lifecycle including data validation, data cleaning, SQL analysis, and business intelligence dashboard development.

---

## Business Problem

Organizations need visibility into workforce utilization, project staffing, resource demand, and skill availability to make informed operational decisions.

This project helps answer questions such as:

* Are employees fully utilized?
* Which employees are overutilized or underutilized?
* Are projects receiving sufficient resources?
* What is the organization's available workforce capacity?
* Which skills are most common across the workforce?
* Are there resource allocation gaps?

---

## Objectives

* Validate workforce-related datasets for data quality issues.
* Clean and standardize workforce data.
* Analyze employee utilization and resource allocation.
* Measure project demand versus allocated resources.
* Assess workforce capacity and planning requirements.
* Evaluate workforce skill distribution and capability.
* Build interactive dashboards for operational decision-making.

---

## Datasets

### Employees.csv

Contains employee information:

* Employee ID
* Employee Name
* Department
* Skill
* Capacity Hours

### Projects.csv

Contains project information:

* Project ID
* Project Name
* Start Date
* End Date
* Required Hours

### Resource_Allocation.csv

Contains workforce allocation records:

* Allocation ID
* Employee ID
* Project ID
* Allocated Hours

### Skills_Matrix.csv

Contains employee skill information:

* Employee ID
* Skill
* Level

---

## Data Validation

Validation checks performed include:

### Employees

* Missing Employee IDs
* Missing Employee Names
* Missing Departments
* Missing Skills
* Missing Capacity Hours
* Duplicate Employee Records
* Invalid Capacity Values

### Projects

* Missing Project IDs
* Missing Project Names
* Missing Dates
* Duplicate Projects
* End Date Earlier Than Start Date

### Resource Allocations

* Missing Allocation Records
* Invalid Employee References
* Invalid Project References
* Missing Allocated Hours
* Duplicate Allocation Records

### Skills Matrix

* Missing Skill Records
* Missing Skill Levels
* Duplicate Skill Entries

---

## Data Cleaning

### Employees

* Removed duplicates
* Standardized department names
* Standardized skills
* Corrected data types
* Imputed missing capacity values

### Projects

* Standardized date formats
* Corrected invalid dates
* Handled missing values
* Removed duplicate records

### Allocations

* Removed invalid references
* Corrected allocation values
* Removed duplicates

### Skills

* Standardized skill names
* Standardized skill levels
* Removed duplicate records

---

## SQL Analysis

The project includes workforce analytics such as:

### Workforce Utilization

* Employee Utilization Rate
* Most Utilized Employees
* Least Utilized Employees
* Overutilized Employees
* Underutilized Employees

### Department Analysis

* Employee Distribution
* Department Capacity
* Department Utilization

### Project Resource Planning

* Project Demand Analysis
* Resource Allocation Analysis
* Overallocated Projects
* Underallocated Projects

### Capacity Planning

* Total Workforce Capacity
* Total Demand Hours
* Capacity Gap Analysis

### Skills Analytics

* Skill Distribution
* Skill Level Distribution
* Multi-Skilled Employees

---

## SQL Views

### employee_utilization

Stores:

* Employee Information
* Capacity Hours
* Allocated Hours
* Utilization Percentage

### project_variance

Stores:

* Required Hours
* Actual Allocated Hours
* Variance Hours

---

## Power BI Dashboards

### Workforce Overview

KPIs:

* Total Employees
* Total Projects
* Total Capacity Hours
* Total Allocated Hours

### Utilization Analytics

KPIs:

* Average Utilization
* Overutilized Employees
* Underutilized Employees

### Project Resource Planning

KPIs:

* Total Demand Hours
* Total Allocated Hours
* Capacity Gap

### Skills & Workforce Capability

KPIs:

* Total Skills
* Unique Skills
* Multi-Skilled Employees

---

## Project Workflow

1. Data Collection
2. Data Validation
3. Data Cleaning
4. SQL Database Design
5. Workforce Analytics
6. SQL Views Development
7. Dashboard Development
8. Business Insights Generation

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* MySQL
* Power BI
* Microsoft Excel
* GitHub

---

## Repository Structure

Workforce-Resource-Planning-Utilization-Analytics/

├── Raw Data/

├── Cleaned Data/

├── Validation Report/

├── Python/

├── SQL/

├── Dashboard/

├── Documentation/

└── README.md

---

## Key Skills Demonstrated

* Data Validation
* Data Cleaning
* Data Quality Assessment
* Data Transformation
* SQL Analytics
* SQL Views
* Workforce Planning
* Resource Allocation Analysis
* Capacity Planning
* Power BI Dashboarding
* Business Intelligence Reporting
* End-to-End Data Analytics

---

## Author

Tanmay Sawant


