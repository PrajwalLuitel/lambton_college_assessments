import tmdbsimple as tmdb
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob



from my_secrets import TMDB_API_KEY

# Set up the TMDb API key
tmdb.API_KEY = TMDB_API_KEY

# Function to get movie details from TMDb
def get_movie_details(company_id, num_movies=10):
    company = tmdb.Companies(company_id)
    movies = company.movies()['results'][:num_movies]
    movie_details = []
    for movie in movies:
        movie_info = tmdb.Movies(movie['id']).info()
        movie_details.append({
            'title': movie_info['title'],
            'release_date': movie_info['release_date'],
            'description': movie_info['overview']
        })
    return pd.DataFrame(movie_details)

# Example: Collecting movie details for Walt Disney Pictures (company ID: 2)
movie_data = get_movie_details(company_id=2)


print(movie_data)


# Function to get stock data from Yahoo Finance
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Example: Collecting stock data for Disney (ticker: DIS)
# Collect stock data for 5 days before and 5 days after each movie release date
def get_stock_data_around_release_dates(movie_data, ticker, days_before=15, days_after=15):
    stock_data_list = []
    for release_date in movie_data['release_date']:
        release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        start_date = (release_date - datetime.timedelta(days=days_before)).strftime('%Y-%m-%d')
        end_date = (release_date + datetime.timedelta(days=days_after)).strftime('%Y-%m-%d')
        stock_data = get_stock_data(ticker, start_date, end_date)
        stock_data['release_date'] = release_date.strftime('%Y-%m-%d')
        stock_data_list.append(stock_data)
    return pd.concat(stock_data_list)

# Example: Getting stock data around movie release dates
stock_data = get_stock_data_around_release_dates(movie_data, ticker='DIS')

# Merge movie data and stock data
def merge_movie_and_stock_data(movie_data, stock_data):
    movie_data['release_date'] = pd.to_datetime(movie_data['release_date'])
    stock_data['release_date'] = pd.to_datetime(stock_data['release_date'])
    merged_data = pd.merge_asof(stock_data.sort_index(), movie_data, left_on='Date', right_on='release_date', direction='backward')
    return merged_data

# Example: Merging data
merged_data = merge_movie_and_stock_data(movie_data, stock_data)

# Sentiment Analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Example: Sentiment analysis on movie descriptions
movie_data['sentiment'] = movie_data['description'].apply(analyze_sentiment)

# Data Visualization
def plot_stock_prices_around_release(merged_data):
    plt.figure(figsize=(14, 7))
    for release_date in merged_data['release_date'].unique():
        subset = merged_data[merged_data['release_date'] == release_date]
        plt.plot(subset.index, subset['Close'], marker='o', label=release_date)
    plt.axvline(x=0, color='red', linestyle='--', label='Release Date')
    plt.xlabel('Days Around Release')
    plt.ylabel('Stock Closing Price')
    plt.title('Stock Prices Around Movie Release Dates')
    plt.legend()
    plt.show()

# Example: Plotting stock prices
plot_stock_prices_around_release(merged_data)
