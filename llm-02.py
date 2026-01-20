import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    model="llama-3.1-8b-instant",
    instructions="Responda de forma simples em apenas 1 parágrafo curto.",
    input="O que é machine learning?",
    
    ## Input com uso de roles:
    # input= [
    #     {
    #         "role": "system",
    #         "content": "Atue como um especialista em machine learning."
    #     },
    #     {
    #         "role": "user",
    #         "content": "De forma simples, o que é machine learning?"
    #     }
    # ]
)

print(response.output_text)
