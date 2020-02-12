
import utility
import shopping.shopping_cart
from shopping.more_shopping.import_demo import printer
from shopping.more_shopping.import_demo import printer2 as imported_printer


if __name__ == "__main__":
    print(utility)
    print(utility.test("Hello"))

    print(shopping.shopping_cart.buy("Jacket"))

    print(printer("Hello from import demo!"))

    print((imported_printer("Hello from imported printer!")))



