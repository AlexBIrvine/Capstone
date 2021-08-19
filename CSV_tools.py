import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def data_prep():


    # Create dataframe, remove unneeded columns, remove rows without ratings
    df = pd.read_csv('./CarRentalDataV1.csv')
    df = df.drop(columns=['location.city', 'location.country', 'location.latitude', 'location.longitude', 'location.state', 'owner.id', 'airportcity'])
    df = df.dropna(subset=['rating'])

    # Create and populate a dictionary of model-fuel type
    model_fuel_dict = {}
    for index, row in df.iterrows():
        if row['vehicle.model'] not in model_fuel_dict and not pd.isna(row['fuelType']):
            model_fuel_dict[row['vehicle.model']] = row['fuelType']

    # Update rows missing a fuel type where able, drop when unable
    indexes_to_drop = []
    for i, row in df.iterrows():
        if pd.isna(row['fuelType']) and row['vehicle.model'] in model_fuel_dict:
            df.at[i, 'fuelType'] = model_fuel_dict[row['vehicle.model']]

        if pd.isna(row['fuelType']) and not row['vehicle.model'] in model_fuel_dict:
            indexes_to_drop.append(i)

    # Drop rows when unable to update fuel type
    for index in indexes_to_drop:
        df = df.drop([index])
    
    # Create label columns for string based columns
    le = LabelEncoder()
    # fuel type
    # Make
    # model
    # vehicle type
    
    return df