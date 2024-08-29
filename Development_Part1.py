import os
import json
from groq import Groq
import time
file1=open('input.txt', 'r')
file2=open('output.json', 'w')
l=[]
while True:
    t=file1.readline()
    if t is '':
        break
    timesent = int(time.time())

    client = Groq(
        api_key=("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"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": t,
            }
        ],
        model="llama3-8b-8192",


    )
    j = chat_completion.choices[0].message.content
    timerec = int(time.time())
    l.append({'prompt':t[:-1:], 'message':j,'TImesent': timesent, 'TimeRecvd': timerec,'source':"llama3-8b-8192"})
json.dump(l,file2, indent=4)
file1.close()
file2.close()





