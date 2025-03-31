import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv("complete.csv")

# Generate the profile report
profile = ProfileReport(df, explorative=True)

# Save the report as index.html
profile.to_file("index.html")

print("Pandas Profiling report saved as index.html")
