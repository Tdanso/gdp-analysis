import csv
# from tokenize import Name
# from email.errors import MissingHeaderBodySeparatorDefect

def get_highest_gdp(data, year):
    # data is a list of dictionaries
    # year is the 
    state = data[0]["GeoName"]
    max_gdp = float(data[0][year])
        # for each row
    for row in data:
            # if that value is greater than the max I've seen so far
        val = float(row[year])
        if val > max_gdp:
             # set it to be my new max
         max_gdp = val
         state = row["GeoName"]
    return state, max_gdp
    

def get_lowest_gdp(data, year):
    state = data[0]["GeoName"]
    min_gdp = float(data[0][year])
        # for each row
    for row in data:
            # if that value is greater than the max I've seen so far
        val = float(row[year])
        if val < min_gdp:
             # set it to be my new max
            min_gdp = val
            state = row["GeoName"]
    return state, min_gdp

def get_state_gdp(data, state, year):
    # state  = float(data[0][state][year])
    # looping thru the row of clean data 
    for row in data:
            # access volume (dictionary key)
            # val = row["Geo Name"]
        if state == row["GeoName"]:
            return row[year]
            # adding val to state 
            # state += val
        # getting the total 
    # return state

    


# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using 
maxgdp = get_highest_gdp(list_data, '2020')


# get lowest gdp for 2020 using 
mingdp = get_lowest_gdp(list_data, '2020')

# getting the state gdp 
stategdp = get_state_gdp(list_data, "New York",'2020')

pre_2019 = float(get_state_gdp(list_data, "New York",'2019'))
new_2020 = float(get_state_gdp(list_data, "New York",'2020'))


print("This is the maximum GDP State\n ", maxgdp)
print("This is the minimum GDP State\n", mingdp)
print("this is the state of New York GDP for 2020\n", stategdp)
print("This is GDP from 2019 Minus from 2020\n", pre_2019 - new_2020)
