import pandas as pd

isotope_file_H2=pd.read_excel("H2_file.xlsx")
isotope_file_O18=pd.read_excel("O18_file.xlsx")
project_sites=pd.unique(isotope_file_H2['Sample Site Name'])

metadata_library = {
    "Countries/territories":[],
    'Project Region':[],
    'Sample Site Name': [],
    'Latitude': [],
    'Longitude': [],
    'Altitude': [],
    'Measurand Symbol': [],
    'Sample Date start H2': [],
    'Sample Date end H2': [],
    'Sample Date start O18': [],
    'Sample Date end O18': []
}

for site in project_sites:
    # Filter rows corresponding to the current site
    site_data_H2 = isotope_file_H2[isotope_file_H2['Sample Site Name'] == site]
    site_data_O18 = isotope_file_O18[isotope_file_O18['Sample Site Name'] == site]
    
    # Extract relevant information
    metadata_library['Countries/territories'].append(site_data_H2['Countries/territories'].iloc[0])
    metadata_library['Project Region'].append(site_data_H2['Project Region'].iloc[0] if 'Project Region' in site_data_H2.columns else None)
    metadata_library['Sample Site Name'].append(site)
    metadata_library['Latitude'].append(site_data_H2['Latitude'].iloc[0] if 'Latitude' in site_data_H2.columns else None)
    metadata_library['Longitude'].append(site_data_H2['Longitude'].iloc[0] if 'Longitude' in site_data_H2.columns else None)
    metadata_library['Altitude'].append(site_data_H2['Altitude'].iloc[0] if 'Altitude' in site_data_H2.columns else None)
    metadata_library['Measurand Symbol'].append(site_data_H2['Measurand Symbol'].iloc[0] if 'Measurand Symbol' in site_data_H2.columns else None)
    metadata_library['Sample Date start H2'].append(site_data_H2['Sample Date'].iloc[0] if 'Sample Date' in site_data_H2.columns else None)
    metadata_library['Sample Date end H2'].append(site_data_H2['Sample Date'].iloc[-1] if 'Sample Date' in site_data_H2.columns else None)
    metadata_library['Sample Date start O18'].append(site_data_O18['Sample Date'].iloc[0] if 'Sample Date' in site_data_O18.columns else None)
    metadata_library['Sample Date end O18'].append(site_data_O18['Sample Date'].iloc[-1] if 'Sample Date' in site_data_O18.columns else None)

metadata_library_df=pd.DataFrame(metadata_library)
metadata_library_df.to_excel(f"Metadata_{metadata_library_df['Countries/territories'].iloc[0]}.xlsx",index=False)

