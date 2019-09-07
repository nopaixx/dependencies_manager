
# Prepare environment
`virtualenv --python python3.7 venv`

`source venv/bin/activate `

`pip install -r minimal_requirement.txt`

# run install manager with you input file
`python installer.py input_commands.json`

-edit you input_command.json file if need

# you can run test by running
`pytest test`


easy you can ad more test by creating more .json test files

# Improvements!!

-Better error handling

-I have worked with the base to install real dependencies in the library with calls to the system

-More test needed, specially we need mock the system calls for example apt-cache rdepends mysql etc..


# Acknowledgements

I had a good time with the test, I think the architecture is correct, is developed with POO which allows a minimalist development of code and easy to understand.

Thank you for the opportunity, any doubt do not hesitate to contact
