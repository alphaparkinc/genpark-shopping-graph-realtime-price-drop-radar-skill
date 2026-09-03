from client import ShoppingGraphRealtimePriceDropRadarClient

def main():
    client = ShoppingGraphRealtimePriceDropRadarClient()
    res = client.track_product_price_graph('0123456789012', 'Sony WH-1000XM5', 320.00)
    print('Shopping Graph Price Radar: ' + res['radar_tracking_id'] + ' (' + res['deal_rating_score'] + ')')
    print('Lowest Price: $' + str(res['current_lowest_merchant_price_usd']) + ' at ' + res['lowest_merchant_name'] + ' (-$' + str(res['price_drop_amount_usd']) + ')')
    print('Graph URL: ' + res['price_history_graph_url'])

if __name__ == '__main__':
    main()
