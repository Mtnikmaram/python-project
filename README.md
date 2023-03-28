![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


<h1>Batlleship Game!</h1>
<p>This project is a battleships game that is run and played within the terminal. The system runs on a mock terminal through <a href="https://www.heroku.com/" target="_blank">Heroku</a>
The aim of the game is to destroy the computers battleships by guessing where on a grid their battleships are and firing upon them before the computer finds and destroys all yours first.</p>

click here to play the game: <a href="https://terminal-battleships-game.herokuapp.com/" target="_blank">Battleship Game</a>
<br><br>

![image](https://user-images.githubusercontent.com/72948843/145606585-ccd414af-14ba-4f99-8a72-54d61ef08bc9.png)

# Contents

* [**Game Rules**](<#Game-rules>)
    * [How to Play](<#How-to-play>)
* [**Features**](<#features>)
    * [future Features](<#future-features>)
* [**Testing**](<#testing>)
    * [Bugs](<#bugs>)
    * [Solved Bugs](<#solved-bugs>)
    * [Validation Testing](<#validation-testing>)
* [**Technologies Used**](<#technologies-used>)
* [**Deployment**](<#deployment>)
    * [Deployment of the project](<#deployment-of-the-project>)
    * [Cloning of the project](<#cloning-of-the-project>)
* [Credits](<#Credits>)
* [**Acknowledgements**](<#acknowledgements>)


# Game Rules

## How to Play
The rules to the game are very straight forward and are as follows as breifly explained above. From the outset, in this version of the game the user will be prompted for their name who will take on the computer.

The game will generate a random board with the battleships placed for both the computer and human players.

The player will be able to see their ships marked with a '$' sign on their board whilst the other board will computer's pieces will remain hidden from the human user.

Hit ships will be marked with a '@' whilst missed targets will show a 'X'.

The user and the player both take turns to hit one anothers ships by taking guesses to where they are on the board by giving a grid coordanate that fits the board size.

The winner of the game is the player who wins sinks all the opposing players battleships first.


[Back to Top](<#contents>)
<br>

# Features
<hr>

## Existing Features

Upon starting the game, the game will read you the rules and give the player the a chance to enter their name and play as themselves.

![image](https://user-images.githubusercontent.com/72948843/145609400-1e5f22a0-9569-40b0-9130-ac0b056dc3fc.png)

Once you are in the game will then generate some information regarding the game that will be useful to the player, i.e how many ships and the board size.
The game generates the ships for the game randomly.

![image](https://user-images.githubusercontent.com/72948843/145609544-238e4080-b8fe-49ee-a139-fac93dbf5b77.png)


<ul>
    <li>This will generate two boards, The player's board and the computers board.</li>
    <li>The number of ships specified will be randomly placed  on the board as the game starts up.</li>
    <li>You can see where all the players ships are marked on the board, but the ships on the enemy's board remains hidden.</li>
</ul>

![image](https://user-images.githubusercontent.com/72948843/145608810-98067079-0210-4669-b2be-e4da32a8d0cf.png)

<ul>
    <li>You play against the computer to take turns trying to sink each others ships.</li>
    <li>The game requires user inputs to make guesses to find and destory the ships.</li>
    <li>The game keeps track of the scores and will signify a winner when all ships are sunk.</li>
</ul>
<li>Input Validation and checking</li>
<ul>
    <li>You cannot enter letters or floats or negative numbers as inputs.</li>
    <li>You cannot input values greater than the size of the board.</li>
    <li>You cannot enter co-ordinates that have already been guessed before.</li>
</ul>

![image](https://user-images.githubusercontent.com/72948843/145610133-06fb4731-4858-4465-9e75-438c6909279c.png)

<li>Turn counter</li>
<ul>
    <li>The turn counter returns the ammount of shots fired to win the game at the end of the game.</li>
    <li>It returns a positve feedback message to the player based on how well you performed based on the ammount of shots fired.</li>
</ul>

<li>The data is maintained in class instances</li>
<br>
    
[Back to Top](<#contents>)

### Future Features 

<li>Allow the players to select the size of the board and how many battleships there can be.</li>
<li>Allow the player to position the ships themselves.</li>
<br>

[Back to Top](<#contents>)
<br>

# Testing

To test my project, I have manually tested the project by doing the following:

![image](images/CI%20Python%20Linter.png)

[Back to Top](<#contents>)
<br>

## Bugs

 <p> I had trouble for the validate cordinate </p>

[Back to Top](<#contents>)
<br>

## Technologies Used

<li><a href="https://github.com/" target="_blank">GitHub</a> - The site was used to edit and host the website.</li>
<li><a href="https://www.python.org/" target="_blank">Python</a> - This was used in the production to get the game running as it is required for the app to run.</li>
<li><a href="http://pep8online.com/" target="_blank">pep8online</a> - This site was used to validate the python code to check for any errors within my writing.</li>
<li><a href="https://www.heroku.com/" target="_blank">Heroku</a> - This was used to deploy the game in a mock terminal that allows anyone to play the game online.</li>
<br>

[Back to Top](<#contents>)
<br>

## Deployment

### Deployment of the project

<p> I deployed this game using Heroku which is a container based cloud platform where you can deploy, manage and scale applications. To deploy this project I used the following steps in Heroku:</p>
<li>Fork or clone a copy of this repository.</li>
<li>Log in or create an account in heroku.</li>

![image](https://user-images.githubusercontent.com/72948843/145614236-09b624d2-1201-464e-895e-422e146fce65.png)

<li>click on the button in the right corner to create a new app.</li>

![image](https://user-images.githubusercontent.com/72948843/145615564-0d2ebde1-261f-44f4-b64f-17632f646f0e.png)

<li>inside the app page, go to setting page (underlined in green) and set the buildpacks to "Python" and "Nodejs" in that order (like in the picture below).</li>

![image](https://user-images.githubusercontent.com/72948843/145614557-168c86ac-9a83-4cd9-a1c6-a5dc7ac9dd42.png)

<li>Link the heroku app to the repository.</li>
<li>Go back to the deploy page (underlined in yellow) and you can either choose to manually deploy the site or automatically.</li>
<li>Once it has deployed, it may take a fww minutes to load and you can play the game.</li>

<br>
<p>The link to the page to play the game can be found here - <a href="https://terminal-battleships-game.herokuapp.com/" target="_blank">LINK HERE!!!!</a></p>

<br>

[Back to Top](<#contents>)

<br>

### Cloning of the Project
<hr>
<p>To create a local clone of the project, follow the steps below:</p>
<ol>
    <li>In the GitHub repository, under the repository name there is a code tab., click on the <b>code</b> tab.</li>
    <li>In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.</li>
    <li>Open an IDE of your choosing and run Git Bash.</li>
    <li>Change the current working directory to the location of which you wish to place the cloned repository.</li>
    <li>In the terminal, write <b>Git Clone</b> and then paste in the URL supplied via GitHub from step 2.</li>
    <li>Press enter and your new cloned repository will be created within the desired location.</li>
</ol>
<br>

[Back to Top](<#contents>)
<br>

# Credits

<p>I searched the google for the battel ship game and i have seen a lot projects so i have combind all of them and write my project </p>
<p>I used the help of my mentor for this project</p>

[Back to Top](<#contents>)

## Acknowledgements
The site was completed as a Portfolio 3 Project piece for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), the Slack community, and all at the Code Institute for their help and support. 


[Back to Top](<#contents>)
