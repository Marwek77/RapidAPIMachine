from rapidapi_machine import RapidApiMachine

database = {
    "Dino Ipsum":
        ["GET",
         "https://alexnormand-dino-ipsum.p.rapidapi.com/",
         {"format": "json", "words": "5", "paragraphs": "3"}
         ],
    "Stock Market Data":
        ["GET",
         "https://stock-market-data.p.rapidapi.com/stock/quote",
         {"ticker_symbol": "HOG"}
         ],
    "Order Tracking get":
        ["GET",
         "https://order-tracking.p.rapidapi.com/carriers",
         {}
         ],
    "Order Tracking post":
        ["POST",
         "https://order-tracking.p.rapidapi.com/trackings/realtime",
         "{\"tracking_number\": \"1Z74A08E0317341984\", \"carrier_code\": \"ups\"}"
         ],
    "Google Search get":
        ["GET",
         "https://google-search3.p.rapidapi.com/api/v1/search/q=ufo",
         {}
         ],
    "Google Search post":
        ["POST",
         "https://google-search3.p.rapidapi.com/api/v1/serp/",
         "{\r\"query\": \"q=google+search+api&num=100\",\r\"website\": \"https://rapidapi.com\"\r}",
         ]

}

result = RapidApiMachine(*database["Order Tracking post"])
result.get_api_machine_data()
