import pandas as pd
import numpy as np
import pytest
from src.utils.ingestion_utils import drop_nulls

@pytest.mark.parametrize("test_nans", [0, 5, 10, 3])
def test_drop_nulls(test_nans):
    df= pd.DataFrame(np.random.randint(0, 100, size= (100, 4)), columns= list('ABCD'))
    df.iloc[:test_nans, 0]= np.nan
    df_drop_nulls= drop_nulls(df= df)
    assert df_drop_nulls.equals(df)