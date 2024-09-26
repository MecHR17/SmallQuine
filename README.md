Python Quine Code that operates as specified in Sipser's Introduction to ToC book.

A outputs code of <B,T>
B uses <B,T> to get its own code, then figures out <A> from it
B combines these descriptions as <A,B,T> to get <SELF>, which is its own code
T can then go on to compute with <SELF>, such a printing it out or calculating its own length

There is also "quineMaker.py" that constructs a quine from only <T>
"quineMaker.py" takes in "quineInput.py" as input and outputs "quineOutput.py"
The first line in "quineInput.py" is for setting "self_code" to a random value
The standard rules apply. Backslashes and triple quotes are not permitted.