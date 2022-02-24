import csv
import sys
import json

if __name__ == "__main__":
    with open(sys.argv[1]) as f:

        csvReader = csv.reader(f)

        lookups = {}

        volumes = {}
        for row in csvReader:
            #print(row[1])
            #print(row[3])
            id = row[1]
            komprise_path = row[3]
            path_tokens = komprise_path.split('/')
            if len(path_tokens) > 1:
                path_tokens.pop(0)
                path_tokens.pop(0)
                path_tokens.pop(0)
            path_tokens = '/'.join(path_tokens)

            lookups['/' + path_tokens] = id

            #print('/' + path_tokens + ' ' + id)

    f = open('newout.csv', 'w', newline='')
    spamwriter = csv.writer(f, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


    with open(sys.argv[2]) as f:
        ncsvReader = csv.reader(f)

        for row in ncsvReader:
            path = row[7]
            pure_name = row[24]

            try:
                #print(path + ' ' + lookups[path] + ' ' + pure_name + lookups['/' + pure_name])
                print(path + ' ' + lookups[path] + ' ' + pure_name + ' ' + lookups['/' + pure_name])
                row[27] = lookups[path]
                row[28] = lookups['/' + pure_name]
            except:
                print('nope')

            spamwriter.writerow(row)

