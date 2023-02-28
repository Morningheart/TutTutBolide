Lancer le projet avec la commande :
python manage.py runserver 
Sync la database :
python manage.py makemigrations
python manage.py migrate

Query base :
query {
  allIngredients {
    id
    name
  }
}
Query chargetrip :
query vehicleListFilter {
  vehicleList(search: "Audi"){
    id
    naming {
      chargetrip_version
      edition
      make 
      model
      version
    }
    # add more fields here
  }
}