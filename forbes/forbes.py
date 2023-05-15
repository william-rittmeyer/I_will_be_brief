import openai
import requests
import time
import sys
from urllib.parse import urlparse
from collections import defaultdict
from datetime import datetime
from bs4 import BeautifulSoup
import random

url = "https://www.forbes.com/"

def main(subcategory):
    # Send a GET request to the URL
    response = requests.get(url + subcategory)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the anchor tags (links) in the parsed HTML
    links = soup.find_all("a")

    # Extract the href attribute from each anchor tag and print them
    link_set = set()

    for link in links:
        href = link.get("href")
        if href and "/2023/" in href:
            link_set.add(href)
    
    link_list = list(link_set)


    def group_links_by_date(link_list):
        def get_date_from_link(link):
            path = urlparse(link).path
            date_string = path.split("/")[3:6]
            if date_string[1] == '05':  # Only include links from May
                return "/".join(date_string)  # return date as string
            else:
                return None

        links_by_date = defaultdict(list)
        for link in link_list:
            date = get_date_from_link(link)
            if date is not None:  # Only include links with valid dates
                links_by_date[date].append(link)

        return links_by_date

    links_by_date = group_links_by_date(link_list)

    # Sort the dates in descending order
    sorted_dates = sorted(links_by_date.keys(), key=lambda date: datetime.strptime(date, '%Y/%m/%d'), reverse=True)

    for date in sorted_dates:
        print(f"Date: {date}")
        print('\n')
        for link in links_by_date[date]:
            print(f"\t{link}")
        print('\n')
        print('\n------------------------------------------------------------------------------------------')

    #print(link_list)
    #print(len(link_list))
    # Set the OpenAI model to use
    model = "text-davinci-002"

    print('\n*****************************************************************************************')
    print('\n*****************************************************************************************')

    # Generate a summary sentence for each article using the GPT-3.5 model
    #prompt = "Please read the following articles and give me a sentence summary for each:\n"
    #for link in link_list:
    #    prompt += f"{link}\n"
    #response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)
    #summaries = response.choices[0].text.strip().split('\n')
    #for summary in summaries:
    #    print(summary)
    
    print('Summaries for all articles go here')

    #time.sleep(5)
    print('\n*****************************************************************************************')
    print('\n*****************************************************************************************')

    # Randomly select an article from the link list and provide a TV news host-like presentation
    #selected_link = random.choice(link_list)
    #prompt = f"Please read the following article and give me a 4 paragraph summary, and present it like TV news show. Leave out any introduction to the viewer: {selected_link}\n"
    #response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=3000)
    #summary = response.choices[0].text.strip()
    #print(f"{summary}")
    print('Summary for selected article goes here')
    print('\n*****************************************************************************************')
    print('\n*****************************************************************************************')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a subcategory as a command-line argument.")
    else:
        subcategory = sys.argv[1]
        main(subcategory)
