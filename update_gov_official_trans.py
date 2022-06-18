import get_goverment_official_data
import data_load_gov_official

#Loop through the twitter user ids and download and import tweets.
get_goverment_official_data.get_gov_official_data()

#Upload tweets.
data_load_gov_official.import_gov_official()