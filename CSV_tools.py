import pandas as pd
import numpy as np
from seaborn import categorical
from sklearn.preprocessing import LabelEncoder

# File-Global variables
categorical_values = {}


def data_prep():

    # Create dataframe, remove unneeded columns, remove rows without ratings
    df = pd.read_csv('./CarRentalDataV1.csv')
    df = df.drop(columns=['reviewCount', 'location.city', 'location.country', 'location.latitude', 'location.longitude', 'location.state', 'owner.id', 'airportcity'])
    df = df.dropna(subset=['rating'])

    # Drop rows with rating under 4.0
    df = df.drop(df[df['rating'] < 4].index)

    # Create and populate a dictionary of model-fuel type & list of vehicle age
    model_fuel_dict = {}
    vehicle_age_list = []
    recommended = []

    for index, row in df.iterrows():
        # Vehicle age
        vehicle_age_list.append(2021 - row['vehicle.year'])

        # model-fuelType
        if row['vehicle.model'] not in model_fuel_dict and not pd.isna(row['fuelType']):
            model_fuel_dict[row['vehicle.model']] = row['fuelType']

        # Add to recommended if rating is 5
        if row['rating'] == 5:
            recommended.append(1)
        else:
            recommended.append(0)

    # Add column for vehicle.age & recommended
    df['vehicle.age'] = vehicle_age_list
    df['recommended'] = recommended

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

    # Create dictionaries of catelogical values
    fuel_types = {}
    vehicle_makes = {}
    vehicle_models = {}
    vehicle_types = {}
    model_to_make = {}

    for i, row in df.iterrows():
        if row['fuelType_cat'] not in fuel_types: 
            fuel_types[row['fuelType_cat']] = row['fuelType']

        if row['vehicle.make_cat'] not in vehicle_makes:
            vehicle_makes[row['vehicle.make_cat']] = row['vehicle.make']

        if row['vehicle.model_cat'] not in vehicle_models:
            vehicle_models[row['vehicle.model_cat']] = row['vehicle.model']
            model_to_make[row['vehicle.model_cat']]  = row['vehicle.make_cat']

        if row['vehicle.type_cat'] not in vehicle_types:
            vehicle_types[row['vehicle.type_cat']] = row['vehicle.type']

    # Add those dictionaries to categorical_values_dict
    categorical_values['fuel_types'] = fuel_types
    categorical_values['vehicle_makes'] = vehicle_makes
    categorical_values['vehicle_models'] = vehicle_models
    categorical_values['vehicle_types'] = vehicle_types
    categorical_values['model_to_make'] = model_to_make

    # Drop catelogical columns we no longer need
    df = df.drop(columns=['fuelType', 'vehicle.make', 'vehicle.model', 'vehicle.type','vehicle.year'])

    # Overwrite the input data with the cleaned up data
    df.to_csv('./CarRentalDataCleaned.csv')