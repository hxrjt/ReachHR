 # try:
    #     response=openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role":"user","content":prompt}],
    #         temperature=0.7,
    #         max_tokens=400
    #     )
    #     return response["choices"][0]["message"]["content"].strip()
    
    # except Exception as e:
    #     return f"❌ Error generating message: {str(e)}"