import requests
import os
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAJjRVgEAAAAApJFt3ZG9EyHXx9Zq%2FH%2BsQeUEI%2FM%3DttLTxNoTTvx7bi8lKDaGD2ZskZE1jlyk79RXxgIWcZSTIRKZX5"

#search_url = "https://api.twitter.com/2/tweets/search/recent"
search_url = "https://api.twitter.com/1.1/search/tweets.json?q=$TSLA"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
#query_params = {'query': 'TSLA','max_results':'100','tweet.fields': 'id,text,created_at,entities,public_metrics'}
query_params ={}

def bearer_oauth(r):
    

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()



