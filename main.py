import requests
import json

token = '0c5ab349fdca8adbd851961556b6c646'
responce = requests.post('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token': token}, json={
   "name": "Бульбазаврик",
   "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"   
})

print(responce.text)

responce_put = requests.put('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token': token}, json={
    'pokemon_id': 2997,
   "name": "Бульба",
   "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"   
})

print(responce_put.text)



responce_post = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',headers={'trainer_token': token}, json={
    'pokemon_id': 2997
   
   
 })

print(responce_post.text)