from pandas import read_csv


def drop_index():
    df = read_csv("D:\DB Cleanup - V2.0.csv")

    df['query'] = 'DROP INDEX IF EXISTS ' + df['schema'] + '.' + df['Index'] + ';'
    except_list = ['20220331', '20220401']
    for x in except_list:
        df = df[df["query"].str.contains(x) == False]
    final_query = '\n'.join([x for x in df['query']])
    with open('final_query.txt', 'w') as f:
        f.write(final_query)


if __name__ == '__main__':
    drop_index()