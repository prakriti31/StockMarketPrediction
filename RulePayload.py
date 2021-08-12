from searchtweets import gen_rule_payload
from searchtweets import load_credentials

premium_search_args = load_credentials("twitter_keys_fullarchive.yaml",
                                       yaml_key="search_tweets_api",
                                       env_overwrite=False)
print(premium_search_args)
query = "AAPL"
rule = gen_rule_payload(query, results_per_call=100, from_date="2021-05-01", to_date="2021-05-20")
from searchtweets import ResultStream

rs = ResultStream(rule_payload=rule,
                  max_results=25000,
                  **premium_search_args)
print(rs)
import json
with open('tweets1.json', 'a', encoding='utf-8') as f:
    for tweet in rs.stream():
        json.dump(tweet, f)
        f.write('\n')
print('done')
