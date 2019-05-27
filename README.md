MCyver maze game
=================                                                                       
Why this program? 
-----------------                                                                    
This game is a 2D labyrinth in which MacGyver has been locked up. The exit is supervised by a bodyguard whose hair would turn Tina Turner pale. To distract, you need to gather the following elements (scattered in the labyrinth): a needle, a small plastic tube and ether. They will allow MacGyver to create a syringe and lull the guard to go out of the labyrinth. The technical library used Pygame. This game is a practical application of the Openclassrooms App Developer in Python course. The skills mobilized:                                                                                
                                                                                              
* Read and understand a module documentation                                        
* Manage different versions of Python and its modules according to projects         
* Create scripts for the web using Python                                          
* Use an algorithm to solve a technical need                                       
* Code effectively using the right tools                                          
* Conceptualize the whole of its application by describing its structure (Entities / Domain Objects) 

How does it work ? 
-------------------
To start use **clone or download** button on github and **Download ZIP** on your computer, or copy HTTPS link and use the terminal on your computer and type : 
```
$ git clone https://github.com/GuillaumeStaub/McGyverMaze.git
```
Check if python 3 is installed on your machine. For this, open the terminal and type : 
```
$ python3 -V
```
You have to get something like : 
```
Python 3.X.X
```
If python is not installed on your machine go to the site: [https://www.python.org](https://www.python.org), download **Python 3.X.X** and follow the instructions. 

If you are Linux user you can install Python from the console with the command : `$ sudo apt-get install python3`

If you are MacOS user you can use [MacPorts](https://www.macports.org) and install Python from the terminal with the command : `$ sudo port install python3`

Or you can use too [HomeBrew](https://brew.sh) from the terminal with the command : `$ brew install python3`

### ![windows](https://img.icons8.com/color/48/000000/windows-logo.png) For Windows users :

1. Open the console and navigate to the root of the project McGyverMaze with the commande `$ cd\...\McGyverMaze`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip install pipenv`
3. To start the game with GUI with Pygame type the following command from the root of the project : 
```
$ pipenv run python home.py
```
4. To start the game with Terminal Interface type the following command from the root of the project : 
```
$ pipenv run python home.py --terminal
```

### ![apple](https://img.icons8.com/dusk/48/000000/mac-os.png) For MacOs users : 

There is a known error between pipenv, pygame and MacOS Mojave. [Error Pygame and MacOS Mojave](https://github.com/pygame/pygame/issues/555)

You can try the same things WIndows users:

1. Open the console and navigate to the root of the project McGyverMaze with the commande `$ cd\...\McGyverMaze`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip3 install pipenv`
3. To start the game with GUI with Pygame type the following command from the root of the project : 
```
$ pipenv run python home.py
```
4. To start the game with Terminal Interface type the following command from the root of the project : 
```
$ pipenv run python home.py --terminal
```

If you get a similar screen for the pygame version:
![Pygame Error](https://zupimages.net/up/19/22/orl6.png)

Follow the following instructions:

1. Open the console and navigate to the root of the project McGyverMaze with the commande `$ cd\...\McGyverMaze`
2. Create your virtual environement with [venv](https://docs.python.org/3/library/venv.html)
 ```
$ python3 -m venv venv
```
3. Activate your venv environment with:
```
$ source venv/bin/activate
```
4. Install the necessary packages to run the program like Pygame, Click ... This is possible thanks to the requirements file. To do this, run the following command : 
```
$ pip install -r requirements.txt
```
5. Now that all packages are installed run the program with Pygame Interface :
```
$ python home.py
```
6. To start the game with Terminal Interface type the following command from the root of the project : 
```
$ python home.py --terminal
```


### ![linux](https://img.icons8.com/color/48/000000/linux.png) For Linux  or other Unix users :
1. Open the Terminal and navigate to the root of the project McGyverMaze with the commande `$ cd\...\McGyverMaze`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip install pipenv`
3. To start the game with GUI with Pygame type the following command from the root of the project : 
```
$ pipenv run python home.py
```
4. To start the game with Terminal Interface type the following command from the root of the project : 
```
$ pipenv run python home.py --terminal
```

Contribute to the program
--------------------------                                                            
                                                                                              
* Fork it                                                                           
* Create your feature branch (git checkout -b my-new-feature)                             
* Commit your changes (git commit -am 'Add some feature')                                 
* Push to the branch (git push origin my-new-feature)                                     
* Create new Pull Request                                                              