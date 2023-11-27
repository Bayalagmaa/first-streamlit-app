import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Theme  
sns.set_theme(style="whitegrid")

# Page config
st.set_page_config(page_title="Job Explorer", page_icon="📈")  

# Load data  
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df  

df = load_data("jobs.csv")    

# Title
st.title("Job Data Explorer")

# Sector filter   
sector = st.selectbox("Select a sector", df['Sector'].unique())
filtered_df = df[df["Sector"] == sector]  

# Data summary
st.dataframe(filtered_df.describe())

# Salary distribution
plt.figure(figsize=(8, 6))  # Adjust figure size for better spacing

ax = sns.histplot(filtered_df["Salary"])
ax.set(xlabel="Salary")   

# Adjusting x-axis tick labels
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()

# Display the plot using st.pyplot() with the figure object
st.pyplot(plt.gcf())  # Pass in the current figure (gcf)

# Disable the warning
st.set_option('deprecation.showPyplotGlobalUse', False)
