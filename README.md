<p align="center">
  <!--img width="280" src="https://github.com/dmtzs/ProyectoRaspArduino/blob/master/resources/Imgs/BoaEsmeraldaAppOriginal.png" alt="logo"-->
  <h1 align="center" style="margin: 0 auto 0 auto;">Hash your files</h1>
  <h5 align="center" style="margin: 0 auto 0 auto;">Get the hash of the files that you want in a document</h5>
</p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/dmtzs/GetFileHash">
    <img src="https://img.shields.io/github/contributors/dmtzs/GetFileHash">
    <img src="https://img.shields.io/github/issues/dmtzs/GetFileHash?label=issues">
    <img src="https://img.shields.io/github/stars/dmtzs/GetFileHash">
</p>

# Instructions for the correct execution of the FileHash application

If you want to run the app with terminal you need to have python 3 or later versions, this app works on windows only and the libraries you will need are the next ones:

## Python libraries:
* Run the next command in order to install the other python libraries:
```
pip install -r requirements.txt
```
<br>
The rest of the libraries comes with python from default, if not please reply to me in order to add that prerequisities.

## Then you run the program with the next command: 
```
python PrincipalHash.py
```

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

## Documentation
A documentation with images will be developed with the time in the wiki part of this repository.

## Release
Please download the zip in the release part, that zip will include the exe file of ther application and the folder that you can use in order to test the app.
