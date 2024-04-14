# Creating a class
class Book:
    # Constructor method
    def __init__(self, title:str, author:str, price:float) -> None:
        self.title = title
        self.author = author
        self.price = price
    
    def discount(self,percent:float):
        """
        Applies discount to the price of the book object.

        Arguments:
        percent : float : the percentage discount for the book

        Returns:
        None
        """
        self.price -= (percent/100)*self.price

# The main code
if __name__ == "__main__":
    my_book = Book("The Alchemist", "Paulo Coelho", 21.99)
    print(f"\nI have a book, {my_book.title} written by {my_book.author} with price {my_book.price}")
    print("\nNow, I apply for a 30% discount in that book!!\n")
    my_book.discount(30)
    print(f"Now, my book's price is : {my_book.price:.2f}")