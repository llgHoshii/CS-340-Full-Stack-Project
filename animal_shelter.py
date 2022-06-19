from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
     #CRUD operations for Animal collection in MongoDB

    def __init__(self,username,password) -> None:
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient("mongodb://%s:%s@localhost:45328" % (username, password))
        # where xxxxx is your port number
        self.database = self.client["AAC"]

# Complete this create method to implement the C in CRUD.
    def create(self, data) -> True:
        
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary format
            return True  #returns true if data inserted
            
        else:
            raise exception("Nothing to save, because data parameter is empty")
            #else returns exception

# Create method to implement the R in CRUD. 
    def read(self, search) -> dict:
        
        if search is not None:
            searchResult=self.database.animals.find(search, {"_id":False}) #searching in database
            return searchResult   #if data is not empty and in database it will return it
        
        #if search is None:  #delete later maybe?
         #   cursor = self.database.animals.find({})
          #  for document in cursor:
           #       print(document)
            
           
        else:
            raise exception("Nothing to read, because data parameter is empty")#if data not in database, return this exception
            return exception

# Create method to implement the U in CRUD
    def update(self,oldvals,newvals) -> dict:
        
        if oldvals and newvals is not None:  #only preforms the update if they are not none
            updateResult = self.database.animals.update(oldvals, newvals) #updates the old values with the new ones
            return updateResult  #returns in JSON format
        else:
            raise exception ("Nothing to update, becasue parameter is empty") #if update values not provided throw exception
            return exception
        
# Create method to implement the D in CRUD
    def delete(self,deletequery) -> dict:
        
        if deletequery is not None:   #only deletes if the parameter is not empty
            self.database.animals.delete_one(deletequery)  #deletes the entry based on parameter input
            return self.database.animals.find_one(deletequery)  #returns in JSON format
        else:
            raise exception ("Nothing to delete, becasue parameter is empty") #if delete values not provided throw exception
            return exception


        
#create __repr__ method to display proper output
    def __repr__(self) -> dict:
        return str(self.searchResult)
    
