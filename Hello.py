# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib
# matplotlib.use("Agg")  # Use the 'Agg' backend to prevent conflicts with Streamlit
# import matplotlib.pyplot as plt


# Imports
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
fig, ax = plt.subplots()
sns.histplot(filtered_df["Salary"], ax=ax)
ax.set(xlabel="Salary")  
st.pyplot(fig)

# Other visualizations...

# Footer 
st.write("""**Data source:** *jobs.csv*""")