import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv("water_data.csv")

# Inputs and output
X = data[['ph', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity']]
y = data['potability']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# User input
print("Enter water details:")
ph = float(input("pH: "))
hardness = float(input("Hardness: "))
solids = float(input("Solids: "))
chloramines = float(input("Chloramines: "))
sulfate = float(input("Sulfate: "))
conductivity = float(input("Conductivity: "))

# Prediction
result = model.predict([[ph, hardness, solids, chloramines, sulfate, conductivity]])

# Output
if result[0] == 1:
    print("Water is SAFE")
else:
    print("Water is NOT SAFE")
    input("\nPress Enter to exit...")
    