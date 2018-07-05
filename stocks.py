stock_dict = {
    "GE": "Galactic Empire",
    "RA": "Rebel Alliance",
    "TF": "Trade Federation"
}

purchases = [
    ("GE", 50, '10-sep-2001', 24),
    ("TF", 200, '10-jan-2002', 5),
    ("RA", 20, '14-jun-2004', 50),
    ("GE", 50, '15-dec-2004', 10)
]


def calculate_price(filter=None):
    total_price = 0
    for purchase in purchases:
        for ticker, company in stock_dict.items():
            if purchase[0] == ticker and (filter == None or filter == ticker):
                print(f"{company} stock bought for {purchase[1] * purchase[3]}")
    
calculate_price()
