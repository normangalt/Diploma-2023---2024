def extract_headlines(articles_list_str):
    articles_list_str = articles_list_str.replace("\"\"", '\"')
    aritcles_list = []
    found_mark = False
    mark = ''
    headline = ""
    for letter_index in range(1, len(articles_list_str) - 1):
        letter = articles_list_str[letter_index]
        # print(letter, found_mark)
        if not found_mark:
            if letter == "'" or letter == "\"":
                mark = letter
                found_mark = True
                continue

        if found_mark:    
            # print(headline, mark, letter)
            if letter == mark:
                found_mark = False
                headline = headline.replace("\n", "")
                headline = headline.replace("\\", "")
                aritcles_list.append(headline)
                headline = ""
                found_mark = False
            else:
                headline += letter
    if headline:
        headline = headline.replace("\n", "")
        headline = headline.replace("\\", "")
        aritcles_list.append(headline)

    return aritcles_list

# headlines = extract_headlines("""[""Bitcoin Price: Traders Angry Over Mt Gox Trustee's Bitcoin Sales"", 'Will Ripple be Bigger than Bitcoin? Experts Say Yes', 'How Much Does It Cost to Mine Bitcoin Around the World?', 'This rap song about bitcoin cash makes no sense, and it is ...', 'Bitcoin and cryptocurrency millionaires on Instagram: PHOTOS', 'New Jersey Demands ICO Endorsed By Steven Seagal To Stop Selling To \nResidents', 'Bithumb to Bring Bitcoin ATMs and Kiosks to South Korea', 'Neurogress Begins Shaping the World by Sharing its Source Code | \nBitcoinist.com', 'Nissi Online Casino Adds Live Blackjack | Bitcoinist.com', 'One-Third of Cryptocurrencies Are Unspendable']""")
# for h in headlines:
#     print(h, "|")
