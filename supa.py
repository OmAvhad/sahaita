
import os
from supabase import create_client, Client
import json

url: str = "https://qwrranvmkfmxcmjilkam.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF3cnJhbnZta2ZteGNtamlsa2FtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NzI2NDI3MywiZXhwIjoyMDEyODQwMjczfQ.O2suIZCGyNwbPV7PC8EyK8jrvyrF3iTv31cdKwsVD4M"
supabase: Client = create_client(url, key)


with open('test.jpeg', 'rb') as f:
    name = f.name.split('.')[0]
    response =  supabase.storage.from_("images").upload(file=f,path=name, file_options={"content-type": "image/jpeg"})

try:
    print(response)
    response_json = response.json()
    print("Response JSON:", response_json)
    url = response_json.get('url')
    print("Upload URL:", url)
except json.JSONDecodeError:
    print("Unable to parse JSON from response.")