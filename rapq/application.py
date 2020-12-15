import logging
import sys
import threading

from flask import Flask, request, render_template, redirect, url_for

from rapq.config import Config
from rapq.search_engine import se_search

app = Flask(__name__)

# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)

# t = threading.Thread(target=prevent_herokuapp_from_sleeping, args=())
# t.start()

# Initialize
@app.route('/')
def index():
    print('in def index():')
    config = Config()
    if not config.was_initialized:
        config.initialize_application_config()
    return render_template('index.html')


# Click app
@app.route('/apps/show')
def show_app():
    url = request.args.get('url')
    if not url:
        return redirect(url_for('index'))

    return render_template('app/index.html', article=app, url=url)


# Search app
@app.route('/search')
def search_app():
    query = request.args.get('query')
    search_results = se_search(query)
    if not search_results:
        return no_results_template(query)
    return render_template('search_results.html', search_results=search_results, query=query)

@app.route('/search/lucky')
def search_lucky():
    return redirect('https://appgallery.huawei.com/#/Featured')

# No result
def no_results_template(query):
    return render_template('simple_message.html', title='No results found',
                           message='Your search - <b>' + query + '</b> - did not match any documents.'
                                                                 '<br>Suggestions:<br><ul>'
                                                                 '<li>Make sure that all words are spelled correctly.</li>'
                                                                 '<li>Try different keywords.</li>'
                                                                 '<li>Try more general keywords.</li>'
                                                                 '<li>Try fewer keywords.</ul>')


@app.route('/reset_config')
def reset_config():
    Config.initialize_application_config()
    return render_template('simple_message.html', title='Application config updated', message='Config attributes: <br>' + str(vars(Config)))
