def greet(name):
  print("Hello {}, welcome to the world!".format(name))

if __name__ == "__main__":
  from sys import argv
  greet(argv[1]) # first command argument