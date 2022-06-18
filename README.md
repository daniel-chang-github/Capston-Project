# Project Title

Stock dashboard

## Description

The goal of this project is to stay on top of the financial market and make better purchasing/selling decisions in the stock market and be alerted of any significant changes/updates in the market.

## Getting Started

### Dependencies

Please reference the requirement.txt

### Installing


### Executing program

Running the scheduler.py will run the following python scripts.

     -update_gov_official_trans.py : Everyday at 10:00
     -update_stock_price.py : Everyday at 22:00
     -update_tweets.py : Every 10 minutes


## Project Structure

There are 4 main parts to this project.

    - Downloding the data.
        - get_*.py files
    - Formatting the downloaded data and uploading the data to DB.
        - data_load*.py files
    - Script that runs downloading and uploading the data.
        - update-*.py files
    - Scheduler that runs doanloding and uploading at set times.
        - scheduler.py

## Authors

Contributors names and contact info

Daniel

## Version History

* 0.1
    * Initial Draft

## License


## Acknowledgments

Inspiration, code snippets, etc.


## Choices you had to make about any cleaning/transformation of the data you perform in your prototype



## Choices you made about the automation of your data pipeline that impact its performance or reliability

- 
