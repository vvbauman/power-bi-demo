import pandas as pd
import pandera as pa
import logging

from src.validation.validation_utils import validate_schema

def ingest_flat_file(path : str, filename : str, schema : pa.DataFrameSchema, sep : str = ',') -> tuple([pd.DataFrame, str]):
    """
    Ingest a flat file saved to path and validate schema of ingested dataframe
    Acceptable file formats are .csv, .txt, and .pkl. Any other provided formats will throw an error
    Schema of ingested dataframe must exactly match the input argument schema otherwise an error will be thrown

    Parameters
    ----------
    path : absolute path to flat file, not including the flat file name and extension itself
    filename : name and extension of flat file to be ingested
    schema : expected schema of the ingested file
    sep : separator to use in pd.read_csv() when attempting to ingest the flat file

    Returns
    ----------
    df : ingested data
    msg : str describing the results of data ingestion and schema check. Intended to display in print statement or log

    """
    try:
        df= pd.read_csv(path + filename, sep= sep)
    except: 
        try: 
            df= pd.read_pickle(path + filename)
        except:
            raise(Exception)

    try:
        validate_schema(df= df, schema= schema)
        msg= 'Dataframe successfully ingested and has expected schema'
    except:
        msg= 'Dataframe successfully ingested but does not have expected schema'
    
    return df, msg

def save_flat_file(path : str, filename : str, df : pd.DataFrame) -> str:
    """ 
    Save a pandas dataframe as a flat file to a specified location

    Parameters
    ----------
    path : absolute path to where the flat file should be saved. Do not include name or extension to save table as
    filename : name and extension to save dataframe under 
    df : pandas dataframe to save as a flat file. This function does not include any data validation, so it should be conducted before running this function

    Returns
    ----------
    msg : str describing the results of writing the dataframe. Intended to display in print statement or log
    """
    try: 
        df.to_csv(path + filename)
        msg= f'Dataframe successfully written to {path} (filename: {filename})'
    except:
        msg= f'Dataframe write unsuccessful. Check provided path and filename are correct (path: {path}, filename: {filename})'
    return msg

def drop_nulls(df : pd.DataFrame, subset : list = [], logger : logging.Logger = None) -> pd.DataFrame:
    """ 
    Function to drop rows in a dataframe containing null values, if the % of rows with null values is less than 5% of the entire dataframe length
    If logging.Logger object provided to input arguments, log messages on rows being dropped will be written to logger

    Parameters
    ----------
    df : dataframe to check for null values
    subset : list of str. Columns in df to consider when checking for null values. 
            If this argument is provided, any columns not in this list are not considered when checking for nulls
    logger : logging.Logger object to write log messages to

    Returns
    ----------
    df : same as input df but with rows with null values dropped (as long as they account for less than 5% of the data)
    """
    if len(subset) == 0:
        percent_null= df.isnull().sum().sum() / len(df)
    else:
        percent_null= df[subset].isnull().sum().sum() / len(df)

    if percent_null == 0:
        if isinstance(logger, logging.Logger):
            logger.info('No null values in dataframe. Returned dataframe is same as input dataframe')
        return df
    elif percent_null < 0.05:
        if isinstance(logger, logging.Logger):
            logger.warning('Less than 5% of rows are missing data. Returned dataframe is same as input dataframe with these rows dropped')
        return df.dropna(subset= subset)
    else:
        if isinstance(logger, logging.Logger):
            logger.warning('More than 5% of rows are missing data. Returning dataframe without dropping rows')
        return df