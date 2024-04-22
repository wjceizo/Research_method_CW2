import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'Results_21Mar2022.csv'
data = pd.read_csv(file_path)

# Calculate mean_ghgs_others for each row
data['mean_ghgs_others'] = data['mean_ghgs'] - data['mean_ghgs_ch4'] - data['mean_ghgs_n2o']

# Capitalize the first letter of each gender
data['sex'] = data['sex'].str.capitalize()

# Create a list to store the aggregated data
agg_data = []

# Define the GHG subcategories and their new names
subcategories = {
    'mean_ghgs_ch4': 'GHGs_CH4',
    'mean_ghgs_n2o': 'GHGs_N2O',
    'mean_ghgs_others': 'GHGs_CO2'  # Assuming you want to rename 'mean_ghgs_others' to 'GHGs_CO2'
}

# Loop over each gender, GHG subcategory, and diet type to aggregate the data
for gender in data['sex'].unique():
    for subcategory, new_name in subcategories.items():
        for diet_type in data['diet_group'].unique():
            # Calculate the sum of the GHG subcategory for the current gender and diet type
            sum_ghg = data[(data['diet_group'] == diet_type) & (data['sex'] == gender)][subcategory].sum()
            
            # Append the aggregated data to the list
            agg_data.append({
                'GHG_Type': 'GHG Emissions',
                'Subcategory': new_name,
                'Gender': gender,
                'Diet_Type': diet_type,
                'Sum_GHG': sum_ghg
            })

# Convert the aggregated data list into a DataFrame
agg_df = pd.DataFrame(agg_data)

# Create the treemap using plotly
fig = px.treemap(agg_df, path=['GHG_Type', 'Subcategory', 'Gender', 'Diet_Type'], values='Sum_GHG',
                 color='Sum_GHG', hover_data=['Gender', 'Diet_Type'],
                 color_continuous_scale='peach')

# Show the treemap
fig.show()
