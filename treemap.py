import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'Results_21Mar2022.csv'
data = pd.read_csv(file_path)

# Calculate mean_ghgs_co2 for each row
data['GHGs_CO2'] = data['mean_ghgs'] - data['mean_ghgs_ch4'] - data['mean_ghgs_n2o']

# Create a list to store the aggregated data
agg_data = []

# Define the GHG subcategories with updated names
subcategories = ['GHGs_CH4', 'GHGs_N2O', 'GHGs_CO2']
subcategories_mapping = {
    'GHGS':'mean_ghgs',
    'GHGs_CH4': 'mean_ghgs_ch4',
    'GHGs_N2O': 'mean_ghgs_n2o',
    'GHGs_CO2': 'GHGs_CO2'
}

# Loop over each diet type and GHG subcategory to aggregate the data
for diet_type in data['diet_group'].unique():
    for subcategory in subcategories:
        # Use the mapping to get the corresponding column in the original data
        original_column = subcategories_mapping[subcategory]
        
        # Calculate the sum of the GHG subcategory for the current diet type
        sum_ghg = data[data['diet_group'] == diet_type][original_column].sum()
        
        # Append the aggregated data to the list
        agg_data.append({
            'GHG_Type': 'GHG Emissions',
            'Subcategory': subcategory,
            'Diet_Type': diet_type,
            'Sum_GHG': sum_ghg
        })

# Convert the aggregated data list into a DataFrame
agg_df = pd.DataFrame(agg_data)

# Create the treemap using plotly
fig = px.treemap(agg_df, path=['GHG_Type', 'Subcategory', 'Diet_Type'], values='Sum_GHG',
                 color='Sum_GHG', hover_data=['Diet_Type'],
                 color_continuous_scale='peach')
fig.update_layout(
    margin = dict(t=50, l=25, r=25, b=25)
)
# Show the treemap
fig.show()
fig.write_image("treemap_high_res.png", width=2800, height=1600)