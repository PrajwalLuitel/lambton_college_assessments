from typing import Any
import tmdbsimple as tmdb
import yfinance as yf
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
from textblob import TextBlob

from my_secrets import TMDB_API_KEY

# The API key to fetch data from the TMDB
tmdb.API_KEY = TMDB_API_KEY


# Class with all the methods regarding the movie data and TMDB api
class MovieData:
    def __call__(self, company_id, num_movies=10) -> Any:
        company = tmdb.Companies(company_id)
        movies = company.movies()['results'][:num_movies]
        movie_details = []
        for movie in movies:
            movie_info = tmdb.Movies(movie['id']).info()
            reviews = tmdb.Movies(movie['id']).reviews()
            review_texts = [review['content'] for review in reviews['results']]
            movie_details.append({
                'title': movie_info['title'],
                'release_date': movie_info['release_date'],
                'description': movie_info['overview'],
                'reviews': ' '.join(review_texts)  # Combine all reviews into a single string
            })
        return pd.DataFrame(movie_details)

# Class with all the methods with relation to the stock market data
class StockData:
    def __call__(self,movie_data, ticker, days_before=15, days_after=15) -> Any:
        stock_data_list = []
        for release_date in movie_data['release_date']:
            release_date_dt = datetime.datetime.strptime(release_date, '%Y-%m-%d')
            start_date = (release_date_dt - datetime.timedelta(days=days_before)).strftime('%Y-%m-%d')
            end_date = (release_date_dt + datetime.timedelta(days=days_after)).strftime('%Y-%m-%d')
            stock_data = self.get_stock_data(ticker, start_date, end_date)
            stock_data['release_date'] = release_date_dt
            stock_data_list.append(stock_data)
        return stock_data_list

    def get_stock_data(self, ticker, start_date, end_date):
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data

# Class method for performing sentiment analysis
class SentimentAnalysis:
    def reviews_sentiment(self, movie_data_sentiment:pd.DataFrame) -> Any:
        return movie_data_sentiment['reviews'].apply(self.analyze_sentiment)

    def description_sentiment(self, movie_data_sentiment:pd.DataFrame) -> Any:
        return movie_data_sentiment['description'].apply(self.analyze_sentiment)

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity


# Class for visualization of the findings
class Visualization:
    def stock_plots(self,movie_data, stock_data_list) -> None:
        for i, release_date in enumerate(movie_data['release_date']):
            stock_data = stock_data_list[i]
            release_date_dt = datetime.datetime.strptime(release_date, '%Y-%m-%d')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines+markers', name='Closing Price'))
            
            # Add vertical line for the release date
            fig.add_vline(x=release_date_dt, line=dict(color='red', dash='dash'))
            
            # Adding annotation for the release date
            fig.add_annotation(x=release_date_dt, y=stock_data['Close'].max(), text='Release Date', showarrow=True, arrowhead=2)

            fig.update_layout(
                title=f"Stock Prices Around Release Date of '{movie_data['title'][i]}'",
                xaxis_title='Date',
                yaxis_title='Stock Closing Price',
                template='plotly_dark'
            )
            fig.show()

    def sentiment_plot(self, movie_data, sentiment_on) -> None:
        fig = px.bar(movie_data[['title',f'sentiment_{sentiment_on}']], x='title', y=f'sentiment_{sentiment_on}', title=f'Sentiment for Each Movie Title on {sentiment_on}', labels={'sentiment': 'Sentiment Score', 'title': 'Movie Title'})
        fig.update_layout(xaxis_title='Movie Title', yaxis_title='Sentiment Score', template='plotly_dark')
        fig.show()



if __name__ == '__main__':
    # Firstly, fetching the movie data for 10 movies of Walt Disney Pictures
    movie_data = MovieData()(company_id=2)

    # Getting the stock prices for the time around the movie release (15 days before and after the release)
    stock_data_list = StockData()(movie_data, ticker='DIS') # DIS stands for Disney in the stock market

    # Analyzing the sentiment on movie reviews
    movie_data['sentiment_reviews'] = SentimentAnalysis().reviews_sentiment(movie_data)


    # Analyzing the sentiment on movie description
    movie_data['sentiment_description'] = SentimentAnalysis().description_sentiment(movie_data)

    # Visualization
    # Visualizing the sentiments
    visualizer = Visualization()
    # Sentiments for reviews
    visualizer.sentiment_plot(movie_data, "reviews")

    # sentiments for description
    visualizer.sentiment_plot(movie_data,"description")

    # Visualization the graphs of stock prices and release dates for each movie
    visualizer.stock_plots(movie_data, stock_data_list)
