import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot

class MainBackend(QObject):
    def __init__(self):
        super().__init__()
        self._root = None

    def set_root(self, root):
        self._root = root

    def parse_european_number(self, s):
        s = s.strip().replace('.', '').replace(',', '.')
        return float(s)

    def format_european_number(self, value, decimal_places=2):
        format_string = f"{{:.{decimal_places}f}}"
        integer_part, decimal_part = format_string.format(value).split('.')
        integer_with_thousand_sep = ''
        for i, digit in enumerate(reversed(integer_part)):
            if i % 3 == 0 and i != 0:
                integer_with_thousand_sep = '.' + integer_with_thousand_sep
            integer_with_thousand_sep = digit + integer_with_thousand_sep
        return integer_with_thousand_sep + ',' + decimal_part

    @Slot(str, str, str, str, str)
    def calculateResults(self, local_currency_symbol, exchange_rate_str, local_price_str, thailand_price_str, investment_amount_str):
        local_currency_symbol = local_currency_symbol.strip()
        exchange_rate_str = exchange_rate_str.strip()
        local_price_str = local_price_str.strip()
        thailand_price_str = thailand_price_str.strip()
        investment_amount_str = investment_amount_str.strip()

        try:
            exchange_rate = self.parse_european_number(exchange_rate_str)
            local_price = self.parse_european_number(local_price_str)
            thailand_price_baht = self.parse_european_number(thailand_price_str)
            investment_amount = self.parse_european_number(investment_amount_str)

            if exchange_rate <= 0:
                raise ValueError("Exchange rate must be a positive number.")
            if local_price <= 0:
                raise ValueError("Gold price in your local country must be a positive number.")
            if thailand_price_baht <= 0:
                raise ValueError("Gold price in Thailand must be a positive number.")
            if investment_amount <= 0:
                raise ValueError("Investment amount must be greater than 0.")

            TROY_OUNCE_IN_GRAMS = 31.1034768
            GOLD_BAHT_WEIGHT_GRAMS = 15.244
            gold_baht_weight = GOLD_BAHT_WEIGHT_GRAMS / TROY_OUNCE_IN_GRAMS
            LOCAL_PURITY = 99.99 / 100  # Assuming local country purity
            THAILAND_PURITY = 96.5 / 100

            adjusted_local_price = local_price / LOCAL_PURITY

            thailand_price_local_currency_per_baht = thailand_price_baht / exchange_rate
            thailand_price_per_ounce_local_currency = thailand_price_local_currency_per_baht / gold_baht_weight
            adjusted_thailand_price_local_currency = thailand_price_per_ounce_local_currency / THAILAND_PURITY

            gold_amount_local = investment_amount / adjusted_local_price
            gold_amount_thailand = investment_amount / adjusted_thailand_price_local_currency

            if adjusted_local_price > adjusted_thailand_price_local_currency:
                price_difference = adjusted_local_price - adjusted_thailand_price_local_currency
                better_option = "Thailand offers a better gold price."
            elif adjusted_thailand_price_local_currency > adjusted_local_price:
                price_difference = adjusted_thailand_price_local_currency - adjusted_local_price
                better_option = "Your local country offers a better gold price."
            else:
                price_difference = 0
                better_option = "Both countries offer the same gold price."

            results = f"""
Gold Price Comparison:
Your Local Country: {self.format_european_number(adjusted_local_price)} {local_currency_symbol}/ounce
Thailand: {self.format_european_number(adjusted_thailand_price_local_currency)} {local_currency_symbol}/ounce
{better_option}
Price difference: {self.format_european_number(price_difference)} {local_currency_symbol}/ounce

Investment: {self.format_european_number(investment_amount)} {local_currency_symbol}
Your Local Country: {self.format_european_number(gold_amount_local, 4)} ounces
Thailand: {self.format_european_number(gold_amount_thailand, 4)} ounces
"""

            if self._root is not None:
                self._root.setProperty('resultsText', results)
            else:
                print("Error: Root object is not set.")

        except ValueError as e:
            if self._root is not None:
                self._root.setProperty('resultsText', f"Error: {e}")
            else:
                print(f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    main_backend = MainBackend()
    engine.rootContext().setContextProperty("main", main_backend)

    engine.load('main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    main_backend.set_root(engine.rootObjects()[0])

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
