import plotly.express as px
import pandas as pd

file_path = 'Results_21Mar2022.csv' 
data = pd.read_csv(file_path)
data['GHGs_CO2'] = data['mean_ghgs'] - data['mean_ghgs_ch4'] - data['mean_ghgs_n2o']

# Renaming the columns
data.rename(columns={'mean_ghgs_ch4': 'GHGs_CH4', 'mean_ghgs_n2o': 'GHGs_N2O'}, inplace=True)


fig = px.scatter(data, x='GHGs_CH4', y='GHGs_N2O',
                 facet_col='diet_group', color='diet_group',
                 trendline='ols',  
                 title='Scatter plots of CH4 vs. N2O emissions for each Diet Type')

fig.show()

