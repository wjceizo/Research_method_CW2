import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'Results_21Mar2022.csv'
data = pd.read_csv(file_path)

# Calculate mean_ghgs_others for each row
data['GHGs_CO2'] = data['mean_ghgs'] - data['mean_ghgs_ch4'] - data['mean_ghgs_n2o']

# Create a list to store the aggregated data
agg_data = []

# Define the GHG subcategories and use the new name for 'mean_ghgs_others'
subcategories = ['mean_ghgs_ch4', 'mean_ghgs_n2o', 'GHGs_CO2']

# Loop over each diet type, GHG subcategory, and age group to aggregate the data
for diet_type in data['diet_group'].unique():
    for subcategory in subcategories:
        for age_group in data['age_group'].unique():
            # Calculate the sum of the GHG subcategory for the current diet type and age group
            sum_ghg = data[(data['diet_group'] == diet_type) & (data['age_group'] == age_group)][subcategory].sum()
            
            # Append the aggregated data to the list
            agg_data.append({
                'GHG_Type': 'GHG Emissions',
                'Subcategory': subcategory,
                'Diet_Type': diet_type,
                'Age_Group': age_group,
                'Sum_GHG': sum_ghg
            })

# Convert the aggregated data list into a DataFrame
agg_df = pd.DataFrame(agg_data)

# Create the treemap using plotly
fig = px.treemap(agg_df, path=['GHG_Type', 'Subcategory', 'Diet_Type', 'Age_Group'], values='Sum_GHG',
                 color='Sum_GHG', hover_data=['Diet_Type', 'Age_Group'],
                 color_continuous_scale='peach')  # Changed to Viridis color scale for aesthetic preference

# Show the treemap
fig.show()
