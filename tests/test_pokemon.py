import requests
import pytest

def test_status_code():
 responce = requests.get('https://pokemonbattle.me:5000/trainers') 
 assert responce.status_code == 200  

def test_piece_of_body():
 responce = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id': '1778'}) 
 assert responce.json()['trainer_name'] == 'Насмита☺️'