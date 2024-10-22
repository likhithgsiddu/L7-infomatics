import sqlite3
import os

DB_PATH = os.path.join('db', 'database.db')

# Database setup
def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            season TEXT NOT NULL
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flavor_suggestion TEXT,
            allergy_concerns TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Add seasonal flavor
def add_seasonal_flavor(name, description, season):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO seasonal_flavors (name, description, season)
        VALUES (?, ?, ?)
    ''', (name, description, season))
    
    conn.commit()
    conn.close()

# List seasonal flavors
def list_seasonal_flavors():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM seasonal_flavors')
    flavors = cur.fetchall()
    
    conn.close()
    
    return flavors

# Add ingredient to inventory
def add_ingredient(name, quantity, unit):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO ingredient_inventory (name, quantity, unit)
        VALUES (?, ?, ?)
    ''', (name, quantity, unit))
    
    conn.commit()
    conn.close()

# List ingredients
def list_ingredients():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM ingredient_inventory')
    ingredients = cur.fetchall()
    
    conn.close()
    
    return ingredients

# Add customer suggestion
def add_customer_suggestion(name, flavor_suggestion, allergy_concerns):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO customer_suggestions (name, flavor_suggestion, allergy_concerns)
        VALUES (?, ?, ?)
    ''', (name, flavor_suggestion, allergy_concerns))
    
    conn.commit()
    conn.close()

# List customer suggestions
def list_customer_suggestions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM customer_suggestions')
    suggestions = cur.fetchall()
    
    conn.close()
    
    return suggestions

if _name_ == '_main_':
    create_tables()
    print("Database and tables created successfully.")
