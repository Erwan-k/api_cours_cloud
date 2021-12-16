from flask_restful import Api, Resource, reqparse



personnes_post_args = reqparse.RequestParser()
personnes_post_args.add_argument("nom",type=str,required=True)
personnes_post_args.add_argument("prenom",type=str,required=True)
personnes_put_args = reqparse.RequestParser()
personnes_put_args.add_argument("nom",type=str,required=True)
personnes_put_args.add_argument("prenom",type=str,required=True)
personnes_delete_args = reqparse.RequestParser()
personnes_delete_args.add_argument("nom",type=str,required=True)

liste_personnes = [{"nom":"Kerbrat","prenom":"Erwan"}]

class personnes(Resource):
	def get(self): #s_inscrire
		global liste_personnes
		return liste_personnes
	def post(self):
		global liste_personnes
		body = personnes_post_args.parse_args()
		[nom,prenom] = [body[i] for i in body]

		liste_personnes += [{"nom":nom,"prenom":prenom}]

		return {"retour":"ok"}
	def put(self):
		global liste_personnes
		body = personnes_put_args.parse_args()
		[nom,prenom] = [body[i] for i in body]

		for i in range(len(liste_personnes)):
			if liste_personnes[i]["nom"] == nom:
				liste_personnes[i]["prenom"] = prenom

		return {"retour":"ok"}
	def delete(self):
		global liste_personnes
		body = personnes_delete_args.parse_args()
		[nom] = [body[i] for i in body]

		indice = -1
		for i in range(len(liste_personnes)):
			if liste_personnes[i]["nom"] == nom:
				indice = i
		if indice == -1:
			return {"retour":"ok","detail":"personne non trouvée"}
		else:
			liste_personnes.pop(indice)
			return {"retour":"ok"}



