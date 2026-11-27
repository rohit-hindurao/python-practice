A variable is a name that refers to a value stored in memory. Variables are created using the assignment operator (=).

The print() function outputs to the screen. It’s a variadic function: accepts any number of arguments.

When you run python3 file.py, Python doesn't run your text directly. It goes through steps:
your code (text) → tokens → AST (tree) → BYTECODE → interpreter runs it
Bytecode is a list of small, simple instructions, like a recipe the Python interpreter follows step by step.