"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('src/foo.txt') as file:

    read_file = file.read()

print(read_file)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


with open('src/bar.txt', "w") as file2:
    file2.write("this is the first line\n")
    file2.write("this is the second line\n")
    file2.write("this is the third line\n")
