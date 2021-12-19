from .binance_api import BinanceCall


class BinanceHandler:
    def __init__(self):
        self.binance_api = BinanceCall()

    @staticmethod
    def quote_cleaner(quotes: list, all_tickers: list) -> list:
        result_tickers = list()
        # Iterate through all pairs and define pairs, that quote value is in quotes
        for ticker in all_tickers:
            for quote in quotes:
                # Amount of symbols to compare quote in ticker
                quote_len = len(quote)
                if quote in ticker[-quote_len:]:
                    result_tickers.append(ticker)
        return result_tickers

    @staticmethod
    def add_exact_pairs(exact_pairs: list, all_tickers: list) -> list:
        for cur_pair in exact_pairs:
            if cur_pair not in all_tickers:
                all_tickers.append(cur_pair)
        return all_tickers

    def define_pairs(self, quotes: list, exact_pairs: list) -> list:
        '''
        :param quotes: List of quotes in tickers that needs to be used
        :param exact_pairs:  If quotes is empty, only exact_pairs will be added
        :param empty quotes, exact_pairs: If they are empty, whole list will return
        :return: List of tickers, that user selected by config
        '''

        all_tickers = [ticker['symbol'] for ticker in self.binance_api.tickerPrice()]

        # Applying the rules from user's config
        if quotes:
            # Select only pairs with exact quotes
            all_tickers = self.quote_cleaner(quotes=quotes, all_tickers=all_tickers)
            if exact_pairs:
                # Add if if user set exact_pairs
                all_tickers = self.add_exact_pairs(exact_pairs=exact_pairs, all_tickers=all_tickers)
        else:
            if exact_pairs:
                # User chose only exact pairs
                return exact_pairs
        return all_tickers











