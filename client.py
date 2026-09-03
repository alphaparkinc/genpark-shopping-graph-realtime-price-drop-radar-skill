class ShoppingGraphRealtimePriceDropRadarClient:
    def track_product_price_graph(self, global_gtin_barcode='0194252000000', target_product_name='Apple MacBook Pro M4 16-inch', target_price_threshold_usd=2199.00):
        return {
            'radar_tracking_id': 'shg_rdr_9918',
            'product_name': target_product_name,
            'current_lowest_merchant_price_usd': 2099.00,
            'lowest_merchant_name': 'BestBuy Direct',
            'historic_30d_avg_price_usd': 2399.00,
            'price_drop_amount_usd': 300.00,
            'deal_rating_score': 'EXCEPTIONAL_ALL_TIME_LOW',
            'price_history_graph_url': 'https://graph.shopping.genpark.ai/prices/9918.json'
        }
