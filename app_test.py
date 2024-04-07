import streamlit as st
# import openai
from openai import OpenAI


openai_api_key = st.secrets["api_key"]
st.title("ChatGPT Plus DALL-E")

with st.form("form"): 
    user_input = st.text_input("Prompt")
    img_size = st.selectbox("Size", ["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:        
    st.write("Answer:" +user_input)
    gpt_prompt = [{
        "role": "system"
        # , "content": "Imagine the detail appearance of the input. Response it shortly."
        , "content": "Imagine the detail appearance of the input. Response it shortly around 20 words."
    }]
    
    gpt_prompt.append({
        "role": "user"
        , "content": user_input
    })
    
    
    #openai.ChatCompletion.create(
    #    model = "gpt-3.5-turbo"
    #    , messages=gpt_prompt
    #)
    
    client = OpenAI(api_key=openai_api_key)
    
    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = client.chat.completions.create(
            model = "gpt-3.5-turbo"
            , messages=gpt_prompt        
        )
    
    
    # gpt_response["choices"][0]["message"]["content"]
    # print(gpt_response)
    #print(gpt_response["choices"].message)
    
    dalle_prompt = gpt_response.choices[0].message.content
    print("dalle_prompt=" + dalle_prompt )
    
    st.write(dalle_prompt)
    
    with st.spinner("Waiting for DALL-E..."):
        #dalle_respinse = openai.Image.create(
        #    prompt = dalle_prompt
        #    , size="1024x1024"
        #)
        dalle_respinse = client.images.generate(
            prompt = dalle_prompt
            , size=img_size
        )
    
    image_url = dalle_respinse.data[0].url
    st.image(image_url)
    # print("dalle_respinse=" + dalle_respinse)
    
    