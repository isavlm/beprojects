"""Hash table examples. Challenge 2 - Class 003."""
#Step 1 - Create an empty hash Table (aka dict)

dog_type = {} 

#Step 2 - Define a function. 

def dogs_hash(key):
    return len(key) % 10 


#Step 3 - Adding dogs to the has table 

def add_dogs(hash_table, key, location):
    #We always need to use the hash function (step2) to get the value for the key
    hash_value = dogs_hash(key)

    if hash_value in hash_table:
        #We need to add a way to deal with collision. 
        hash_table[hash_value].append((key,location))
    else:
        hash_table[hash_value] = [(key, location)]

#Adding dogs! 
add_dogs( dog_type, 'Golden Retriever', 'Big dogs',)
add_dogs( dog_type,'Pug', 'Small dogs')
add_dogs( dog_type, 'Beagle', 'Medium dogs')

#Step 4 - Retrieve the location of a dog

def find_dog_location(hash_table, key):
    hash_value = dogs_hash(key)
    
    if hash_value in hash_table:
        for dog_key, location in hash_table[hash_value]:
            if dog_key == key:
                return location
    return None #if dog not found

#Step 5 - Testing the code! 

dog_to_find = 'Pug'
location_found = find_dog_location(dog_type, dog_to_find)

if location_found:
    print(f"The location of {dog_to_find} is: {dog_type}")
else:
    print(f"Sorry, {dog_to_find} not found.")
