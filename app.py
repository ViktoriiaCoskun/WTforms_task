from flask import Flask, jsonify, render_template, request,Response
from models import booklibrary
from flask import abort
from flask import make_response
from forms import UpdateForm,GetBookByID,DeleteForm,CreateNew

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/searchbyid")
def searchbyid():
    form = GetBookByID()
    form.method.default="GET"
    return render_template("books.html", form=form)

@app.route("/update")
def update():
    form = UpdateForm()
    form.method.default="PUT"
    return render_template("books.html", form=form)

@app.route("/delete")
def delete():
    form = DeleteForm()
    form.method.default="DELETE"
    return render_template("books.html", form=form)

@app.route("/new")
def newBook():
    form = CreateNew()
    form.method.default="POST"
    return render_template("books.html", form=form)

@app.route("/", methods=["GET"])
def home():
    return render_template("Home.html")


@app.route("/allBooks", methods=["GET"])
def allBooks():
    return jsonify(booklibrary.all())

@app.route("/api/v1/booklibrary/", methods=["GET"])
def home_api():
  book_id = request.args.get("id")
  if book_id :
    if request.args.get("button") == 'delete':
      return delete_todo(int(book_id))
    elif request.args.get("button") == 'update':
      return update_todo(int(book_id))
    elif request.args.get("button") == 'search':
      return get_todo(int(book_id))
  elif request.args.get("button") == 'create':
    return create_todo()  
  else : return jsonify(booklibrary.all())


@app.route("/api/v1/booklibrary/", methods=["POST"])
def create_todo():
  if request.args:
    data= {
        'id': booklibrary.all()[-1]['id'] + 1,
        'author': request.args.get('author'),
        'country': request.args.get('country'),
        'imageLink': request.args.get('imageLink'),
        'language': request.args.get('language'),
        'pages': request.args.get('pages'),
        'title': request.args.get('title'),
        'link': request.args.get('link'),
        'year': request.args.get('year')
        }
    booklibrary.create(data)  
    return jsonify({'todo': data}), 201  
  elif not request.json or not 'title' in request.json:
    abort(400)
  else:
    todo = {
      'id': booklibrary.all()[-1]['id'] + 1,
      'author': request.json['author'],
      'country': request.json['country'],
      'imageLink': request.json['imageLink'],
      'language': request.json['language'],
      'pages': request.json['pages'],
      'title': request.json['title'],
      'link': request.json['link'],
      'year': request.json['year']
    }
    booklibrary.create(todo)
  return jsonify({'todo': todo}), 201

@app.route("/api/v1/booklibrary/<int:book_id>", methods=["GET"])
def get_todo(book_id):

  todo = booklibrary.get(book_id)
  if not todo:
    abort(404)
  return jsonify({"todo": todo})

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
  return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)



@app.route("/api/v1/booklibrary/<int:book_id>", methods=['DELETE'])
def delete_todo(book_id):
  result = booklibrary.delete(book_id)
  if not result:
    abort(404)
  return jsonify({'result': result})

@app.route("/api/v1/booklibrary/<int:book_id>", methods=["PUT"])
def update_todo(book_id):
  todo = booklibrary.get(book_id)
  if not todo:
    abort(404)
  if request.args:
      todo = {
        'id': request.args.get('id', todo['id']),
        'author': request.args.get('author', todo['author']),
        'country': request.args.get('country', todo['country']),
        'imageLink': request.args.get('imageLink', todo['imageLink']),
        'language': request.args.get('language', todo['language']),
        'pages': request.args.get('pages', todo['pages']),
        'title': request.args.get('title', todo['title']),
        'link': request.args.get('link', todo['link']),
        'year': request.args.get('year', todo['year'])
      }
      booklibrary.update(book_id, todo)
      return jsonify({'todo': todo})
  elif not request.json:
     abort(400)
  data = request.json
  if any([
    'link' in data and not isinstance(data.get('link'), str),
    'author' in data and not isinstance(data.get('author'), str),
    'country' in data and not isinstance(data.get('country'), str),
    'imageLink' in data and not isinstance(data.get('imageLink'), str),
    'language' in data and not isinstance(data.get('language'), str),
    'pages' in data and not isinstance(data.get('pages'), int),
    'title' in data and not isinstance(data.get('title'), str),
    'year' in data and not isinstance(data.get('year'), int)
  ]):
    abort(400)
  todo = {
    'id': data.get('id', todo['id']),
    'author': data.get('author', todo['author']),
    'country': data.get('country', todo['country']),
    'imageLink': data.get('imageLink', todo['imageLink']),
    'language': data.get('language', todo['language']),
    'pages': data.get('pages', todo['pages']),
    'title': data.get('title', todo['title']),
    'link': data.get('link', todo['link']),
    'year': data.get('year', todo['year'])
  }
  booklibrary.update(book_id, todo)
  return jsonify({'todo': todo})


if __name__ == "__main__":
  app.run(debug=True)
