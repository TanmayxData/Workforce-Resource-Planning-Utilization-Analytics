import pandas as pd

# ==================================
# LOAD FILES
# ==================================

employees = pd.read_csv("Raw Data/Employees.csv")

projects = pd.read_csv("Raw Data/Projects.csv")

allocations = pd.read_csv("Raw Data/Resource_Allocation.csv")

skills = pd.read_csv("Raw Data/Skills_Matrix.csv")

# ==================================
# EMPLOYEES CLEANING
# ==================================

employees = employees.drop_duplicates()

employees = employees.dropna(
    subset=["Employee_Name"]
)

employees["Department"] = employees["Department"].fillna("Unknown")

employees["Skill"] = employees["Skill"].fillna("Unknown")

employees["CapicityHours"] = employees["CapicityHours"].fillna(employees["CapicityHours"].median())

employees["Employee_Name"] = (employees["Employee_Name"].astype(str).str.strip().str.title())

employees["Department"] = (employees["Department"].astype(str).str.strip())

employees["Skill"] = (employees["Skill"].astype(str).str.strip())

employees["CapicityHours"] = (employees["CapicityHours"].astype(int))

# ==================================
# PROJECTS CLEANING
# ==================================

projects = projects.drop_duplicates()

projects = projects.dropna(subset=["Project_ID"])

projects = projects.dropna(subset=["Project_Name"])

projects["Start_Date"] = pd.to_datetime(projects["Start_Date"],format="%d-%m-%Y",errors="coerce")

projects["End_Date"] = pd.to_datetime(projects["End_Date"],format="%d-%m-%Y",errors="coerce")

# Fix invalid dates

mask = projects["End_Date"] < projects["Start_Date"]

projects.loc[mask, "End_Date"] = (projects.loc[mask, "Start_Date"])

projects["Required_Hours"] = (projects["Required_Hours"].fillna(projects["Required_Hours"].median()))

projects["Required_Hours"] = (projects["Required_Hours"].astype(int))

# MySQL format

projects["Start_Date"] = (projects["Start_Date"].dt.strftime("%Y-%m-%d"))

projects["End_Date"] = (projects["End_Date"].dt.strftime("%Y-%m-%d"))

# ==================================
# ALLOCATIONS CLEANING
# ==================================

allocations = allocations.drop_duplicates()

allocations = allocations.dropna(subset=["Allocated_Id"])

allocations = allocations.dropna(subset=["Employee_Id"])

allocations = allocations.dropna(subset=["Project_Id"])

allocations["AllocatedHours"] = (allocations["AllocatedHours"].fillna(allocations["AllocatedHours"].median()))

allocations["AllocatedHours"] = (allocations["AllocatedHours"].astype(int))

# ==================================
# REMOVE INVALID REFERENCES
# ==================================

valid_employee_ids = set(employees["Employee_Id"])

valid_project_ids = set(projects["Project_ID"])

allocations = allocations[allocations["Employee_Id"].isin(valid_employee_ids)]

allocations = allocations[allocations["Project_Id"].isin(valid_project_ids)]

# ==================================
# SKILLS CLEANING
# ==================================

skills = skills.drop_duplicates()

skills = skills.dropna(subset=["Employee_Id"])

skills = skills.dropna(subset=["Skill"])

skills = skills.dropna(subset=["Level"])

skills["Skill"] = (skills["Skill"].astype(str).str.strip())

skills["Level"] = (skills["Level"].astype(str).str.strip())

# ==================================
# EXPORT CLEAN FILES
# ==================================

employees.to_csv("Cleaned Data/Employees_Clean.csv",index=False)

projects.to_csv("Cleaned Data/Projects_Clean.csv",index=False)

allocations.to_csv("Cleaned Data/Allocations_Clean.csv",index=False)

skills.to_csv("Cleaned Data/Skills_Clean.csv",index=False)

print("Cleaning completed successfully.")
print("Cleaned files exported.")