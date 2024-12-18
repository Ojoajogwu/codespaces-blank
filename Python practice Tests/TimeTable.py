import pandas as pd
# Define the subjects for each day
subjects = {
    'Monday': ['Math', 'Science', 'History', 'English'],
    'Tuesday': ['Art', 'Chemistry', 'PE', 'Biology'],
    'Wednesday': ['Drama', 'Geography', 'Math', 'Computer Science']
}
# Create a DataFrame to represent the timetable
timetable = pd.DataFrame(subjects)

# Display the timetable in a friendly format
print("Timetable:")
print(timetable)