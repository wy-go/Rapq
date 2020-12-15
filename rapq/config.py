from elasticsearch import Elasticsearch

class Config:
    was_initialized = False
    indexed_articles = {}
    # rapq_url = 'https://rapq.com'  # apply for url
    is_prevention_form_sleep_enabled = False
    es = Elasticsearch


    def initialize_application_config(self):
        # connect elasticsearch
        self.es = Elasticsearch(["localhost:9200"])
        self.was_initialized = True


# def prevent_rapq_from_sleeping():
#     Config.is_prevention_form_sleep_enabled = True
#     s = sched.scheduler(time.time, time.sleep)
#
#     def make_request(sc):
#         print('make request')
#         try:
#             urllib.request.urlopen(Config.rapq_url)
#         except:
#             _, ex, _ = sys.exc_info()
#             print('Failed to ping rapq: ' + Config.rapq_url + '. Reson: ' + str(ex))
#         s.enter(ping_interval, 1, make_request, (sc,))
#
#     ping_interval = 300  # 5 minutes
#     s.enter(ping_interval, 1, make_request, (s,))
#     s.run()
