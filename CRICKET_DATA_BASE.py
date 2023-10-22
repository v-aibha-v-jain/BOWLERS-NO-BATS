# This is an project on handling an csv file having data on cricket world cup of different matches
# As we know there are many matches and teams and every team as 11 players
# It is recomended to have a look on the csv file once


import pandas as pd


df = pd.read_csv("/home/vaibhav/Desktop/waste/Bowling.csv")

df.drop_duplicates()


# As we see in the csv file that there are 10 * 11 sets of same match name 
# each set of 11 rows has one of its column filled excluding match column
# So the thing is we need to bring all the separated out columns in a single set of rows (11 rows)


# We had already read the csv file using pandas and stored it in the variable df
# Now let's try to solve this problem by creating new dataframe with only those columns which have values for all 11 player names


# Now let's create a new list which will be having all 11 players of each respective match
new_name_l = []
n = -1
nl = []
name_column = df["Name"]
namelist = list(name_column)
for i in namelist:
  n = n+1
  if type(i) == float:
    continue
  else:
    new_name_l.append(i)
    nl.append(n)

# Now let's create a new list which will be having the numbers of overs played by each player of each match
new_over_l = []
over_column = df["overs"]
overlist = list(over_column)
for i in overlist:
  if i>=-1 or i<=10:
    new_over_l.append(i)

# Now let's create a new list which will be having the runs scored by all the players on all the matchs
new_run_l = []
run_column = df["runs"]
runlist = list(run_column)
for i in runlist:
  if i>=0 or i<=100:
    new_run_l.append(i)


# Now let's create a new list which will be having the numbers of wickets taken by each player of each match
new_wickets_l = []
wickets_column = df["wickets"]
wicketslist = list(wickets_column)
for i in wicketslist:
  if i>=0 or i<=10:
    new_wickets_l.append(i)


# Now let's create a new list which will be having the Economy of each player of each match
new_econ_l = []
econ_column = df["Econ"]
econlist = list(econ_column)
for i in econlist:
  if i>=0 or i<=100:
    new_econ_l.append(i)


# Now let's create a new list which will be having the number of balls missied by each player of each match
new_zero_l = []
zero_column = df["zero"]
zerolist = list(zero_column)
for i in zerolist:
  if i>=0 or i<=100:
    new_zero_l.append(i)


# Now let's create a new list which will be having the numbers of fours hit by each player of each match
new_four_l = []
four_column = df["four"]
fourlist = list(four_column)
for i in fourlist:
  if i>=0 or i<=100:
    new_four_l.append(i)


# Now let's create a new list which will be having the numbers of six hit by each player of each match
new_six_l = []
six_column = df["six"]
sixlist = list(six_column)
for i in sixlist:
  if i>=0 or i<=100:
    new_six_l.append(i)


# Now let's create a new list which will be having the numbers of wide given by each player of each match
new_wide_l = []
wide_column = df["wide"]
widelist = list(wide_column)
for i in widelist:
  if i>=0 or i<=20:
    new_wide_l.append(i)


# Now let's create a new list which will be having the numbers of noball given by each player of each match
new_nb_l = []
nb_column = df["six"]
nblist = list(nb_column)
for i in nblist:
  if i>=0 or i<=10:
    new_nb_l.append(i)


# Now let's create a new list which will be having the 11 multiples of each match name
match_column_list = df["match"]
match_column_list = list(match_column_list)
unique_match_l = []
new_match_l = []
na = 0
for i in match_column_list:
  if na in nl:
    new_match_l.append(i)
  na = na + 1


dict = { 'match' : new_match_l , 'name' : new_name_l , 'overs' : new_over_l , 'runs' : new_run_l , 'wickets' : new_wickets_l , 'Econ' : new_econ_l , 'four' : new_four_l , 'six' : new_six_l , 'wide' : new_wide_l , 'noball' : new_nb_l}
dff = pd.DataFrame(dict)
# Here you can replace filename by your file name in the working directory or paste the path where you want to modify it
#dff.to_csv("filename.csv")