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
         #       "analyzer": "ik_max_word"  # didnot set analyzer for index
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

