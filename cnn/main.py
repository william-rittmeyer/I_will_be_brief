import openai
import requests
import time
from bs4 import BeautifulSoup
import random

# Authenticate with OpenAI API key
openai.api_key = "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"

url = 'https://www.cnn.com/business'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print('\n------------------------------------------------------------------------------------------')

# Find all the links to the stories on the page that have "2023" in the link and do not have "www.cnn.com/videos/" in the link
link_list = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and '/business/' in href and '/video/' not in href and '/gallery/' not in href and '/interactive/' not in href and '2023' in href and '/videos/' not in href:
        link_list.append(f"https://www.cnn.com{href}")

# Set the OpenAI model to use
model = "text-davinci-002"

# Generate a summary sentence for each article using the GPT-3.5 model
prompt = "Please read the following articles and give me a sentence summary for each:\n"
for link in link_list:
    prompt += f"{link}\n"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)
summaries = response.choices[0].text.strip().split('\n')
for summary in summaries:
    print(summary)

time.sleep(5)
print('\n------------------------------------------------------------------------------------------')
# Randomly select an article from the link list and provide a TV news host-like presentation
selected_link = random.choice(link_list)
prompt = f"Please read the following article and give me a 4 paragraph summary, and present it like TV news show. Leave out any introduction to the viewer: {selected_link}\n"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=3000)
summary = response.choices[0].text.strip()
print(f"{summary}")
print('\n------------------------------------------------------------------------------------------')
