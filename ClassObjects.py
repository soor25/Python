# Classes starts with a capital letter
class Report:
    # __ two inderscores means its a private function. First argument in initialized function always have to be self 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # we are going to create a method, which is just a function inside of a class. .format is the value you will fill in the curly braces blanks with.
    def write_report(self,text):
        return '{} By: {} \n {}'.format(self.title, self.author, text)
    
    # Now we will use the class we just created.
# the first parameter is the title and the second is the author.
my_report = Report('I should have studied art', 'Mansur')

# we pull my_report because thats where its initialized, then we call the method .write_report because its the function within the class, then we need to pass parameters of that function which is just text
print(my_report.write_report('This is OOP'))