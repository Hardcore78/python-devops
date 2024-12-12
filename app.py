#importation des bibliotheques
from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr
app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():

# attribution des donnes au variable pour simplifier le calcul
        data = request.get_json()
        hau = data.get('height')  
        poi = data.get('weight')
# appel de la focntion et je met dedans les variables du json 
        resultat = calculate_bmi(hau, poi)
#renvoi du resultat de la fonction 
        return jsonify({"bmi": resultat})


@app.route('/bmr', methods=['POST'])
def bmr():

#recuperation des donnés du json
        data = request.get_json()
        hau2 = data.get('height')  
        poi2 = data.get('weight')  
        age = data.get('age')  
        genre = data.get('gender')

# appel de la fonction avec les varaible pour plus de simpliciter 
        resultat2 = calculate_bmr(hau2, poi2, age, genre)
        #renvoi du resultat de la fonction 
        return jsonify({"bmr": resultat2})
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
