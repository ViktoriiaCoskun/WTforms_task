# WTforms_task
installation of requirements:

python -m pip install requests
pip install email_validator
pip install Flask-WTF

You can use Postman for API testing or from home page(home.html) by using links you can process functionalities. After you run project in DEBUG mode you can easily check functions in code.

Functionalities:

1- To list all books in json format:
    *  from postman you can use http://127.0.0.1:5000/api/v1/booklibrary/ with 'GET' method or
    *  from home page use "All Books" link from menu

2- To get book details by ID in json format: ID must be integer value
    *  from postman you can use http://127.0.0.1:5000/api/v1/booklibrary/<int:book_id> with 'GET' method or
    *  from home page use "Search By Book Id" link from menu. After selecting link you neet to set book id in search form and click seach button.

3- To delete book by ID:
    *  from postman you can use http://127.0.0.1:5000/api/v1/booklibrary/<int:book_id> with 'DELETE' method or
    *  from home page use "Delete" link from menu. After selecting link you neet to set book id in delete form and click on delete button.

4- To update book data:
    *  from postman you can use http://127.0.0.1:5000/api/v1/booklibrary/<int:book_id> with 'PUT' method. You need to put variables of book in json format in body of  request. Select raw and as file type json. Or,
    *  from home page use "Update" link from menu. After selecting link you neet to set all required data to components for updating book and click on update button.

5- To ad new book :
    *  from postman you can use http://127.0.0.1:5000/api/v1/booklibrary/ with 'POST' method. You need to put variables of book in json format in body of  request. Select raw and as file type json. Or,
    *  from home page use "Create New" link from menu. After selecting link you need to set all required data to components for creating book and click on update button. Components are type sensitive. If you put string in integer component it will get error after you run the process.

Json example:
    {
        "id": 8,
        "author": "Jane Austen",
        "country": "United Kingdom",
        "imageLink": "images/pride-and-prejudice.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
        "pages": 226,
        "title": "Pride and Prejudice",
        "year": 1813
    }

* WtfForms are in forms.py file. 
* The functions about data like getting ,updating,deleting or adding new data on json file, are in models.py file
* main interface is home.html
* Forms are viewed in books.html
* booklibrary.json file is to store data.