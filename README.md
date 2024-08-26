# IPL Auction Game

## Overview

The IPL Auction Game is a web-based application designed to simulate an IPL player auction. It consists of a Django backend to manage the player and team data, and a Flask frontend to handle user interactions. Each team starts with a budget of 100 million and can bid for players based on their skills and expertise levels.

## Project Structure

- **Django Backend (`ipl_auction`)**:
  - Manages the database and provides APIs for player and team data.
  - Uses `auction` app for auction-related functionalities.
  
- **Flask Frontend (`flask_app`)**:
  - Provides the user interface for teams to view players and place bids.
  - Interacts with the Django backend via API requests.

## Installation

### Prerequisites

- Python 3.8+
- Django
- Flask
- Requests library for Flask

Usage
Access the Django Admin:

Open your browser and go to http://127.0.0.1:8000/admin.
Log in with the superuser credentials you created.
Add teams and players through the Django admin interface.
Use the Flask Frontend:

Open your browser and go to http://127.0.0.1:5000.
View the list of teams and their budgets.
Click on a team to see details of its players.
Place bids on players by entering the player ID and bid amount.
File Descriptions
Django Project (ipl_auction):

ipl_auction/settings.py: Configuration settings for the Django project.
ipl_auction/urls.py: URL routing for the Django project.
auction/models.py: Defines the database models for teams and players.
auction/views.py: Handles the API endpoints for teams and players.
auction/admin.py: Registers models with the Django admin site.
Flask Project (flask_app):

app.py: Main application file for the Flask frontend.
templates/index.html: Template for displaying teams.
templates/team_detail.html: Template for displaying team and player details.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.
