import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://mulesaikrishnareddy2003:saikris2003@cluster0.bnz2azr.mongodb.net/subject_DB?retryWrites=true&w=majority")


data = pd.read_excel("major.xlsx")



db = client["subject_DB"]


collection = db["subjects"]

topics_to_search = ["git", "java", "aws"]
matching_documents = collection.find({"topic": {"$in": topics_to_search}})
matching_documents_content=[]
for document in matching_documents:
    
    for content_item in document["content"]:
        matching_documents_content.append(content_item['value'])
print(matching_documents_content)
