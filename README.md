# techtest2_pollapi

# Introduction
 My submission for a tech test to produce a web application with a RESTful API in limitied scope.  
## Requirements 
**Web Application**:
1. **Voting page:**  
   a. To get poll.  
   b. Display poll options.  
   c. Allows user to select and submit a vote.  
      i. Highlights option selected.  
     ii. Selection check before submitting.  
3. **Confirmation page**    
   a. Show thank you message.  
   b. Display percentage of votes for the options.  
       i. Results order in descending.  
      ii. Percentages should have no decimals  

**RESTful API**
1. GET poll to be displayed.  
2. POST a vote of what option user has selected.  
3. GET votes for a poll by poll's id.

# How to Run and Folder and File Structure 
## Main Folder Structure  
* Classes# Contains all internal classes and functions created for project.
   * /abstract_classes.py # Contains abstract classes for project.
   * /utility.py # Contains all concrete classes or utility functions.
* Resources # Contains example json.
* Static #Contains css and images.
* templates # contains hmtl files
* tests/ Contains test files
  * /test_polls_api.py # tests for polls micro-controller.
  * /test_utility.py # tests for concrete classes and utility functions.
  * /test_votes_api.py # tests for votes micro-controller.
* requirements.txt #text file for needed libraries.
* **api.py** The Restful API driver file.
* **webapp.py** The web application driver file.  

## How to Run Project##
1. Install libraries in the **requirements.txt** using pip in VSC.
2. In one terminal type **python api.py**. You need to run API first before web app.
3. In a new terminal type **python webapp.py**. Then click on the server to automatically open up a browser.

## How to Run Tests ##
1. In one terminal type **python api.py**. You need to run API so you can test it.
2. Run all tests type in the same terminal type **pytest -svv**.

# My Implementation



