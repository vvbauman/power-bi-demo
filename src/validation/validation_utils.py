import pandas as pd
import pandera as pa

def validate_schema(df : pd.DataFrame, schema : pa.DataFrameSchema, cols : list = []) -> str:
    """ 
    Validate pandas dataframe schema
    First, run schema check using panderas. If schema check fails, check that columns of interest (specified in cols argument) are at least present. 
    If these columns are not present, throw an error. If they are present, return the dataframe. Regardless of outcome, return a message 
    (message intended to display in print statement or in a logger)

    Parameters
    ----------
    df : dataframe you want to validate the schema of
    schema : expected/desired schema of df
    cols : subset of columns in df you require the dataframe to have

    Returns
    ----------
    msg : str describing results of schema check
    """
    try:
        schema.validate(df, lazy= True)
        print('ok')
        msg= 'Correct schema, no action needed'
    except:
        if (len(cols) > 0) & (not set(df.columns) >= set(cols)):
            msg= 'Provided schema does not match dataframe schema. Dataframe also does not have expected columns'
        elif (len(cols) == 0):
            msg= 'Provided schema does not match dataframe schema. Did not check for subset of columns - no argument provided to cols argument'
        elif (len(cols) > 0) & (set(df.columns) >= set(cols)):
            msg= 'Provided schema does not match dataframe schema but dataframe has expected columns'
    return msg