import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Provisional_COVID-19_Deaths_by_Sex_and_Age .csv")
print(df.head())
print(df.info())

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

#Handling Missing Data
df_cleaned = df.dropna(subset=['Year'])

# OBJECTIVE 1: Age-wise COVID-19 Deaths
age_data = df.groupby("Age Group")["COVID-19 Deaths"].sum().dropna()
plt.bar(age_data.index, age_data.values, color='skyblue')
plt.title("COVID-19 Deaths by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Deaths")
plt.xticks(rotation=90)
plt.show()

# OBJECTIVE 2: Trend of COVID-19, Pneumonia, and Influenza Deaths
df2 = df.dropna(subset=['Year'])
data = df2.groupby("Year")[["COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]].sum()
plt.plot(data.index, data["COVID-19 Deaths"], 'r*-', label="COVID-19")
plt.plot(data.index, data["Pneumonia Deaths"], 'go--', label="Pneumonia")
plt.plot(data.index, data["Influenza Deaths"], 'bs-.', label="Influenza")
plt.title("Yearly Deaths: COVID-19 vs Pneumonia vs Influenza")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.legend()
plt.grid(True)
plt.show()

# OBJECTIVE 3: Year-wise COVID-19 Deaths
df_clean = df.dropna(subset=["Year"])
yearly_deaths = df_clean.groupby("Year")["COVID-19 Deaths"].sum()
plt.bar(yearly_deaths.index.astype(str), yearly_deaths.values, color='skyblue')
plt.title("Year-wise COVID-19 Deaths")
plt.xlabel("Year")
plt.ylabel("Total Deaths")
plt.grid(axis='y')
plt.show()

# OBJECTIVE 4: Gender-wise COVID-19 Deaths
gender_deaths = df.groupby("Sex")["COVID-19 Deaths"].sum().dropna()
plt.pie(gender_deaths.values, labels=gender_deaths.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title("Gender-wise Distribution of COVID-19 Deaths")
plt.axis('equal')  # Equal aspect ratio for a perfect circle
plt.show()

# OBJECTIVE 5: State-wise COVID-19 Deaths (Top 20)
state = df.groupby("State")["COVID-19 Deaths"].sum().dropna().sort_values(ascending=False).head(20)
plt.figure(figsize=(10,5))
plt.bar(state.index, state.values, color='teal')
plt.title("Top 20 US States by COVID-19 Deaths")
plt.xlabel("State")
plt.ylabel("Total Deaths")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
