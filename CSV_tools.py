import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def data_prep():


    # Create dataframe, remove unneeded columns, remove rows without ratings
    df = pd.read_csv('./CarRentalDataV1.csv')
    df = df.drop(columns=['location.city', 'location.country', 'location.latitude', 'location.longitude', 'location.state', 'owner.id', 'airportcity'])
    df = df.dropna(subset=['rating'])

    # Create and populate a dictionary of model-fuel type & list of vehicle age
    model_fuel_dict = {}
    vehicle_age_list = []
    for index, row in df.iterrows():
        # Vehicle age
        vehicle_age_list.append(2021 - row['vehicle.year'])

        # model-fuelType
        if row['vehicle.model'] not in model_fuel_dict and not pd.isna(row['fuelType']):
            model_fuel_dict[row['vehicle.model']] = row['fuelType']

    # Add column for vehicle.age
    df['vehicle.age'] = vehicle_age_list

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
    df['fuelType_cat'] = le.fit_transform(df['fuelType'])
    df['vehicle.make_cat'] = le.fit_transform(df['vehicle.make'])
    df['vehicle.model_cat'] = le.fit_transform(df['vehicle.model'])
    df['vehicle.type_cat'] = le.fit_transform(df['vehicle.type'])
    
    # Overwrite the input data with the cleaned up data
    df.to_csv('./CarRentalDataCleaned.csv')