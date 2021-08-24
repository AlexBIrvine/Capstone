import pandas as pd
import numpy as np
import json
from seaborn import categorical
from sklearn.preprocessing import LabelEncoder

# File-Global variables
categorical_values = {}


def data_prep():
    """
    Reads in raw CSV file and modifies it for use.  Saves a separate file upon completion.  

    Steps taken in this function:
    - Drops unneeded columns: reviewCount, city, country, latitude/longitdue, state, ownerID & airport city
    - Removes all rows where rating is blank
    - Removes the few rows where rating is below a 4 (in data exploration phase, this was found to be very low reviews with minimal trips and would not represent the model on a whole)
    - Creates a column for vehicle age calculated from 2021
    - Creates a column with binary (1/0) result for recommended vehicle.  A vehicle is recommended if it received a 5-star rating.
    - Fills in fuel type for vehicles that don't have it listed based on the fuel types found in matching models.  
    - Removes rows for vehicles of unknown fuel types
    - Creates numerical representations of catelogical values (strings)
    - Saves those representations as separate rows

    """
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


    # Save as CSV file
    df.to_csv('./CarRentalDataCleaned.csv')


def create_catelogical_json():
    """
    Creates a JSON file that is used to map catelogical values (strings) to their numerical values.  
    """
    # Read in cleaned data
    df = pd.read_csv('./CarRentalDataCleaned.csv')

    # Create dictionaries of catelogical values
    fuel_types = {}
    vehicle_makes = {}
    vehicle_models = {}
    vehicle_types = {}
    model_to_make = {}
    model_to_vType = {}
    model_to_fType = {}

    # Loop through the dataframe and add records to the above dictionaries if not already stored
    for i, row in df.iterrows():

        if row['fuelType_cat'] not in fuel_types: 
            fuel_types[row['fuelType_cat']] = row['fuelType']

        if row['vehicle.make_cat'] not in vehicle_makes:
            vehicle_makes[row['vehicle.make_cat']] = row['vehicle.make']

        if row['vehicle.model_cat'] not in vehicle_models:
            vehicle_models[row['vehicle.model_cat']] = row['vehicle.model']
            model_to_make[row['vehicle.model_cat']]  = row['vehicle.make_cat']
            model_to_vType[row['vehicle.model_cat']] = row['vehicle.type_cat']
            model_to_fType[row['vehicle.model_cat']] = row['fuelType_cat']

        if row['vehicle.type_cat'] not in vehicle_types:
            vehicle_types[row['vehicle.type_cat']] = row['vehicle.type']

    # Add those dictionaries to categorical_values_dict
    categorical_values['fuel_types'] = fuel_types
    categorical_values['vehicle_makes'] = vehicle_makes
    categorical_values['vehicle_models'] = vehicle_models
    categorical_values['vehicle_types'] = vehicle_types
    categorical_values['model_to_make'] = model_to_make
    categorical_values['model_to_vType'] = model_to_vType
    categorical_values['model_to_fType'] = model_to_fType

    # Save dictionary to file
    with open("categorical_values.json", "w") as output:
        json.dump(categorical_values, output)


def get_catelogical_dict():
    """
    Opens and returns the JSON created in the `create_catelogical_json` function as a dictionary.
    """
    with open('categorical_values.json') as json_file:
        return json.load(json_file)