#import whisper
#import json
#model=whisper.load_model("large-v2")
#result = model.transcribe(audio="audios/1_Installing VS #Code & How Websites Work.mp3",
#language="hi",
#task="translate",
#word_timestamps=False)
#chunks=[]
#for segment in result["segments"]:
   # chunks.append({"start":segment["start"],"end":segment["end"],"text":segment["text"]})
#print(chunks)    

#print(result)

#with open("output.json","w")# as f:
    #json.dump(result,f,indent=4)
import os   
audios=os.listdir("audios")
for audio in audios:
    print(audio)
                        
                    