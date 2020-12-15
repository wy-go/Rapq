from rapq.config import Config

def se_search(query):
    config = Config()
    if not config.was_initialized:
        config.initialize_application_config()
    es = config.es

    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "detail", "intro"],
                "type": "cross_fields"
                #       "analyzer": "ik_max_word"  # set ik analyzer for index first
            }
        },
        "rescore": {
            "window_size": 30,
            "query": {
                "rescore_query": {
                    "match_phrase": {
                        "content": {
                            "query": query,
                            "slop": 50
                        }
                    }
                }
            }
        }
    }

    results = es.search(index="HUAWEI-AppGallery*", body=body, size=30)

    # total = results['hits']['total']
    res_dict = []
    for hit in results['hits']['hits']:
        print(hit)
        res_dict.append((hit['_score'],hit['_source']))
    return res_dict

