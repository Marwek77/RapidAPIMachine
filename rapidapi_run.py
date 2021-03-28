from rapidapi_machine import RapidApiMachine

database = {
    "Dino Ipsum": ["GET",
                   "https://alexnormand-dino-ipsum.p.rapidapi.com/",
                   {"format": "json", "words": "5", "paragraphs": "3"}
                   ],
    "Stock Market Data": ["GET",
                          "https://stock-market-data.p.rapidapi.com/stock/quote",
                          {"ticker_symbol": "HOG"}
                          ]
}

result = RapidApiMachine(*database["Stock Market Data"])
result.get_api_machine_data()
