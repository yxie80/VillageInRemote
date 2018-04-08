import pandas as pd


class Server:
    # doc stored in the server for basic structure
    base = pd.read_csv('Comm.csv', low_memory=False)
    base["Filter UNSPSC of Interest"] = base["Filter UNSPSC of Interest"].astype("category")
    base["Filter UNSPSC of Interest"].cat.set_categories(["Rest of Categories", "Categories of Interest"], inplace=True)

    temp = base[['UNSPSC Title', 'Filter UNSPSC of Interest']]
    grouped = temp.groupby(by=['UNSPSC Title'])

    # dataframe used to match category of interest
    # for those files missing with 'Filter UNSPSC of Interest'
    match_df = grouped.last()

