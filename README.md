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
## API Highlights
1. **I decided to split my RESTFul API into two micro-services because I assume that votes and polls table will be linked by a link table. Many smaller tables instead of big tables for speed.** 
   * Poll Class that specifically deals with the poll database tables.
   * Vote Class that specifically deals with the votes databas tables.
![alt text](db.png)

2. **I decided to create an abstract class called data source to follow the dependency inversion principle of SOLID. This class was not used due to the project scope but I feel it is good to demonstrate.**
   * There maybe many types of databases so therefore API couples with abstract class.
   * The connection of database, exectuing querying and even searching is then done within the database class NOT the micro-service classes.
 ![alt text](poll_ms.png)

3.**I also created an abstract class for graphs as there could be a lot of different types of graphs implemented. A concrete class for horizontal bar chart was used in the project**
  * This allows encapsulation of graph tweaking away from everything else.

4.**Within the API Vote class I added a constructor that is a list. This list then appends any POST resources carried out and therefore now the POST resource is in memory.** 
  * Within the API terminal you can see that when POST vote is used up, the in memory json file count updates to whatever the user has inputed. This is automatically printed in the API terminal.

![alt text](vote_ms.png)

## Web  App Highlights
1.**If no selection is submitted, clicking the submission button will reload vote page and not trigger any API call**
2.**Graph used is a fully interactive graph** 
3.**All HTML elements are sized to viewport for better device scaling**


  

