"""
Basic example of a Trading bot with a strategy pattern.
"""
import statistics
from dataclasses import dataclass
from typing import List, Callable

from exchange import Exchange


TradingStrategyFunction = Callable[[List[int]], bool]


def should_buy_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_buy_avg(prices: list[int]) -> bool:
        list_window = prices[window_size:]
        return prices[-1] < statistics.mean(list_window)

    return should_buy_avg


def should_sell_avg(prices: list[int]) -> bool:
    list_window = prices[-3:]
    return prices[-1] > statistics.mean(list_window)


def should_buy_minmax(prices: list[int]) -> bool:
    # buy if it's below $32,000
    return prices[-1] < 32_000_00


def should_sell_minmax_closure(max_price: int) -> TradingStrategyFunction:
    def should_sell_minmax(prices: list[int]) -> bool:
        return prices[-1] > max_price

    return should_sell_minmax


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
    bot = TradingBot(
        exchange, should_buy_avg_closure(4), should_sell_minmax_closure(35_000_00)
    )
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()
