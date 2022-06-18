import requests
import json
from pathlib import Path # To create necessary folders
from datetime import datetime
import log


def get_gov_official_data():
  try:
    output_file = 'gov_official_{}.json'.format(datetime.now())
    output_dir = Path('data/gov_official')
    output_dir.mkdir(parents=True, exist_ok=True)

    r= requests.get('https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json')
    with open(output_dir/output_file, 'w') as outfile:
      json.dump(r.json(), outfile)
    log.logger.info('get_gov_official data - Download successful - {}'.format(datetime.now()))

  except:
    log.logger.warning('get_gov_official data - Download FAILED - {}'.format(datetime.now()))

