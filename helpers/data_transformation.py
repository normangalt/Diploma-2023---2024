import pandas as pd
from headline_retrieval import extract_headlines

data = pd.read_csv("BTC.csv")
new_data = pd.DataFrame(columns = ["Date", "Headline"])

new_index = 0
for index in data.index:
    articles = data["articles"].iloc[index]
    date = data["begins_at"].iloc[index]
    headlines = extract_headlines(articles)
    for headline in headlines:
        new_data.loc[new_index] = [date, headline]
        new_index += 1

new_data.to_csv("headlines.csv")

new_data_2 = new_data.merge(data, left_on='Date', right_on='begins_at')
new_data_2.to_csv("headlines_2.csv")

new_data_3 = new_data.merge(data[["begins_at", "open_price", "close_price", "high_price", "low_price", "symbol"]], left_on='Date', right_on='begins_at')
new_data_3.to_csv("headlines_3.csv")

new_data_4 = new_data.merge(data[["begins_at", "open_price", "close_price"]], left_on='Date', right_on='begins_at')
new_data_4.to_csv("headlines_3.csv")

print(new_data_2)
print(new_data_2.head())
print(new_data_2.tail())

print(new_data_3)
print(new_data_3.head())
print(new_data_3.tail())
