# Telegram Bot Portfolio
### 1.  Description

- This Telegram bot serves as a communication hub between a service provider (Tatyana Mogoryan) and potential clients.
It offers information about services, showcases a portfolio, provides contact information, collects client contact details, and allows for exporting user data (for the bot creator).

- Key Features
    * Greets users and introduces Tatyana Mogoryan's services.
    * Provides a list of services with details upon request.
    * Offers links to various contact methods for Tatyana Mogoryan.
    * Collects client names and surnames for later communication.
    * Exports user data to a text file (restricted to the bot creator).


### 2. How to translate and run the program ?

- Install Required Libraries: Use the command
    ````c
    pip install telebot sqlite3
    ````

- Run and compile the program using the command
    
    ````c
    python main.py
    ````

### 3. How the program is programmed?

- Libraries:
    * telebot: Enables interaction with the Telegram Bot API.
    * sqlite3: Facilitates interaction with a SQLite database to store user data.
    * webbrowser: Opens web pages in the user's default browser.
    * time: Manages time-related actions (e.g., delays).

- Key Programming Concepts:
    * Decorators to handle specific commands.
    * Inline keyboards for interactive elements.
    * Callback queries for responding to button clicks.
    * Database operations for storing and retrieving user information.


### 4. Links to source code and websites that were used in the solution

-   [Telegram Bot API](https://core.telegram.org/bots/api)
   
-   [Telebot Library](https://github.com/topics/telebot)

-   [SQLite](https://docs.python.org/3/library/sqlite3.html)


