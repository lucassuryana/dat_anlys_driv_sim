import pandas as pd

def check_dataframe(dataframe, column_index):
    ''' function to check whether dataframe column has datatype Object or not

        Args:
            dataframe

        Return 
            boolean
    '''
    ans = dataframe.iloc[:,column_index].dtypes == 'O'

    return ans

def empty_dataframe():
    ''' function to create an empty dataframe

        Args: 
            None

        Return: 
            dataframe
    '''

    empty_df = pd.DataFrame()
    
    return empty_df

def bracket_remover(dataframe, column_index):
    ''' function to remove bracket from dataframe

        Args:
            dataframe: raw dataframe from csv
            column_index (int): column index of raw dataframe to be cleaned

        Return:
            dataframe: dataframe with no brackets
    '''
    # remove [ for each column
    dataframe.iloc[:,column_index] = dataframe.iloc[:,column_index].str.replace("[", "", regex = True)
    # remove ] for each column
    dataframe.iloc[:,column_index] = dataframe.iloc[:,column_index].str.replace("]", "", regex = True)
    
    return dataframe

def column_expander(dataframe, column_index):
    ''' function to expand number of column based on number of elements for each column

        Args:
            dataframe: raw dataframe from csv
            column_index (int): column index of dataframe to expand

        Return:
            df_expand: dataframe with expanded columns
    '''

    # number of column to expand
    num = len(dataframe.iloc[:, column_index][0].split())
    df_expand = dataframe.iloc[:,column_index].str.split(',', num, expand=True)

    return df_expand

def rename_column(dataframe, ori_dataframe, column_index):
    ''' function to rename column

        Args:
            dataframe: dataframe to be renamed

        Return:
            dataframe: dataframe with renamed columns
    '''

    dataframe.columns = dataframe.columns.astype('string')
    for i in range(0,len(dataframe.columns)):
        dataframe.columns.values[i] = "{}_{}".format(
            ori_dataframe.columns.values[column_index], i)

    
    return dataframe

def concat_dataframe(df1, df2):
    ''' function to join dataframe

        Args:
            df1: dataframe 1
            df2: dataframe 2
        
        Return:
            df_concat: dataframe that has been concatenated
    '''

    df_concat = pd.concat([df1, df2], axis=1)

    return df_concat