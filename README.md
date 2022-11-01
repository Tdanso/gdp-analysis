## GDP Analysis

# gdp-analysis

This is about the finding the Max and Min GDP state of USA
and choose a any state of your choice to find out whats the GDP for that state in 2020 
and sub 2020 GDP from 2019 GDP and return the different 

## Results

[How much did New York drop in GDP from 2019 to 2020?
This is GDP from 2019 Minus from 2020
 73216.0
 Informally, what sorts of economic factors influenced this change? Provide evidence if relevant.]
 in my opinion i think its the pandemic enocomic crash in 2020 is the reason for this change.

This is the maximum GDP State
  ('California', 3091871.5)
This is the minimum GDP State
 ('Vermont', 32796.7)
this is the state of New York GDP for 2020
 1699044.7
This is GDP from 2019 Minus from 2020
 73216.0








For this practice, you will create the following 2 functions:

`def get_highest_gdp(data, year):`  
  This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

`def get_lowest_gdp(data, year):`  
  This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

Code to read in this data will already exist. We simply need to modify our filepath to ensure that we are reading data in correctly. This data is being saved to a list called `list_data`.

We will pass this `list_data` list to the `get_highest_gdp` and `get_lowest_gdp` functions and find the state with both the highest & lowest gdp's for the year 2020.