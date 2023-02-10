import json


class Booklibrary:
  def __init__(self):
    try:
      with open("booklibrary.json", "r") as f:
        self.booklibrary = json.load(f)
    except FileNotFoundError:
      self.booklibrary = []

  def all(self):
    return self.booklibrary

  def get(self, id):
    todo = [todo for todo in self.all() if todo['id'] == id]
    if todo:
      return todo[0]
    return []

  def create(self, data):
    self.booklibrary.append(data)
    self.save_all()

  def delete(self, id):
    todo = self.get(id)
    if todo:
      self.booklibrary.remove(todo)
      self.save_all()
      return True
    return False

  def save_all(self):
    with open("booklibrary.json", "w") as f:
      json.dump(self.booklibrary, f)

  def update(self, id, data):
    todo = self.get(id)
    if todo:
      index = self.booklibrary.index(todo)
      self.booklibrary[index] = data
      self.save_all()
      return True
    return False
  
  def convertJson(self,data):
    json_object = json.dumps(data, indent = 1)
    return json_object

booklibrary = Booklibrary()