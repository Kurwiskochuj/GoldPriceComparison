import sys
from decimal import Decimal, getcontext
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Qt

# Set decimal precision for accurate financial calculations
getcontext().prec = 20

class MainBackend(QObject):
    def __init__(self):
        super().__init__()
        self._root = None

    def set_root(self, root):
        self._root = root

    def parse_european_number(self, s):
        """Parse a European-formatted number string to a Decimal."""
        try:
            s = s.strip().replace('.', '').replace(',', '.')
            return Decimal(s)
        except ValueError as e:
            raise ValueError(f"Invalid number format: {s}") from e

    def format_european_number(self, value, decimal_places=2):
        """Format a Decimal as a European-formatted number string."""
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        
        format_string = f"{{:.{decimal_places}f}}"
        formatted = format_string.format(value)
        integer_part, decimal_part = formatted.split('.')
        
        integer_with_thousand_sep = ''
        for i, digit in enumerate(reversed(integer_part)):
            if i % 3 == 0 and i != 0:
                integer_with_thousand_sep = '.' + integer_with_thousand_sep
            integer_with_thousand_sep = digit + integer_with_thousand_sep
        
        return f"{integer_with_thousand_sep},{decimal_part}"

    @Slot(str, str, str, str, str)
    def calculateResults(self, local_currency_symbol, exchange_rate_str, local_price_str, thailand_price_str, investment_amount_str):
        """Calculate and compare gold prices between the local country and Thailand.
        
        Args:
            local_currency_symbol (str): Symbol of the local currency (e.g., EUR)
            exchange_rate_str (str): Exchange rate between local currency and THB
            local_price_str (str): Gold price in the local country per ounce
            thailand_price_str (str): Gold price in Thailand per baht
            investment_amount_str (str): Investment amount in local currency
        
        Returns:
            None
        """
        try:
            # Parse input values
            local_currency_symbol = local_currency_symbol.strip()
            exchange_rate = self.parse_european_number(exchange_rate_str)
            local_price = self.parse_european_number(local_price_str)
            thailand_price_baht = self.parse_european_number(thailand_price_str)
            investment_amount = self.parse_european_number(investment_amount_str)
            local_purity = Decimal('0.9999')  # Default local purity
            thailand_purity = Decimal('0.965')  # Default Thailand purity

            # Validate input values
            if exchange_rate <= Decimal('0'):
                raise ValueError("Exchange rate must be a positive number.")
            if local_price <= Decimal('0'):
                raise ValueError("Gold price in your local country must be a positive number.")
            if thailand_price_baht <= Decimal('0'):
                raise ValueError("Gold price in Thailand must be a positive number.")
            if investment_amount <= Decimal('0'):
                raise ValueError("Investment amount must be greater than 0.")

            # Constants
            TROY_OUNCE_IN_GRAMS = Decimal('31.1034768')  # Grams per troy ounce
            GOLD_BAHT_WEIGHT_GRAMS = Decimal('15.244')    # Grams per baht

            # Calculate weight conversion factor
            gold_baht_weight = GOLD_BAHT_WEIGHT_GRAMS / TROY_OUNCE_IN_GRAMS

            # Adjust local price for purity
            adjusted_local_price = local_price / local_purity

            # Convert Thailand price to local currency
            thailand_price_local_currency_per_baht = thailand_price_baht / exchange_rate
            thailand_price_per_ounce_local_currency = thailand_price_local_currency_per_baht / gold_baht_weight
            adjusted_thailand_price_local_currency = thailand_price_per_ounce_local_currency / thailand_purity

            # Determine better option
            if adjusted_local_price > adjusted_thailand_price_local_currency:
                price_difference = adjusted_local_price - adjusted_thailand_price_local_currency
                better_option = "Thailand offers a better gold price."
            elif adjusted_thailand_price_local_currency > adjusted_local_price:
                price_difference = adjusted_thailand_price_local_currency - adjusted_local_price
                better_option = "Your local country offers a better gold price."
            else:
                price_difference = Decimal('0')
                better_option = "Both countries offer the same gold price."

            # Calculate gold amounts
            gold_amount_local = investment_amount / adjusted_local_price
            gold_amount_thailand = investment_amount / adjusted_thailand_price_local_currency

                       # Prepare results string with improved formatting
            results = f"""
Gold Price Comparison:

Your Local Country: {self.format_european_number(adjusted_local_price, 2)} {local_currency_symbol}/ounce
Thailand: {self.format_european_number(adjusted_thailand_price_local_currency, 2)} {local_currency_symbol}/ounce

{better_option}

Price Difference: {self.format_european_number(price_difference, 2)} {local_currency_symbol}/ounce

Investment: {self.format_european_number(investment_amount, 2)} {local_currency_symbol}
Your Local Country: {self.format_european_number(gold_amount_local, 4)} ounces
Thailand: {self.format_european_number(gold_amount_thailand, 4)} ounces
"""

            # Update UI or print results
            if self._root is not None:
                self._root.setProperty('resultsText', results)
            else:
                print(results)

        except ValueError as e:
            error_message = f"Error: {str(e)}"
            if self._root is not None:
                self._root.setProperty('resultsText', error_message)
            else:
                print(error_message)

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