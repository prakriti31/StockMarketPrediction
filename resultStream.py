from searchtweets import ResultStream

rs = ResultStream(rule_payload=rule,
                  max_results=1000,
                  **premium_search_args)
print(rs)
