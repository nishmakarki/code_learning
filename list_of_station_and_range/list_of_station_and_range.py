import pandas as pd
import os

def metadata_filter(filename):          #defining function and using filename as a variable to call the function which is described later
    data = pd.read_excel(filename)

    # Ensure date columns are in datetime format and handle errors
    date_columns = ['Sample Date start H2', 'Sample Date end H2', 
                    'Sample Date start O18', 'Sample Date end O18']

    for col in date_columns:            #col holds a data from the column of 'Sample Data start H2' at a time then for other 
        data[col] = pd.to_datetime(data[col], errors='coerce')      #each data_column is converted to pandas datetime format

    # Extract just the date (yyyy-mm-dd), handle NaT values safely
    for col in date_columns:
        data[col] = data[col].apply(lambda x: x.date() if pd.notnull(x) else None)

    # Calculate years of data availability
    data['Years H2'] = (pd.to_datetime(data['Sample Date end H2']) - 
                        pd.to_datetime(data['Sample Date start H2'])).dt.days / 365.25
    data['Years O18'] = (pd.to_datetime(data['Sample Date end O18']) - 
                         pd.to_datetime(data['Sample Date start O18'])).dt.days / 365.25

    # Filter for stations with >10 years of data for both H2 and O18
    filtered_data = data[(data['Years H2'] > 10) & (data['Years O18'] > 10)]        #library that saves the function data
    
    # Drop unnecessary columns
    filtered_data.drop(columns=['Measurand Symbol'], inplace=True)

    return filtered_data        #returns values to  the function metadata_filter(filename) as it is called by it and returned to it as well

all_filtered_data = pd.DataFrame()  #New empty pandas dataframe initialization

for filename in os.listdir():       #os.listdir() to list all files in current directory
    if filename.startswith('Metadata_'):
        filtered_metadata_data=metadata_filter(filename)            
        all_filtered_data = pd.concat([all_filtered_data, filtered_metadata_data], ignore_index=True)       #need this to change filöe from library to pandas

filtered_metadata_data_df=pd.DataFrame(all_filtered_data)       #convert from dataframe to panda
filtered_metadata_data_df.to_excel(f"Complete_station_list.xlsx",index=False)
print('the run is complete')
