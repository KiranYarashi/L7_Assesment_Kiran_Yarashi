from flask import Flask, render_template, request, redirect, url_for, flash
from sqlite3 import Error
from main import FictionalChocoHouse

app = Flask(__name__)
app.secret_key = "d4d68adfc046579d752916505b72d581"

db = FictionalChocoHouse()

# HOME route
@app.route('/')
def index():
    flavours = db.get_all_flavours()
    ingredients = db.get_all_ingredients()
    suggestions = db.get_all_suggestions()
    return render_template('index.html', flavours=flavours, ingredients=ingredients, suggestions=suggestions)

# Route to add new flavour
@app.route('/add_flavour', methods=['POST'])
def add_flavour():
    name = request.form['name']
    description = request.form['description']
    is_seasonal = 1 if request.form.get('is_seasonal', 'off') == 'on' else 0
    season = request.form['season'] if is_seasonal else None
    db.add_flavour(name, description, is_seasonal, season)
    flash('Flavour added successfully!')
    return redirect(url_for('index'))

# Route to delete flavour
@app.route('/delete_flavour', methods=['POST'])
def delete_flavour():
    flavour_id = request.form['flavour_id']
    db.delete_flavour(flavour_id)
    flash('Flavour deleted successfully!')
    return redirect(url_for('index'))

# Route to add new ingredient
@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    unit = request.form['unit']
    allergen_info = request.form.get('allergen_info')
    db.add_ingredient(name, quantity, unit, allergen_info)
    flash("Ingredient added successfully")
    return redirect(url_for('index'))

# Route to delete ingredient
@app.route('/delete_ingredient', methods=['POST'])
def delete_ingredient():
    ingredient_id = request.form['ingredient_id']
    db.delete_ingredient(ingredient_id)
    flash('Ingredient deleted successfully!')
    return redirect(url_for('index'))

# Route to update ingredient quantity
@app.route('/update_ingredient_quantity', methods=['POST'])
def update_ingredient_quantity():
    ingredient_id = request.form['ingredient_id']
    new_quantity = request.form['new_quantity']
    db.update_ingredient_quantity(ingredient_id, new_quantity)
    flash('Ingredient quantity updated successfully!')
    return redirect(url_for('index'))

# Route to add a customer suggestion
@app.route('/add_suggestion', methods=['POST'])
def add_suggestion():
    flavour_name = request.form['flavour_name']
    description = request.form['description']
    allergen_concerns = request.form.get('allergen_concerns')
    db.add_suggestion(flavour_name, description, allergen_concerns)
    flash('Suggestion added successfully!')
    return redirect(url_for('index'))

# Route to update suggestion status
@app.route('/update_suggestion/<int:suggestion_id>', methods=['POST'])
def update_suggestion(suggestion_id):
    new_status = request.form['status']
    db.update_suggestion_status(suggestion_id, new_status)
    flash('Suggestion status updated!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    db = FictionalChocoHouse()
    print("Starting the flask application!")
    app.run()
