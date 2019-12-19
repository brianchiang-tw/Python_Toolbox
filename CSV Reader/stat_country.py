import csv

# open CSV file
with open('test.csv', encoding='utf-8') as csvfile:

    country = ['美國','法國','日本']
    country_occ = dict().fromkeys(country, 0)

    # read csv as python dictionary
    rows = csv.DictReader(csvfile)

    fields = rows.fieldnames
    # print fieldname of csv file
    #print("fieldnames of dictionary: {}".format( fields ) )

    for row in rows:
        for single_field in fields:
            value = row[single_field]

            for c in country:
                if c in value:

                    country_occ[c] = country_occ.get(c, 0) + value.count(c)

    # output occurrence of each country
    print( country_occ )