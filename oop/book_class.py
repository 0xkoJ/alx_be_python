class Book:
    def __init__(self, title : str, author : str, year : str):
        self.title = title
        self.author = author
        self.year = year
        
    def __del__(self):
        """Destrutor that print delete message"""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """String representation of Book instance"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Representation of Book instance """
        return f"Book('{self.title}', '{self.author}', {self.year})"