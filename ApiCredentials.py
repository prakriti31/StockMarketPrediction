import yaml
config = dict(
    search_tweets_api = dict(
        account_type = 'premium',
        endpoint = 'https://api.twitter.com/1.1/tweets/search/30day/development.json',
        consumer_key = 'C1W24fGekeKmUQYFGWbLXL0AC',
        consumer_secret = 'zi8Ko1VLov6IboW0TD62M0iWbYVKjaFGSrpHa2pvpXHWjkzUJw'
    )
)
with open('twitter_keys_fullarchive.yaml', 'w') as config_file:
    yaml.dump(config, config_file, default_flow_style=False)
