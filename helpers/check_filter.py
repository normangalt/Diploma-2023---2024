import pandas as pd
from langdetect import detect

def is_english(headline):
    try:
        language = detect(headline)
        return language == 'en'
    except:
        return False

def categorize_headlines(df):
    english_headlines = pd.DataFrame(columns=df.columns)
    non_english_headlines = pd.DataFrame(columns=df.columns)

    for index, row in df.iterrows():
        if is_english(row['Headline']):
            english_headlines = english_headlines._append(row)
        else:
            non_english_headlines = non_english_headlines._append(row)
    
    return english_headlines, non_english_headlines

def main():
    # Assuming you have a CSV file named 'headlines.csv' with 'headline' column
    df = pd.read_csv('headlines_3.csv', "headlines_3.csv")
    
    english_headlines, non_english_headlines = categorize_headlines(df)

    english_headlines.to_csv("english_headlines_3.csv")
    non_english_headlines.to_csv("non_english_headlines_3.csv")

    print("English Headlines:")
    print(english_headlines)
    
    print("\nNon-English Headlines:")
    print(non_english_headlines)

if __name__ == "__main__":
    main()
