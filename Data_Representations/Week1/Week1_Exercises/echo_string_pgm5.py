""" Program to echo a string given number of times in new line """

def echo(call, repeats):
    """
    Function which takes a string and number as argument and
    echoes the string given number of times
    """
    string = call + ("\n" + call) * (repeats - 1)
    print(string)

echo("Hello", 5)
echo("Guruvayoorappa", 108)
echo("Om Namo Narayanaya", 108)
echo("Om Sham Shanaishcharaya Nama", 108)
echo("Krishna", 100)

