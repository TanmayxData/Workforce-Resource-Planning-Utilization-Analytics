import pandas as pd

# ==========================
# LOAD FILES
# ==========================

employees = pd.read_csv("Raw Data/Employees.csv")

projects = pd.read_csv("Raw Data/Projects.csv")

allocations = pd.read_csv("Raw Data/Resource_Allocation.csv")

skills = pd.read_csv("Raw Data/Skills_Matrix.csv")

# ==========================
# VALIDATION RESULTS
# ==========================

results = []

# ==================================================
# EMPLOYEES TABLE
# ==================================================

results.append([
    "Employees",
    "Missing Employee ID",
    employees["Employee_Id"].isnull().sum()
])

results.append([
    "Employees",
    "Missing Employee Names",
    employees["Employee_Name"].isnull().sum()
])

results.append([
    "Employees",
    "Missing Department",
    employees["Department"].isnull().sum()
])

results.append([
    "Employees",
    "Missing Skill",
    employees["Skill"].isnull().sum()
])

results.append([
    "Employees",
    "Missing Capacity Hours",
    employees["CapicityHours"].isnull().sum()
])

results.append([
    "Employees",
    "Duplicate Employees",
    employees.duplicated().sum()
])

# ==================================================
# PROJECTS TABLE
# ==================================================

results.append([
    "Projects",
    "Missing Project ID",
    projects["Project_ID"].isnull().sum()
])

results.append([
    "Projects",
    "Missing Project Name",
    projects["Project_Name"].isnull().sum()
])

results.append([
    "Projects",
    "Missing Start Date",
    projects["Start_Date"].isnull().sum()
])

results.append([
    "Projects",
    "Missing End Date",
    projects["End_Date"].isnull().sum()
])

results.append([
    "Projects",
    "Missing Required Hours",
    projects["Required_Hours"].isnull().sum()
])

results.append([
    "Projects",
    "Duplicate Projects",
    projects.duplicated().sum()
])

# ==================================================
# DATE VALIDATION
# ==================================================

projects["Start_Date"] = pd.to_datetime(projects["Start_Date"],format="%d-%m-%Y",errors="coerce")

projects["End_Date"] = pd.to_datetime(projects["End_Date"],format="%d-%m-%Y",errors="coerce")

invalid_dates = (projects["End_Date"] < projects["Start_Date"]).sum()

results.append(["Projects","End Date Before Start Date",invalid_dates])

# ==================================================
# ALLOCATION TABLE
# ==================================================

results.append([
    "Allocations",
    "Missing Allocation ID",
    allocations["Allocated_Id"].isnull().sum()
])

results.append([
    "Allocations",
    "Missing Employee ID",
    allocations["Employee_Id"].isnull().sum()
])

results.append([
    "Allocations",
    "Missing Project ID",
    allocations["Project_Id"].isnull().sum()
])

results.append([
    "Allocations",
    "Missing Allocated Hours",
    allocations["AllocatedHours"].isnull().sum()
])

results.append([
    "Allocations",
    "Duplicate Allocations",
    allocations.duplicated().sum()
])

# ==================================================
# INVALID EMPLOYEE REFERENCES
# ==================================================

valid_employees = set(
    employees["Employee_Id"].dropna()
)

invalid_employee_refs = (
    ~allocations["Employee_Id"].isin(valid_employees)
).sum()

results.append([
    "Allocations",
    "Invalid Employee References",
    invalid_employee_refs
])

# ==================================================
# INVALID PROJECT REFERENCES
# ==================================================

valid_projects = set(
    projects["Project_ID"].dropna()
)

invalid_project_refs = (
    ~allocations["Project_Id"].isin(valid_projects)
).sum()

results.append([
    "Allocations",
    "Invalid Project References",
    invalid_project_refs
])

# ==================================================
# SKILLS MATRIX
# ==================================================

results.append([
    "Skills",
    "Missing Employee ID",
    skills["Employee_Id"].isnull().sum()
])

results.append([
    "Skills",
    "Missing Skill",
    skills["Skill"].isnull().sum()
])

results.append([
    "Skills",
    "Missing Level",
    skills["Level"].isnull().sum()
])

results.append([
    "Skills",
    "Duplicate Skill Records",
    skills.duplicated().sum()
])

# ==================================================
# CAPACITY VALIDATION
# ==================================================

invalid_capacity = (~employees["CapacityHours"].isin([160,168,176,184])).sum()

results.append([
    "Employees",
    "Invalid Capacity Values",
    invalid_capacity
])

# ==================================================
# SKILL STANDARDIZATION CHECK
# ==================================================

unique_skills = pd.DataFrame(employees["Skill"].dropna().unique(), columns=["Skill Values Found"])

# ==================================================
# CREATE REPORT
# ==================================================

validation_report = pd.DataFrame(results,columns=["Table","Validation_Check","Count"])

print("\nVALIDATION SUMMARY\n")
print(validation_report)

# ==================================================
# EXPORT REPORT
# ==================================================

with pd.ExcelWriter(
    "Validation Report/Validation_Report.xlsx"
) as writer:

    validation_report.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    unique_skills.to_excel(
        writer,
        sheet_name="Skill Values",
        index=False
    )

print("\nValidation Report Saved Successfully.")
