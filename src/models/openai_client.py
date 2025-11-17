from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client= OpenAI(api_key=self.api_key)

    def generate_response(self, prompt, model="gpt-3.5-turbo", temperature=0.7):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.choices[0].message.content

    def generate_code(self, prompt):
        return self.generate_response(prompt, model="gpt-3.5-turbo")

    def generate_essay(self, prompt):
        return self.generate_response(prompt, model="gpt-3.5-turbo")
