"""
Basic example of a Trading bot with a strategy pattern.
"""
from curses import window
import statistics
from dataclasses import dataclass
from typing import List, Callable

from functools import partial
from exchange import Exchange


TradingStrategyFunction = Callable[[List[int]], bool]


def should_buy_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[window_size:]
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[window_size:]
    return prices[-1] > statistics.mean(list_window)


def should_buy_minmax(prices: list[int], min_price: int) -> bool:
    return prices[-1] < min_price


def should_sell_minmax(prices: list[int], max_price: int) -> bool:
    return prices[-1] > max_price


@dataclass
class TradingBot:
    """Trading bot that connects to a crypto exchange and performs trades."""

    exchange: Exchange
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")


def main() -> None:
    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()

    # create the trading bot and run the bot once
    buy_strategy = partial(should_buy_avg, window_size=4)
    sell_strategy = partial(should_sell_minmax, max_price=35_000_00)

    bot = TradingBot(exchange, buy_strategy, sell_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()
