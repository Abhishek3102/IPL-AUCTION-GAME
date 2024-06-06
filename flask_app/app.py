from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

DJANGO_API_URL = 'http://localhost:8000'

@app.route('/')
def index():
    response = requests.get(f'{DJANGO_API_URL}/teams/')
    teams = response.json()
    return render_template('index.html', teams=teams)

@app.route('/team/<int:team_id>')
def team_detail(team_id):
    response = requests.get(f'{DJANGO_API_URL}/teams/{team_id}/')
    team = response.json()
    return render_template('team_detail.html', team=team)

@app.route('/bid', methods=['POST'])
def bid():
    team_id = request.form['team_id']
    player_id = request.form['player_id']
    amount = request.form['amount']

    response = requests.post(f'{DJANGO_API_URL}/bid/', data={
        'team_id': team_id,
        'player_id': player_id,
        'amount': amount
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
