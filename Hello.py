import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # Use the 'Agg' backend to prevent conflicts with Streamlit
import matplotlib.pyplot as plt


# Load data from CSV
df = pd.read_csv('jobs.csv')

# Streamlit app
st.title('Jobs Visualization App')

# User input - Select Sector
sectors = df['Sector'].unique()
selected_sector = st.selectbox('Select Sector', sectors)
st.write(f"You selected: {selected_sector}")

# Filter data based on user selection
filtered_data = df[df['Sector'] == selected_sector]

# Visualization
st.subheader('Salary Distribution for Selected Sector')

# Set style and context for seaborn
sns.set(style="whitegrid", palette="pastel")

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(filtered_data['Salary'], kde=True, ax=ax)
ax.set_xlabel('Salary', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.set_title(f'Salary Distribution for {selected_sector}', fontsize=16)
sns.despine()

# Show plot in Streamlit
st.pyplot(fig)