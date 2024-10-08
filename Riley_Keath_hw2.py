pizza = ['margarita', 'plain', 'pepperoni'] 
for pizza in pizza: 
 print(f"{pizza.title()},")
 print(f"I enjoy {(pizza)} pizza, {pizza.title()}.\n") 
 
 print("I really love pizza!")

 
 
 
 
 
 
 birds= ['cassowary', 'kakapo', 'kiwi']
 for bird in birds:
  print(f"{bird.title()},")
  print(f"not a good pet {(bird)}")

  
for value in range(1,20):
 print(value)



def greet_user(Reader):
 """Display a simple greeting."""
print("Hello!")
 
greet_user("Reader")

print("In this chapter we will learn how to make a function in python")



def favorite_book(book):
 """Display statement."""
 print(f"This is my favorite book, {book.title()}")
 
favorite_book('Tao Te Ching')




def make_shirt(size, message):
    """Print a summary of the shirt's size and message."""
    print(f"The shirt is size {size} and has the message: '{message}'")


make_shirt('L', 'Nightsky')


make_shirt(size='M', message='I love python!')



def describe_city(city_type, conutry_name='indonsia'):
 """Display information about a city."""
 
 print(f" {city_type} is in {conutry_name.title()}.")

describe_city("jakarta")






def city_country(city, country):
    """Return a string in the format 'City, Country'."""
    return f"{city}, {country}"

formatted_location = city_country('Berlin', 'Germany')
print(formatted_location) 

