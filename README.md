# Game Backlog

Game Backlog is a site to compile a list of games that you have yet to play or want to play again.

## Live Project

[View Game Backlog here.](https://game-backlog-a79ad4905aa8.herokuapp.com/)

## User Experience 

- ### User Stories

- #### First Time Visitor Goals

    1. As a first time visitor, I want to be able to register for an account.
    2. As a first time visitor, I want to be able to easily navigate the site.
    3. As a first time visitor, I want to be able to view the website on any device.

- #### Returning Visitor Goals

    1. As a returning visitor, I want to be able to log in to my account.
    2. As a returning visitor, I want to be able to see what games have been added by non registered users
    3. As a returning visitor, I want to be able to edit and delete games and genres.

- #### Frequent Visitor Goals

    1. As a frequent visitor, I would like to see my own list of games added.
    2. As a frequent visitor, I would like my list to be only visible to me.

- ### Design
    - #### Colour Scheme
        - The main colours of the website are yellow/orange and dark pink. This is just to give an overall lighthearted feel to the list.

## Features
### Existing Features

- __Home Page__
  - The homepage is where you are welcomed to the site and have access to login or register.

  ![homepage](docs/homepage.png)

- __Nav Bar__
  - The navbar has links to the other pages of the website for easy navigation.

  ![navbar](docs/navbar.png)  
  ![navbar_small](docs/navbar_small.png)

- __Dashboard__

    - The dashboard displays when a user is logged in and gives an error message when logged out.

    ![dashboard](docs/dashboard.png)  

    ![dashboard_loggedout](docs/dashboard_loggedout.png)

- __Games Page__
    - The games page shows a dropdown of the games added to website, their genre, description and release date entered by users.
    These are able to be edited and deleted.

    ![games](docs/games.png)
  
- __Modal__
  - The modal pops up when you try to delete a game or genre to double check and confirm your input.

  ![modal](docs/modal.png)

-__Add Game Page__
  - This page is where the user enters information about the new game they are adding to the backlog, including the title, a description and release date etc.

  ![add_game](docs/add_game.png)

- __Genre Page__
  - This page displays all the genres that have been added to the backlog, the games added are then stored under their respective genre chosen.

  ![genres](docs/genres.png)

## Future Features

 - I would like to add each individual users entered games into their own backlog list that will be displayed on the logged in users dashboard. They can then edit this list from within the dashboard menu.

 - From the users dashboard it would be nice if there was an option to only display the favourited games or perhaps games from only a specific genre chosen.

 - Currently there are no messages to show an error when a duplicate of a game or genre is input into the database, as it stands the user is just redirected to the respective page with no changes applied.

 - As of now, you have to choose a genre from the existing dropdown menu when adding a game. This means the genre has to be created first before adding a game. It would be better if you could enter a genre while adding a game and then the genre data would be added to the database list.

## Testing

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/). This was done for every html page created.
    ![html_check](docs/html_check.png)

- Accessibility
  - This was checked using the free tool on this [site](https://pagespeed.web.dev/)
  ![access_mob](docs/access_mob.png)  
  ![access_desk](docs/access_desk.png)

## Known Bugs
 - When on mobile/tablet the select menu to choose a genre when adding or editing a game does not always set the right value when clicked, however this seems to work fine on desktop.

## Credits
 * Majority of code was used from the code institute walkthrough project
 * Materialize CSS was used for the style of the web pages
 * Font awesome was used to display icons on buttons and forms
 * User authentication was learnt from the following [Youtube video](https://www.youtube.com/watch?v=t9zA1gvrTvo&t=10s)