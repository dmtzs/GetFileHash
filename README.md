# Instructions for the correct execution of the FileHash application

If you want to run the app with terminal you need to have python 3 or later versions, this app works on windows only and the libraries you will need are the next ones:

## Python libraries:
* Run the next command in order to install the other python libraries: pip install -r requirements.txt
<br>
The rest of the libraries comes with python from default, if not please reply to me in order to add that prerequisities.

## Then you run the program with the next command: 
python PrincipalHash.py

## Finally
Follow the instructions that appears in the same program.
<br>
In the case of the route for the Excel file that the program will take like input data you just need to put the route where that excel file is located, but-<br>
before this step you need first to fill the Excel file that the program will take as an input data, the instructions for this Excel below.<br>

## Excel file instructions
Here we are going to describe how to prepare the excel file in order to be used by the program to be executed in the correct way. The steps are:
* From cell A1 onwards are for write the ID of the requirement.
* From the cell B1 onwards are for write the general description of the requirement.
* From the cell C1 onwards are for write a sub description if its the case or if its necessary.
* From the cell D1 onwards is just a formula that comes from the first cell that this formula was written and you just need to apply teh formula for all other cells according to the number of requirements you have.
* The cell E2 is for write the path in which all the evidences which we need to get the hash are stored. This path should be written just once in the E2 cell.
* The cell F2 you need to write the word "All" if you want to get the hash of all files or if you want just a type of file in specific then write the extension, for example: .txt, .xlsx, .docx, .pptx, etc. This word should be written just once in the F2 cell
* The cell G2 is for specifying the path in which the word file will be created. This path should be written just once in the G2 cell.
* The cell H2 is for specifying a title for the word file, if you left empty then the program will not write any title.
* The I2 cell is something I´m still implementing in order to use the same file for multiple audits.

## Testing functions
Im using pytest in order to create this testing scripts so every time that we do a change we can test or modify the test script in order to proove that we comply with functionality.
<br>
For running the tests please run the next command: pytest test_app.py -v

# The program is complete