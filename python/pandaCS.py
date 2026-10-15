import pandas as pd

# ============================================================
# PANDAS CASE STUDY: COLLEGE STUDENT PERFORMANCE ANALYSIS
# ============================================================


# ------------------------------------------------------------
# 1. pd.Series()
# Create a one-dimensional Pandas Series
# ------------------------------------------------------------

names = pd.Series([
    "Amit",
    "Riya",
    "Neha",
    "Rahul",
    "Sneha"
])

print("========== STUDENT NAMES ==========")
print(names)


# ------------------------------------------------------------
# 2. Create a dictionary containing student data
# ------------------------------------------------------------

data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Riya", "Neha", "Rahul", "Sneha"],
    "Department": ["MCA", "MCA", "MSc", "MSc", "MCA"],
    "Marks": [78, 92, 65, 88, 55],
    "Attendance": [85, 92, 78, 88, 60],
    "City": ["Pune", "Mumbai", "Pune", "Nashik", "Pune"]
}


# ------------------------------------------------------------
# 3. pd.DataFrame()
# Convert the dictionary into a Pandas DataFrame
# ------------------------------------------------------------

df = pd.DataFrame(data)

print("\n========== COMPLETE DATA ==========")
print(df)


# ------------------------------------------------------------
# 4. df.head()
# Display the first 3 records
# ------------------------------------------------------------

print("\n========== FIRST 3 RECORDS ==========")
print(df.head(3))


# ------------------------------------------------------------
# 5. df.tail()
# Display the last 3 records
# ------------------------------------------------------------

print("\n========== LAST 3 RECORDS ==========")
print(df.tail(3))


# ------------------------------------------------------------
# 6. df.shape
# Display number of rows and columns
# ------------------------------------------------------------

print("\n========== SHAPE ==========")
print(df.shape)


# ------------------------------------------------------------
# 7. df.columns
# Display all column names
# ------------------------------------------------------------

print("\n========== COLUMN NAMES ==========")
print(df.columns)


# ------------------------------------------------------------
# 8. df.info()
# Display DataFrame structure and data types
# ------------------------------------------------------------

print("\n========== DATAFRAME INFORMATION ==========")
df.info()


# ------------------------------------------------------------
# 9. df.describe()
# Display statistical summary of numerical columns
# ------------------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ------------------------------------------------------------
# 10. Select a single column
# Display only Marks
# ------------------------------------------------------------

print("\n========== MARKS ==========")
print(df["Marks"])


# ------------------------------------------------------------
# Select multiple columns
# ------------------------------------------------------------

print("\n========== NAME AND MARKS ==========")
print(df[["Name", "Marks"]])


# ------------------------------------------------------------
# 11. Filtering
# Display students whose marks are greater than 70
# ------------------------------------------------------------

print("\n========== STUDENTS WITH MARKS > 70 ==========")

high_scorers = df[df["Marks"] > 70]

print(high_scorers)


# ------------------------------------------------------------
# 12. df.sort_values()
# Sort students according to marks
# Highest marks first
# ------------------------------------------------------------

print("\n========== SORTED BY MARKS ==========")

sorted_df = df.sort_values(
    "Marks",
    ascending=False
)

print(sorted_df)


# ------------------------------------------------------------
# 13. df.rename()
# Rename Marks column as Percentage
# ------------------------------------------------------------

df = df.rename(
    columns={
        "Marks": "Percentage"
    }
)

print("\n========== AFTER RENAMING ==========")
print(df)


# ------------------------------------------------------------
# 14. df.drop()
# Remove the City column
# ------------------------------------------------------------

df = df.drop(
    columns=["City"]
)

print("\n========== AFTER DROPPING CITY ==========")
print(df)


# ------------------------------------------------------------
# 15. Introduce a missing value
# We deliberately create a missing Attendance value
# ------------------------------------------------------------

df.loc[2, "Attendance"] = None

print("\n========== DATA WITH MISSING VALUE ==========")
print(df)


# ------------------------------------------------------------
# 16. df.isnull()
# Check which values are missing
# True means the value is missing
# ------------------------------------------------------------

print("\n========== CHECK MISSING VALUES ==========")

print(df.isnull())


# ------------------------------------------------------------
# Count missing values in each column
# ------------------------------------------------------------

print("\n========== NUMBER OF MISSING VALUES ==========")

print(df.isnull().sum())


# ------------------------------------------------------------
# 17. df.fillna()
# Calculate average attendance
# and use it to fill the missing value
# ------------------------------------------------------------

average_attendance = df["Attendance"].mean()

df["Attendance"] = df["Attendance"].fillna(average_attendance)

print("\n========== AFTER FILLING MISSING VALUE ==========")
print(df)


# ------------------------------------------------------------
# 18. df.groupby()
# Group students according to Department
# Calculate average percentage for each department
# ------------------------------------------------------------

print("\n========== DEPARTMENT-WISE AVERAGE ==========")

department_average = df.groupby(
    "Department"
)["Percentage"].mean()

print(department_average)


# ============================================================
# END OF PROGRAM
# ============================================================
