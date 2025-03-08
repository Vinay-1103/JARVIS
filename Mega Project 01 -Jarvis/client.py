from google import genai

client = genai.Client(api_key="AIzaSyAt0LgM3prsEo5wbb3_TykRJ38bP2XSXZo")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)