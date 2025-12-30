'''

'''

import pandas as pd

def cleanup(dataframe):
    notneeded = dataframe['Not Needed'].str.rstrip(',').dropna()
    print(notneeded)
    # notneeded = list(dataframe.get('Not Needed').str.rstrip(','))
    total = list(dataframe.get('Total').str.rstrip(','))
    print(f"notneeded count: {len(notneeded)}")
    print("//" * 10)
    print(f"total count: {len(total)}")

    for element in notneeded:
        # print(element)
        if str(element) in total:
            total.remove(element)
    # notneeded.remove()
    print(len(total))
    return total


if __name__ == '__main__':
    path = "E:\Mine\Projects\Task-Manager-mobile-app\Promotions\process-mail.xlsx"
    df = pd.read_excel(path, usecols="C,D")
    final = cleanup(df)
    df = pd.DataFrame(final)
    df.to_excel(path, index=False)
