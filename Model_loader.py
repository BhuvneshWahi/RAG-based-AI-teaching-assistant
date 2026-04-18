import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import joblib 
import requests
import numpy as np
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embed(text_list):
    embeddings = embed_model.encode(
        text_list,
        convert_to_numpy=True,
        show_progress_bar=False
    )
    return embeddings

def inference(prompt):
    r2 = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream":False
    })
    response=r2.json()
    return response["response"]

df=joblib.load("embeddings_full@new.joblib")

incoming_query= input("What do you want to know?")
query_embeddings= create_embed([incoming_query])[0]
similarities= cosine_similarity(np.vstack(df["embeddings"]),[query_embeddings]).flatten()
#print(similarities)
#print(similarities.argsort())
top_indx= (similarities.argsort())[-6:][::-1]
print(top_indx)
new_df=df.iloc[top_indx]      
#print(new_df[["number","title","text"]]) 

prompt=f""" I am teaching Sigma Web development course here. Here are the video with the subtitles chunks containg the video number,video title,start time in seconds and end time in seconds along with the text that is taught at that time:
{new_df[["number","title","start","end","text"]].to_json(orient="records")}
------------------------------------------------------------------------------------------------------------------------------------------
incoming query {incoming_query} 
User asked this question realted to video chunks, you have to answer it in a human way (don't mention the above format it's just for you) where how much content is taught in which video(in which video and at what timestamp) and guide the user to that particular video. If user asks unrelated questions. tell him that you can only answer questions related to this course

"""
with open("prompt.txt","w") as f:
    f.write(prompt)
    
#for index,item in new_df.iterrows():
    # print(index,item["number"],item["title"],item["start"],item["end"],item["text"])


response = inference(prompt)
print(response)
with open("response.txt","w") as f:
    f.write(response)