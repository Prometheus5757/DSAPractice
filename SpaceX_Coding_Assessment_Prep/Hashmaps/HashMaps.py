'''
Suppose we have a list of tuples and we want to group by unique ID. This is a proper use case of a hash map.
We are going to implement this by using initializing an empty dictionary, which in python, is internally implemented as a hash table. 
'''

#Given the below list

dealership = [("RAV4", 2022), ("Camry", 2023), ("Venza", 2021), ("Highlander", 2025), ("Prius", 2022), ("RAV4", 2021), ("Camry", 2022), ("Venza", 2026), ("Highlander", 2019), ("Prius", 2021)]

carGroups = {} #initializing empty dictionary for unique car IDs that has values of all available years.

for model, year in dealership:
    carGroups.setdefault(model, []).append(year)
    # The above line first checks the carGroups dictionary to see if a model exists. If it doesn't, it will first create a key of the model in the 

print (carGroups)
# This results in {'RAV4': [2022, 2021], 'Camry': [2023, 2022], 'Venza': [2021, 2026], 'Highlander': [2025, 2019], 'Prius': [2022, 2021]}. Notice how each model is a unique key that does not appear twice. Instead, all models of the cars are added to the list that we added as the second argument in the setdefault() method. 