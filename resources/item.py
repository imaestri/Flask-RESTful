import sqlite3
from flask_restful import Resource, reqparse
from  flask_jwt import jwt_required
<<<<<<< HEAD
=======
from models.item import ItemModel
>>>>>>> e6bc6ca... commit

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!!"
    )
    
    
    @jwt_required()
    def get(self, name):
<<<<<<< HEAD
        item  = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404
    
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row: 
            return {'item': {'name': row[0], 'price': row[1]}}
                
    def post(self, name):
        if self.find_by_name(name):
=======
        item  = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
  
                
    def post(self, name):
        if ItemModel.find_by_name(name):
>>>>>>> e6bc6ca... commit
            return {'Message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        
<<<<<<< HEAD
        item = {'name': name, 'price': data['price']}
        
        try:
            self.insert(item)
        except:
            return{"message": "An error ocurred inserting the item."}, 500
        
        return item, 201  
    
    @classmethod
    def insert(cls, item):
        
        connection  = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        
        connection.commit()
        connection.close()
        
        
        
=======
        item = ItemModel(name, data['price'])
        
        try:
            item.insert() 
        except:
            return{"message": "An error ocurred inserting the item."}, 500
        
        return item.json(), 201  
     

>>>>>>> e6bc6ca... commit
    def delete(self, name):
        
        connection  = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))
        
        connection.commit()
        connection.close()
        
        return {'message': 'Item deleted'}
      
    def put(self, name):
        data = Item.parser.parse_args()
        
<<<<<<< HEAD
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        
        if item is None:
            try:
                Item.insert(updated_item)
=======
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        
        if item is None:
            try:
               updated_item.insert()
>>>>>>> e6bc6ca... commit
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
<<<<<<< HEAD
                Item.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}, 500
        
        return updated_item
    
    @classmethod
    def update(cls, item):
        
        connection  = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "UPDATE items SET price=? WHERE name=? "
        cursor.execute(query, (item['price'], item['name']))
        
        connection.commit()
        connection.close()
        
        
=======
               updated_item.update()
            except:
                return {"message": "An error occurred updating the item."}, 500
        
        return updated_item.json()
    
>>>>>>> e6bc6ca... commit

class ItemList(Resource):
    
    def get(self):
        connection  = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items "
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
    
        connection.close()
        
        return {'items': items}
    
    