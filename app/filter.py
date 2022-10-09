import pandas as pd
import csv
import datetime as dt
from datetime import datetime, timedelta

def addRegion(path):
    regions = pd.read_csv('regions.csv', index_col=0, squeeze=True).to_dict()
    df = pd.read_csv(path)
    df['region'] = [regions[state] for state in df['state']]
    df.to_csv('out2.csv', index=False)

def aggregateHelper(row, dict, start):
    week = dt.timedelta(days = 7 * ((row['date'] - start).days // 7)) + start
    if (week in dict[row['state']]):
        pair = dict[row['state']][week]
        dict[row['state']][week] = ((pair[0] * pair[1] + row['sentiment']) / (pair[1] + 1), pair[1] + 1)
    else:
        dict[row['state']][week] = (row['sentiment'], 1)

def politicalHelper(row, political, dummy):
    political[row['state']] = "Democrat" if (row['clinton'] > row['trump']) else "Republican"

def aggregate(path, out):
    df = pd.read_csv(path)
    states = pd.read_csv('states.csv')
    political = {}
    states.apply(politicalHelper, axis = 1, args=(political, 0))

    regions = pd.read_csv('regions.csv', index_col=0, squeeze=True).to_dict()

    df['date'] = [datetime.strptime(date.split(" ")[0], r"%Y-%m-%d") for date in df['date']]
    start = min(df['date'])
    end = datetime.strptime("2019-01-06", r"%Y-%m-%d")

    dict = {}
    for state in regions:
        dict[state] = {}    

    df.apply(aggregateHelper, axis = 1, args=(dict, start))

    with open(out, 'w', newline='') as fout:
        writer = csv.writer(fout)

        header = ["state", "region", "political"]
        week = start
        weeks = []
        while (week <= end):
            header.append(week.strftime(r"%Y-%m-%d"))
            weeks.append(week)
            week += timedelta(days = 7)
        
        writer.writerow(header)

        for state in dict:
            row = [state, regions[state], political[state]]
            previous = 0
            for week in weeks:
                if (week in dict[state]):
                    previous = dict[state][week][0]
                row.append(previous)

            writer.writerow(row)
    
    
    
aggregate("minor.csv", "minor2.csv")

