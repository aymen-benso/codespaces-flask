from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import json


google_api_key = "AIzaSyAZvPEKmK2qPK6TVaP9-tqOi3GpTAFanFU"
google_cx = "e3a2db6e7281d4629"


def fetch_and_scrape(query):
  # Fetch results from Google Search API
  search_results = google_search(query)  # assuming google_search is defined as before

  if search_results:
    # Scrape the first result
      return search_results
  else:
      return {"error": "No snippet found"}


# Rewrite the query to be more effective for a Google search

def rewrite_query_with_gpt(original_query):
    client = OpenAI(
        api_key="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",
        organization='org-yui7Ie8osHV9jytpHdWaIdRv',
    )
    response = client.chat.completions.create(
        model="gpt-4",  # Assuming gpt-4-turbo is the correct model name
        max_tokens=60,  # Adjust as needed
            messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Rewrite the following query to be more effective for a bing search,\nQuery: "+original_query}
    ],

    )
    return response.choices[0].message.content

# Summerize the scraped data

def process_with_gpt(query, scraped_data,gptv):
    client = OpenAI(
        api_key="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",
        organization='org-yui7Ie8osHV9jytpHdWaIdRv',
    )

    try:
        response = client.chat.completions.create(
            model=gptv,  # Replace with the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":"search results from internet " + query + " : \n"+scraped_data}
            ],
            max_tokens=300,
              # Adjust as needed
        )
        return (response.choices[0].message.content)
    except Exception as e:
        return {"error": str(e)}

# Search the web

def google_search(query):
    headers = {"X-API-Key": "a458acae-3fb7-40c0-8e75-90c7f2940f2d<__>1OaosqETU8N2v5f4C8oXybgH"}
    params = {"query": query}
    return json.dumps(requests.get(
        f"https://api.ydc-index.io/search",
        params=params,
        headers=headers,
    ).json())


def get_answer(query,gptv):
    try:
            query = rewrite_query_with_gpt(query)
            return process_with_gpt(query,fetch_and_scrape(query),gptv)
    except Exception as e:
        return {"error": str(e)}
