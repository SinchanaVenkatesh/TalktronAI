import openai

openai.api_key = "###"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Give me 3 ideas for apps I could build with OpenAI APIs.",
    max_tokens=100
)

print(response.choices[0].text.strip())
