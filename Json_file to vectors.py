import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
jsons=os.listdir("jsons_use")
def create_embed(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"]
    return embedding


    

#E1 = create_embed("bhauuuu")["embeddings"]
#print(E1)
my_chunks =[]
chunk_id=0
for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content=json.load(f)
    embeddings=create_embed([c['text'] for c in content['chunks']])
    for i,chunk in enumerate(content ["chunks"]):
        chunk["chunk_id"]=chunk_id
        
        if(chunk_id)<11:
            chunk['embeddings'] =embeddings[i]
            i+=1
            my_chunks.append(chunk)
            chunk_id+=1
    break
#print(my_chunks) 
df=pd.DataFrame.from_records(my_chunks) 
joblib.dump(df,"embeddings.joblib")  
#print(df)
#print(np.vstack(df["embeddings"].values))
#print(np.vstack(df["embeddings"].values).shape)

              