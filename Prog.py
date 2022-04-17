# Main modules
from tkinter import *
from random import randint

# Sounds/SFX
from os import getcwd
from winsound import PlaySound, SND_FILENAME

try:
    with open("config.cfg", "x"):
        pass
except FileExistsError:
    pass

with open("config.cfg", "r") as f:
    readlines = f.readlines(0)
    sfx = readlines[0]
    if sfx == "False":
        sfx = False
    else:
        sfx = True

DONE = 'done'
TYPE = '__type'
BUTTON = 'buttons'
READONLY = 'read-only'
QUESTION = 'questions'
ANS = "__ans"
OUTPUT = "__output"
CODE = "__code"
BUTTONS = "__buttons"
QUESTION = "__question"
QUESTIONS = "__questions"
TASK = "__task"
CODEPOS = "__codepos"

CONSTANTS = {
    "COMPLETED_PERCENT" : 0,
    "TOTAL_LESSONS" : 5,
    "CODECOLOR" : "#040927",
    "CODECOLOR2" : "#22242f",
    "LIME" : "#7eff67",
    "GREEN" : "#27ff00",
    "GREEN2" : "#42b906",
    "LIGHTGREEN" : "#e5ff95",
    "LIGHTGREEN2" : "#e0ff84",
    "LIGHTBLUE2" : "#becfe5",
    "AQUA" : "#84ffde",
    "DARKBLUE" : "#003981",
    "ROSE" : "#ff0097",
    "BROWN" : "#b95806",
    "WHITE" : "#ffffff",
    "BLACK" : "#000000",
    "YELLOW" : "#ffff00",
    "BLUE" : "#000cff",
    "LIGHTBLUE" : "#00fff0",
    "BLUE2" : "#5f9bd3",
    "RED" : "#ff0000",
    "ORANGE" : "#ff8b00",
    "MAGENTA" : "#ff00f0",
    "PURPLE" : "#b200ff",
    "LIGHTPURPLE" : "#df95ff",
    "PINK" : "#ff95f7",
    "GRAY" : "#3d3e3a",
    "LIGHTGRAY" : "#595a54",
    "CODEFONT" : "Courier New",
    "MAINFONT" : "Arial",
    "LESSON_DATA" : {
        "PRINTING" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Printing in python is only print()!",
                "__output" : "",
                "__code" : "print()",
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Code a print statement",
                "__buttons" : [")", "(", "print"],
                "__codepos" : END,
                "__output" : "",
                "__ans" : "print()",
                "__code" : ""
            },
            "LESSON_3" : {
                "__type" : "questions",
                "__question" : "How do we code printing?",
                "__questions" : {
                    "__answer1" : "We cannot code printing in python",
                    "__answer2" : "print()"
                },
                "__ans" : "print()"
            },
            "LESSON_4" : {
                "__type" : "read-only",
                "__task" : "Printing can also print a message but you must put this\nin apostraphes or speech marks",
                "__output" : "Hello",
                "__code" : "print('Hello')"
            },
            "LESSON_5" : {
                "__type" : "buttons",
                "__task" : "That is basically it for very basic printing",
                "__buttons" : ["'Hello World'", ")", "print", "("],
                "__codepos" : END,
                "__output" : "Hello World",
                "__ans" : "print('Hello World')",
                "__code" : ""
            },
            "LESSON_6" : {
                "__type" : "done"
            }
        },
        "VARIABLES" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Variables in python is a bit complicated\nbut easy to get the hang of:",
                "__code" : "variable1 = ",
                "__output" : ""
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Create a variable called variable",
                "__buttons" : ["variable ", "="],
                "__codepos" : END,
                "__output" : "",
                "__ans" : "variable =",
                "__code" : ""
            },
            "LESSON_3" : {
                "__type" : "buttons",
                "__task" : "However, variables need a value.\nif it doesn't then it will give an error",
                "__buttons" : ["= ", "variable ", "''"],
                "__codepos" : END,
                "__output" : "",
                "__ans" : "variable = ''",
                "__code" : ""
            },
            "LESSON_4" : {
                "__type" : "questions",
                "__question" : "What can be our variable name?",
                "__questions" : {
                    "__answer1" : "Any",
                    "__answer2" : "variable",
                    "__answer3" : "Only Numbers"
                },
                "__ans" : "Any"
            },
            "LESSON_5" : {
                "__type" : "read-only",
                "__task" : "To show the error you would get if you don't\nenter a value:",
                "__code" : "variable = ",
                "__output" : "variable = \n           ^\nSyntaxError: invalid syntax"
            },
            "LESSON_6" : {
                "__type" : "done"
            }
        },
        "INPUTTING" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Inputting is accessed using the input() method\nthis will gather an input from the user",
                "__code" : "input()",
                "__output" : "No Output"
            },
            "LESSON_2" : {
                "__type" : "read-only",
                "__task" : "Now, how do we access the input?",
                "__code" : "user = input()",
                "__output" : "No Output"
            },
            "LESSON_3" : {
                "__type" : "buttons",
                "__task" : "Now you try",
                "__buttons" : ["input", ")", "variable ", "= ", "("],
                "__codepos" : END,
                "__output" : "",
                "__code" : "",
                "__ans" : "variable = input()"
            },
            "LESSON_4" : {
                "__type" : "read-only",
                "__task" : "We can print something for the user to go off of\nin the brackets",
                "__code" : "input('What is your age?')",
                "__output" : "What is your age?"
            },
            "LESSON_5" : {
                "__type" : "questions",
                "__question" : "What is an input?",
                "__questions" : {
                    "__answer1" : "Gathering user input",
                    "__answer2" : "Giving information for python to print",
                    "__answer3" : "Making a variable that stores a value",
                    "__answer4" : "Gathering user input and making a\nvariable that stores a value"
                },
                "__ans" : "Gathering user input and making a\nvariable that stores a value"
            },
            "LESSON_6" : {
                "__type" : "done"
            }
        },
        "OPERATIONS" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Operations in python is basically just a complicated word\nfor dividing, adding, multiplying and subtracting",
                "__code" : "1 * 5\n50 + 25\n2 / 2\n100 - 50",
                "__output" : ""
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Print what 50 + 25 is using the + operation",
                "__buttons" : [")", "+ ", "25 ", "print(", "50 "],
                "__codepos" : END,
                "__code" : "",
                "__output" : str(50+25),
                "__ans" : ["print(25 + 50 )", "print(50 + 25 )"]
            },
            "LESSON_3" : {
                "__type" : "buttons",
                "__task" : "Print what 500 - 45 is using the - operation",
                "__buttons" : ["print(", "- ", "45", "500 ", ")"],
                "__codepos" : END,
                "__code" : "",
                "__output" : str(500-45),
                "__ans" : "print(500 - 45)"
            },
            "LESSON_4" : {
                "__type" : "buttons",
                "__task" : "Print what 25 ÷ 5 is using the / operation",
                "__buttons" : ["print(", "5", ")", "/ ", "25 "],
                "__codepos" : END,
                "__code" : "",
                "__output" : str(25/5),
                "__ans" : "print(25 / 5)"
            },
            "LESSON_5" : {
                "__type" : "questions",
                "__question" : "What are the 4 operations?",
                "__questions" : {
                    "__answer1" : "division, multiplication, subtraction and addition",
                    "__answer2" : "printing, inputting, calculations and ifs"
                },
                "__ans" : "division, multiplication, subtraction and addition"
            },
            "LESSON_6" : {
                "__type" : "done"
            }
        },
        "SUPERCHARGEBASIC" : {
            "LESSON_1" : {
                "__type" : "buttons",
                "__task" : "Print the input (\\n is a new line)",
                "__buttons" : ["print", ")", "user", "("],
                "__codepos" : END,
                "__code" : "user = input('What is your favourite color?\\n')\n",
                "__output" : "What is your favourite color\nblue\nblue\n(for example)",
                "__ans" : "user = input('What is your favourite color?\\n')\nprint(user)"
            },
            "LESSON_2" : {
                "__type" : "typing",
                "__task" : "Print 25 + 25 ÷ 2 by typing it in",
                "__code" : "",
                "__output" : str((25 + 25) / 2),
                "__ans" : ["print(25+25/2)", "print(25 + 25 /2)", "print(25+ 25/2", "print(25+25 /2)", "print(25 +25/2", "print(25+25 / 2"]
            },
            "LESSON_3" : {
                "__type" : "buttons",
                "__task" : "Create an empty variable",
                "__buttons" : ["variable ", "="],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : "variable ="
            },
            "LESSON_4" : {
                "__type" : "questions",
                "__question" : "What is the defines a variable as a variable",
                "__questions" : {
                    "__answer1" : "The = sign",
                    "__answer2" : "The spaces in between",
                    "__answer3" : "The variable name"
                },
                "__ans" : "The = sign"
            },
            "LESSON_5" : {
                "__type" : "done"
            }
        },
        "INTEGERS" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Integers (int for short) are just numbers:",
                "__code" : "5\n6\n1\n100\n54",
                "__output" : ""
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Add 5 and 5 and print it",
                "__buttons" : ["(", "5", "+", "5", ")", "print"],
                "__codepos" : END,
                "__code" : "",
                "__output" : str(5+5),
                "__ans" : "print(5+5)"
            },
            "LESSON_3" : {
                "__type" : "read-only",
                "__task" : "Printing can only print the current type in the print:",
                "__code" : "print(50 '')",
                "__output" : "print(50 '')\n          ^\nSyntaxError: invalid syntax"
            },
            "LESSON_4" : {
                "__type" : "questions",
                "__question" : "What is an integer?",
                "__questions" : {
                    "__answer1" : "A value that is surrounded in apostrophes or speech marks",
                    "__answer2" : "A value that is a number",
                    "__answer3" : "A value that has multiple values inside it"
                }
            },
            "LESSON_5" : {
                "__type" : "buttons",
                "__task" : "Integers are like any other value.\nThey can be stored in a variable",
                "__buttons" : ["integer ", "100", "= "],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : "integer = 100"
            },
            "LESSON_6" : {
                "__type" : "done"
            }
        },
        "STRINGS" : {
            "LESSON_1" : {
                "__type" : "buttons",
                "__task" : "Strings (str for short) are values surrounded with apostraphes and speech marks",
                "__buttons" : ["string ", "'", "= ", "im a string!", "'"],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : "string = 'im a string!'"
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "You can add more onto strings with the + operation",
                "__buttons" : ["print", ")", "+", "string2", "(", "string1"],
                "__codepos" : END,
                "__code" : "string1 = 'hello!'\nstring2 = ' I am a program!'\n",
                "__output" : "hello! I am a program",
                "__ans" : ["string1 = 'hello!'\nstring2 = ' I am a program!\nprint(string1+string2)", "print(string2+string1)"]
            },
            "LESSON_3" : {
                "__type" : "read-only",
                "__task" : "You can use the * operator to change all the characters to another",
                "__code" : "string1 = 'I dont want you to see me.'\nprint(string1)\nstring2 = '*' * len(string1)\nprint(string2)",
                "__output" : "I dont want you to see me.\n**************************"
            },
            "LESSON_4" : {
                "__type" : "buttons",
                "__task" : "Overwrite and make all the characters in string1 to *",
                "__buttons" : ["'*'", "string1 = ", "len(", "string1", ")", "*"],
                "__codepos" : END,
                "__code" : "string1 = 'Secret'\n",
                "__output" : "",
                "__ans" : "string1 = 'Secret'\nstring1 = '*'*len(string1)"
            },
            "LESSON_5" : {
                "__type" : "read-only",
                "__task" : "Strings have useful methods and functions attributes:",
                "__code" : "string = 'Test'\nprint(string.__contains__('e'))\nprint(string.lstrip('Te'))\nprint(string.lower())\nprint(string.upper())",
                "__output" : "True\nst\ntest\nTEST"
            },
            "LESSON_6" : {
                "__type" : "questions",
                "__question" : "What are strings?",
                "__questions" : {
                    "__answer1" : "Numbers",
                    "__answer2" : "Values in apostraphes or speech marks",
                    "__answer3" : "True or false"
                },
                "__ans" : "Values in apostraphes or speech marks"
            },
            "LESSON_7" : {
                "__type" : "done"
            }
        },
        "FLOATS" : {
            "LESSON_1" : {
                "__type" : "read-only",
                "__task" : "Floats (floating point numbers) are decimals and are like any\nother value and can be assigned to a variable",
                "__code" : "float = 0.5",
                "__output" : ""
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Assign a floating point number to a variable",
                "__buttons" : ["2", "1", "float ", ".", "= "],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : ["float = 2.1", "float = 1.2"]
            },
            "LESSON_3" : {
                "__type" : "typing",
                "__task" : "Assign a float (1.2) to a variable (number) and print it",
                "__code" : "",
                "__output" : "1.2",
                "__ans" : "number = 1.2\nprint(number)"
            },
            "LESSON_4" : {
                "__type" : "questions",
                "__question" : "What is a float?",
                "__questions" : {
                    "__answer1" : "A number",
                    "__answer2" : "A decimal"
                },
                "__ans" : "A decimal"
            },
            "LESSON_5" : {
                "__type" : "done"
            }
        },
        "BOOLEANS" : {
            "LESSON_1" : {
                "__type" : "buttons",
                "__task" : "Booleans (bools/bool for short) are True or False (they need capitals)\nAssign a boolean value to a variable",
                "__buttons" : ["True", "boolean ", "= "],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : "boolean = True"
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Without any more advanced things, you cannot really do much with booleans",
                "__buttons" : ["boolean_false ", "= ", "True", "False"],
                "__codepos" : END,
                "__code" : "",
                "__output" : "",
                "__ans" : "boolean_false = False"
            },
            "LESSON_3" : {
                "__type" : "questions",
                "__question" : "What is a boolean?",
                "__questions" : {
                    "__answer1" : "True or False",
                    "__answer2" : "A number",
                    "__answer3" : "A decimal",
                    "__answer4" : "A value surrounded in apostraphes or speech marks"
                },
                "__ans" : "True or False"
            },
            "LESSON_4" : {
                "__type" : "questions",
                "__question" : "What is short for boolean/booleans?",
                "__questions" : {
                    "__answer1" : "bool/bools",
                    "__answer2" : "floating point number"
                },
                "__ans" : "bool/bools"
            },
            "LESSON_5" : {
                "__type" : "done"
            }
        },
        "SUPERCHARGETYPES" : {
            "LESSON_1" : {
                "__type" : "buttons",
                "__task" : "Check if string1 contains i",
                "__buttons" : ["__contains__", "('", ".", "i", "')", "string1"],
                "__codepos" : END,
                "__code" : "string1 = 'but I dont contain i'\n",
                "__output" : "",
                "__ans" : "string1 = 'but I dont contain i'\nstring1.__contains__('i')"
            },
            "LESSON_2" : {
                "__type" : "buttons",
                "__task" : "Check the type of True using type()",
                "__buttons" : ["type", "(", "True", ")", "booltype = "],
                "__codepos" : END+"-"+str(len("\nprint(booltype)")+1)+"c",
                "__code" : "\nprint(booltype)",
                "__output" : "<class 'bool'>",
                "__ans" : "booltype = type(True)\nprint(booltype)"
            },
            "LESSON_3" : {
                "__type" : "typing",
                "__task" : "Check the type of 0.5 and assign it to a variable called floattype\nand, on a new line, print it",
                "__code" : "",
                "__output" : "<class 'float'>",
                "__ans" : "floattype = type(0.5)\nprint(floattype)"
            },
            "LESSON_4" : {
                "__type" : "buttons",
                "__task" : "Turn every character into '*' in string1",
                "__buttons" : ["(", "'*'", ")", "string1", " len", "string1 = ", " *"],
                "__codepos" : END,
                "__code" : "string1 = 'My_password123'\n",
                "__output" : "",
                "__ans" : "string1 = 'My_password123'\nstring1 = '*' * len(string1)"
            },
            "LESSON_5" : {
                "__type" : "done"
            }
        },
        "COMPARINGSTRINGS" : {
            "LESSON_1" : {
                TYPE : READONLY,
                TASK : "Comparing strings is for seeing if strings are the same",
                CODE : "print('this is the same'=='this is the same')",
                OUTPUT : "True"
            },
            "LESSON_2" : {
                TYPE : BUTTON,
                TASK : "Make a variable with the value 'hello!'\nand print if it is the same to 'hello'",
                BUTTONS : ["'hello!'", "'hello'", "variable = ", "print(", ")", "==", "'hello'"],
                CODEPOS : END,
                CODE : "",
                OUTPUT : "False",
                ANS : ["variable = 'hello!'\nprint('hello'==variable)", "variable = 'hello!'\nprint(variable=='hello')"]
            }
        },
        "COMPARINGINTEGERS" : {
            "LESSON_1" : {
                TYPE : READONLY
            }
        },
        "IFSTATEMENTS" : {
            "LESSON_1" : {
                TYPE : READONLY,
                TASK : "If statements are like decisions in the code",
                CODE : "variable = 5\nif variable == 5:\n   print(variable)",
                OUTPUT : "5"
            }
        },
        "ELSESTATEMENTS" : {
            "LESSON_1" : {
                TYPE : READONLY
            }
        }
    }
}

class basic_python:
    def function(self):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        basic_python_button.destroy()
        basic_types_button.destroy()
        comparisions_button.destroy()
        conditional_statements_button.destroy()
        default_title.destroy()
        minecraftripoff.destroy()
        
        self.back = Button(app, bg=CONSTANTS["RED"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Back", bd=0, command=self.back_func)

        title.config(text="Basic Python")

        canvas.create_window(400, 50, window=title)
        canvas.create_window(200, 375, window=printing_button)
        canvas.create_window(200, 475, window=variables_button)
        canvas.create_window(400, 375, window=inputting_button)
        canvas.create_window(400, 475, window=operations_button)
        canvas.create_window(650, 425, window=SUPERCHARGEBASIC_button)
    
    def back_func(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        canvas.create_window(200, 375, window=basic_python_button)
        canvas.create_window(200, 475, window=basic_types_button)
        canvas.create_window(400, 100, window=default_title)
        
    def printing(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        AutoCreate(CONSTANTS["LESSON_DATA"]["PRINTING"], app, "printing")

    def variables(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        AutoCreate(CONSTANTS["LESSON_DATA"]["VARIABLES"], app, "variables")

    def inputting(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        AutoCreate(CONSTANTS["LESSON_DATA"]["INPUTTING"], app, "inputting")
    
    def operations(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        AutoCreate(CONSTANTS["LESSON_DATA"]["OPERATIONS"], app, "operations")
    
    def SUPERCHARGE(self):
        printing_button.destroy()
        title.destroy()
        variables_button.destroy()
        inputting_button.destroy()
        operations_button.destroy()
        SUPERCHARGEBASIC_button.destroy()

        AutoCreate(CONSTANTS["LESSON_DATA"]["SUPERCHARGEBASIC"], app, "SUPERCHARGEBASIC")

class basic_types:
    def function(self):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        basic_python_button.destroy()
        basic_types_button.destroy()
        comparisions_button.destroy()
        conditional_statements_button.destroy()
        default_title.destroy()
        minecraftripoff.destroy()

        title.config(text="Basic Types")

        canvas.create_window(400, 50, window=title)
        canvas.create_window(200, 375, window=integers_button)
        canvas.create_window(200, 475, window=floats_button)
        canvas.create_window(400, 375, window=strings_button)
        canvas.create_window(400, 475, window=booleans_button)
        canvas.create_window(650, 425, window=SUPERCHARGETYPES_button)
    
    def integers(self):
        integers_button.destroy()
        floats_button.destroy()
        strings_button.destroy()
        booleans_button.destroy()
        SUPERCHARGETYPES_button.destroy()
        title.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["INTEGERS"], app, "integers")
    
    def floats(self):
        integers_button.destroy()
        floats_button.destroy()
        strings_button.destroy()
        booleans_button.destroy()
        SUPERCHARGETYPES_button.destroy()
        title.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["FLOATS"], app, "floats")
    
    def strings(self):
        integers_button.destroy()
        floats_button.destroy()
        strings_button.destroy()
        booleans_button.destroy()
        SUPERCHARGETYPES_button.destroy()
        title.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["STRINGS"], app, "strings")
    
    def booleans(self):
        integers_button.destroy()
        floats_button.destroy()
        strings_button.destroy()
        booleans_button.destroy()
        SUPERCHARGETYPES_button.destroy()
        title.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["BOOLEANS"], app, "booleans")
    
    def SUPERCHARGETYPES(self):
        integers_button.destroy()
        floats_button.destroy()
        strings_button.destroy()
        booleans_button.destroy()
        SUPERCHARGETYPES_button.destroy()
        title.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["SUPERCHARGETYPES"], app, "SUPERCHARGETYPES")

class comparisions:
    def function(self):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        minecraftripoff.destroy()
        basic_python_button.destroy()
        basic_types_button.destroy()
        default_title.destroy()
        comparisions_button.destroy()
        conditional_statements_button.destroy()
        title.config(text="Comparisions")

        canvas.create_window(400, 50, window=title)
        canvas.create_window(200, 275, window=comparing_integers_button)
        canvas.create_window(200, 375, window=comparing_strings_button)
    
    def cstrings(self):
        title.destroy()
        comparing_integers_button.destroy()
        comparing_strings_button.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["COMPARINGSTRINGS"], app, "cstrings")

    def cints(self):
        title.destroy()
        comparing_strings_button.destroy()
        comparing_integers_button.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["COMPARINGINTEGERS"], app, "cints")

class conditionalstatements:
    def function(self):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        minecraftripoff.destroy()
        basic_python_button.destroy()
        basic_types_button.destroy()
        comparisions_button.destroy()
        conditional_statements_button.destroy()
        default_title.destroy()
        title.config(text="Conditional Statements")

        canvas.create_window(200, 275, window=if_statements_button)
        canvas.create_window(200, 375, window=else_statements_button)
        canvas.create_window(400, 50, window=title)
    
    def if_statements(self):
        title.destroy()
        if_statements_button.destroy()
        else_statements_button.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["IFSTATEMENTS"], app, "if_statement")
    
    def else_statements(self):
        title.destroy()
        if_statements_button.destroy()
        else_statements_button.destroy()
        AutoCreate(CONSTANTS["LESSON_DATA"]["ELSESTATEMENTS"], app, "else_statement")

class confusingencoding:
    """Encode messages in a confusing manner."""
    def __init__(self, message):
        self.message = message
        self.encoding_type = {"r" : "1","'" : "2","#" : "3","m" : "4",";" : "5","." : "6","p" : "7","Z" : "8","}" : "9","[" : "0"}
        self.encoding_type_reverse = {"1" : "r", "2" : "'", "3" : "#", "4" : "m", "5" : ";", "6" : ".", "7" : "p", "8" : "Z", "9" : "}", "0" : "["}
    
    def encode(self):
        """For encoding the weird language"""
        for number in self.message:
            if number in list(self.encoding_type.keys()):
                self.message = self.message.replace(number, self.encoding_type[number])
        return self.message
    
    def decode(self):
        """For decoding the weird language"""
        for number in self.message:
            if number in list(self.encoding_type_reverse.keys()):
                self.message = self.message.replace(number, self.encoding_type_reverse[number])
        return self.message

def done(lesson_name: str):
    """For when a lesson finishes"""
    if CONSTANTS["COMPLETED_PERCENT"] == 0:
        CONSTANTS["COMPLETED_PERCENT"] = 1
    else:
        CONSTANTS["COMPLETED_PERCENT"] += int(CONSTANTS["TOTAL_LESSONS"])/CONSTANTS["COMPLETED_PERCENT"]
    if CONSTANTS["COMPLETED_PERCENT"] >= 100:
        CONSTANTS["COMPLETED_PERCENT"] = 100
    try:
        with open("data.txt", "x") as f:
            f.close()
    except FileExistsError:
        pass

    with open("data.txt", "w") as f:
        f.write(confusingencoding(str(CONSTANTS["COMPLETED_PERCENT"])).encode())
        f.close()
    
    print("Please restart the program. Your data has been saved!")
    exit(0)

def read_data():
    """For reading data from data.txt (to get data and apply it)"""
    try:
        with open("data.txt", "x") as f:
            f.close()
    except FileExistsError:
        pass
    
    with open("data.txt", "r") as f:
        readlines = f.readlines(0)
        try:
            CONSTANTS["COMPLETED_PERCENT"] = int(readlines[0].rstrip("\n"))
            CONSTANTS["CURRENT_LESSONS"] = list(readlines[1].rstrip("\n"))
        except IndexError:
            pass
        f.close()

class AutoCreate:
    """For creating guis based on the data given"""
    def __init__(self, data: dict, app: Tk, lesson_name: str):
        self.data = data
        self.app = app
        self.current_character = []
        self.current_button = []
        self.lesson = 0
        self.lesson_name = lesson_name
        self.lessons(self.data["LESSON_" + str(self.lesson+1)])
    
    def delete_components(self):
        self.cont.destroy()
        try:
            self.output.destroy()
            self.output_title.destroy()
        except AttributeError:
            pass

        try:
            self.code.destroy()
            self.code_title.destroy()
        except AttributeError:
            pass

        try:
            self.task.destroy()
            self.todo.destroy()
        except AttributeError:
            pass

        self.current_button = []
        self.current_character = []

        try:
            for button in list(self.buttons.values()):
                button.destroy()
            else:
                self.buttons = {}
            self.backspaceb.destroy()
        except:
            pass

        try:
            for question in list(self.questions.values()):
                question.destroy()
            else:
                self.questions = {}
            self.question.destroy()
        except:
            pass
    
    def code_button(self, code_piece: str, code_button: Button, code: Text, *, pos=None):
        self.current_character.append(code_piece)
        self.current_button.append(code_button)

        code.config(state=NORMAL)
        if pos != None:
            code.insert(pos, self.current_character[-1])
        else:
            code.insert(END, self.current_character[-1])
        code.config(state=DISABLED)

        self.current_button[-1].config(state=DISABLED)
        PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
    
    def backspace(self, code: Text):
        try:
            code.config(state=NORMAL)
            code.delete(END+"-"+str(self.current_character[-1].__len__()+1)+"c", END)
            code.config(state=DISABLED)

            self.current_button[-1].config(state=NORMAL)

            self.current_button.pop(-1)
            self.current_character.pop(-1)
        except:
            pass
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
    
    def change_question_answer(self, answer: str, button: Button):
        try:
            self.current_button[-1].config(state=NORMAL)
            self.current_button.pop(-1)
        except IndexError:
            pass
        self.current_button.append(button)
        self.answer = answer
        button.config(state=DISABLED)
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
    
    def next_lesson(self, cur_data: dict):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        self.cont.destroy()
        if cur_data["__type"] == "buttons":
            for i in range(len(cur_data["__buttons"])):
                self.buttons[i].destroy()
            
            self.output = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=5)
            self.output_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="Output", anchor="w", width=35)

            try:
                self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="Continue", command=lambda: self.lessons(self.data["LESSON_"+str(self.lesson+1)]))  
            except KeyError:
                done()
            
            if cur_data["__output"] == "":
                self.output.insert(END, "No Output")
            else:
                self.output.insert(END, cur_data["__output"])
            self.output.config(state=DISABLED)

            if type(cur_data["__buttons"]) == str:
                if self.code.get("1.0", END).rstrip("\n") == cur_data["__ans"]:
                    self.output_title.config(fg="lime", text="Output - Correct")
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    self.output_title.config(fg="red", text="Output - Incorrect")
                    self.code.insert(END, "\n\nAnswer: " + cur_data["__ans"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            elif type(cur_data["__buttons"]) == list:
                if self.code.get("1.0", END).rstrip("\n") in cur_data["__ans"]:
                    self.output_title.config(fg="lime", text="Output - Correct")
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    self.output_title.config(fg="red", text="Output - Incorrect")
                    self.code.insert(END, "\n\nAnswer: " + cur_data["__ans"][0])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            
            canvas.create_window(400, 450, window=self.output)
            canvas.create_window(400, 380, window=self.output_title)
            canvas.create_window(400, 550, window=self.cont)
        elif cur_data["__type"] == "questions":
            try:
                self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Continue", command=lambda: self.lessons(self.data["LESSON_" + str(self.lesson+1)]), bd=0)
            except KeyError:
                done()
            
            try:
                selected_button = self.questions[self.answer]
                correct_answer_button = self.questions[cur_data["__ans"]]
                selected_button.config(state=NORMAL)
            except:
                pass
            
            try:
                if self.answer == cur_data["__ans"]:
                    selected_button.config(bg=CONSTANTS["GREEN2"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    selected_button.config(bg='red')
                    correct_answer_button.config(bg=CONSTANTS["GREEN2"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            except:
                pass

            canvas.create_window(400, 550, window=self.cont)
        elif cur_data["__type"] == "code-questions":
            try:
                self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Continue", command=lambda: self.lessons(self.data["LESSON_" + str(self.lesson+1)]), bd=0)
            except KeyError:
                done()
            
            try:
                selected_button = self.questions[self.answer]
                correct_answer_button = self.questions[cur_data["__ans"]]
                selected_button.config(state=NORMAL)
            except:
                pass
            
            try:
                if self.answer == cur_data["__ans"]:
                    selected_button.config(bg=CONSTANTS["GREEN2"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    selected_button.config(bg='red')
                    correct_answer_button.config(bg=CONSTANTS["GREEN2"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            except:
                pass

            canvas.create_window(400, 550, window=self.cont)
        elif cur_data["__type"] == "typing":
            self.output = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=5)
            self.output_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="Output", anchor="w", width=35)

            try:
                self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="Continue", command=lambda: self.lessons(self.data["LESSON_"+str(self.lesson+1)]))  
            except KeyError:
                done()
            
            if cur_data["__output"] == "":
                self.output.insert(END, "No Output")
            else:
                self.output.insert(END, cur_data["__output"])
            self.output.config(state=DISABLED)

            if type(cur_data["__ans"]) == "<class 'str'":
                if self.code.get("1.0", END).rstrip("\n") == cur_data["__ans"] and cur_data["__ans"] != "" and self.code.get("1.0",END).rstrip("\n") != "":
                    self.output_title.config(fg="lime", text="Output - Correct")
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    self.output_title.config(fg="red", text="Output - Incorrect")
                    self.code.insert(END, "\n\nAnswer: " + cur_data["__ans"])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            elif type(cur_data["__ans"]) == "<class 'list'":
                if self.code.get("1.0", END).rstrip("\n") in cur_data["__ans"] and cur_data["__ans"] != "" and self.code.get("1.0",END).rstrip("\n") != "":
                    self.output_title.config(fg="lime", text="Output - Correct")
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Correct.wav", SND_FILENAME)
                else:
                    self.output_title.config(fg="red", text="Output - Incorrect")
                    self.code.insert(END, "\n\nAnswer: " + cur_data["__ans"][0])
                    if sfx:
                        PlaySound(getcwd()+"\\S\\Incorrect.wav", SND_FILENAME)
            
            canvas.create_window(400, 450, window=self.output)
            canvas.create_window(400, 380, window=self.output_title)
            canvas.create_window(400, 550, window=self.cont)
        else:
            self.output = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=5)
            self.output_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Output", anchor="w", width=35, bd=0)
            try:
                self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Continue", command=lambda: self.lessons(self.data["LESSON_" + str(self.lesson+1)]), bd=0)
            except KeyError:
                done()
            
            if cur_data["__output"] == "":
                self.output.insert(END, "No Output")
            else:
                self.output.insert(END, cur_data["__output"])
            
            canvas.create_window(400, 450, window=self.output)
            canvas.create_window(400, 380, window=self.output_title)
            canvas.create_window(400, 550, window=self.cont)
    
    def lessons(self, cur_data: dict):
        if sfx:
            PlaySound(getcwd()+"\\S\\Select.wav", SND_FILENAME)
        try:
            self.delete_components()
        except:
            pass
        self.lesson += 1

        if cur_data["__type"] == "read-only":
            self.task = Label(self.app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__task"], bd=0)
            self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Submit", bd=0, command=lambda: self.next_lesson(cur_data))

            self.code = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=10)
            self.code_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="script.py", anchor="w", width=35)
            
            if cur_data["__code"] != "":
                self.code.insert(END, cur_data["__code"])
            
            self.code.config(state=DISABLED)

            canvas.create_window(400, 50, window=self.task)
            canvas.create_window(400, 550, window=self.cont)
            canvas.create_window(400, 230, window=self.code)
            canvas.create_window(400, 105, window=self.code_title)
        elif cur_data["__type"] == "buttons":
            self.task = Label(self.app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__task"], bd=0)
            self.todo = Label(self.app, bg=CONSTANTS["BLUE2"], fg=CONSTANTS["GRAY"], font=(CONSTANTS["CODEFONT"],12,"bold"), text="Tap the buttons below the code".title())
            self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Submit", bd=0, command=lambda: self.next_lesson(cur_data))

            self.code = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=10)
            self.code_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="script.py", anchor="w", width=35)
            
            if cur_data["__code"] != "":
                self.code.insert(END, cur_data["__code"])
            
            self.code.config(state=DISABLED)
            
            self.buttons = {}
            for i in range(len(cur_data["__buttons"])):
                self.button = Button(self.app, bg=CONSTANTS["GRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__buttons"][i], bd=0)
                self.buttons[i] = self.button
                self.button.config(command=lambda c=i: self.code_button(cur_data["__buttons"][c], self.buttons[c], self.code, pos=cur_data["__codepos"]))
                canvas.create_window((100)+i*100, 375, window=self.button)
            
            self.backspaceb = Button(self.app, bg=CONSTANTS["RED"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Backspace", bd=0, command=lambda: self.backspace(self.code))

            canvas.create_window(400, 50, window=self.task)
            canvas.create_window(400, 100, window=self.todo)
            canvas.create_window(400, 550, window=self.cont)
            canvas.create_window(400, 230, window=self.code)
            canvas.create_window(400, 105, window=self.code_title)
            canvas.create_window(400, 425, window=self.backspaceb)
        elif cur_data["__type"] == "questions":
            self.answer = ""
            self.question = Label(self.app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__question"], bd=0)
            self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Submit", command=lambda: self.next_lesson(cur_data), bd=0)

            self.questions = {}
            for i in range(len(cur_data["__questions"])):
                try:
                    i += 1
                    i_ans = cur_data["__questions"]["__answer"+str(i)]
                    self.questions[i_ans] = Button(self.app, bd=0, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],12,"bold"), text=i_ans)
                    try:
                        self.questions[i_ans].config(state=NORMAL, command=lambda c=i, c_ans=i_ans: self.change_question_answer(cur_data["__questions"]["__answer"+str(c)], self.questions[c_ans]))
                    except TclError:
                        pass
                    canvas.create_window(400, (149)+i*75, window=self.questions[i_ans])
                except KeyError:
                    pass

            canvas.create_window(400, 50, window=self.question)
            canvas.create_window(400, 575, window=self.cont)
        elif cur_data["__type"] == "done":
            self.delete_components()
            done(self.lesson_name)
        elif cur_data["__type"] == "code-questions":
            try:
                self.delete_components()
            except:
                pass
            
            self.answer = ""
            self.task = Label(self.app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__task"], bd=0)
            self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Submit", bd=0, command=lambda: self.next_lesson(cur_data))

            self.code = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=10)
            self.code_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="script.py", anchor="w", width=35)

            self.questions = {}
            for i in range(len(cur_data["__questions"])):
                try:
                    i += 1
                    i_ans = cur_data["__questions"]["__answer"+str(i)]
                    self.questions[i_ans] = Button(self.app, bd=0, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],12,"bold"), text=i_ans)
                    try:
                        self.questions[i_ans].config(state=NORMAL, command=lambda c=i, c_ans=i_ans: self.change_question_answer(cur_data["__questions"]["__answer"+str(c)], self.questions[c_ans]))
                    except TclError:
                        pass
                    canvas.create_window(400, (300)+i*75, window=self.questions[i_ans])
                except KeyError:
                    pass

            canvas.create_window(400, 50, window=self.question)
            canvas.create_window(400, 575, window=self.cont)
            canvas.create_window(400, 230, window=self.code)
            canvas.create_window(400, 105, window=self.code_title)  
        elif cur_data["__type"] == "typing":
            try:
                self.delete_components()
            except:
                pass

            self.task = Label(self.app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=cur_data["__task"], bd=0)
            self.todo = Label(self.app, bg=CONSTANTS["BLUE2"], fg=CONSTANTS["GRAY"], font=(CONSTANTS["CODEFONT"],12,"bold"), text="Type in your answer in the code below".title())
            self.cont = Button(self.app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Submit", bd=0, command=lambda: self.next_lesson(cur_data))

            self.code = Text(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, width=35, height=10)
            self.code_title = Label(self.app, bg=CONSTANTS["CODECOLOR"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), bd=0, text="script.py", anchor="w", width=35)
            
            if cur_data["__code"] != "":
                self.code.insert(END, cur_data["__code"])

            canvas.create_window(400, 50, window=self.task)
            canvas.create_window(400, 550, window=self.cont)
            canvas.create_window(400, 230, window=self.code)
            canvas.create_window(400, 105, window=self.code_title)

app = Tk()
app.title("Prog - Programming Learner")

read_data()

canvas = Canvas(app, bg=CONSTANTS["BLUE2"], width=800, height=600)

__version__ = "1.0"
update = "Update v"+__version__+"\nRelease & SFX"
main_update_log = Label(app, bg=CONSTANTS["BLUE2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text=update, bd=0)

minecraftripoff_QUOTES = ["Also try mimo!", "Theres lots to learn!", "Python is complicated?", "Python the snake?", "Start with basic python lessons!", "This is not a ripoff!", "Lessons!", "Created by Alex Tubb, not a promotion.", "The hall of the mountain python?", "Distraction py?", "How do I work out 5 + 1823481230418? Python!", "Help!!", "Square brackets can help?", "Wait. Equal does something?", "Curly brackets or braces?", "IDLE. That's what I am", "Auto creation?", "Data isn't actually stored in data.txt LOL", "What can I name a variable? Anything!", "This text is not a ripoff from minecraft. Don't say otherwise"]
minecraftripoff = Label(app, bg=CONSTANTS["BLACK"], fg="white", font=(CONSTANTS["CODEFONT"],10,"bold"), text=minecraftripoff_QUOTES[randint(0,minecraftripoff_QUOTES.__len__()-1)], bd=0)
title = Label(app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="_Title", bd=0)
default_title = Label(app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Prog - Programming Learner", bd=0)

basic_python_button = Button(app, bg=CONSTANTS["GRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Basic Python", bd=0, command=basic_python().function)
printing_button = Button(app, bg=CONSTANTS["LIME"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Printing", bd=0, command=basic_python().printing)
variables_button = Button(app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Variables", bd=0, command=basic_python().variables)
inputting_button = Button(app, bg=CONSTANTS["PURPLE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Inputting", bd=0, command=basic_python().inputting)
operations_button = Button(app, bg=CONSTANTS["ORANGE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Operations", bd=0, command=basic_python().operations)
SUPERCHARGEBASIC_button = Button(app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="SUPER CHARGE KNOWLEDGE", bd=0, command=basic_python().SUPERCHARGE)

basic_types_button = Button(app, bg=CONSTANTS["ORANGE"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Basic Types", bd=0, command=basic_types().function)
integers_button = Button(app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Integers", bd=0, command=basic_types().integers)
strings_button = Button(app, bg=CONSTANTS["LIGHTGREEN"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Strings", bd=0, command=basic_types().strings)
floats_button = Button(app, bg=CONSTANTS["LIGHTPURPLE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Floats", bd=0, command=basic_types().floats)
booleans_button = Button(app, bg=CONSTANTS["PURPLE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Booleans", bd=0, command=basic_types().booleans)
SUPERCHARGETYPES_button = Button(app, bg=CONSTANTS["LIGHTGRAY"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="SUPER CHARGE KNOWLEDGE", bd=0, command=basic_types().SUPERCHARGETYPES)

comparisions_button = Button(app, bg=CONSTANTS["CODECOLOR2"], fg="white", font=(CONSTANTS["CODEFONT"],15,"bold"), text="Comparisions", bd=0, command=comparisions().function)
comparing_strings_button = Button(app, bg=CONSTANTS["AQUA"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Comparing Strings", bd=0, command=comparisions().cstrings)
comparing_integers_button = Button(app, bg=CONSTANTS["GRAY"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Comparing Ints", bd=0, command=comparisions().cints)

conditional_statements_button = Button(app, bg=CONSTANTS["PURPLE"], fg="white", font=(CONSTANTS["CODEFONT"],12,"bold"), text="Conditional Statements", bd=0, command=conditionalstatements().function)
if_statements_button = Button(app, bg=CONSTANTS["BLUE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="If Statements", bd=0, command=conditionalstatements().if_statements)
else_statements_button = Button(app, bg=CONSTANTS["LIGHTPURPLE"], fg="white", font=(CONSTANTS["CODEFONT"],20,"bold"), text="Else Statements", bd=0, command=conditionalstatements().else_statements)

canvas.create_window(200, 275, window=basic_python_button)
canvas.create_window(200, 375, window=basic_types_button)
canvas.create_window(200, 475, window=comparisions_button)
canvas.create_window(400, 275, window=conditional_statements_button)
canvas.create_window(400, 100, window=default_title)
canvas.create_window(400, 135, window=minecraftripoff)
canvas.create_window(100, 30, window=main_update_log)

canvas.pack()

app.mainloop()