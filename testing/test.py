class Model:
    def __setattr__(self, name: str, value) -> None:
        # Construct the name of the setter method
        setter_name = f"set_{name}"

        # Check if the setter method exists in the class
        setter_method = getattr(self, setter_name, None)
        print(setter_name)
        # If the setter method exists and is callable, call it
        if callable(setter_method):
            setter_method(value)  # Call the setter method with the value
        else:
            # Otherwise, set the attribute directly
            super().__setattr__(name, value)

class Book(Model):
    def __init__(self, title: str, page_count: int) -> None:
        super().__init__()
        self.title = title
        self.page_count = page_count

    def set_title(self, title: str):
        # Custom logic for setting the title
        print(f"Setting title to: {title}")

    
        # super().__setattr__('title', title)  # Actually set the attribute

# Example usage
book = Book("Harry Potter", 300)
book.title = "Harry Potter and the Philosopher's Stone"  # This will call __set_title