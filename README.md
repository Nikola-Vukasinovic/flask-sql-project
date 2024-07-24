# Demo project showcasing Flask app developement with SQLAlechemy
## Simple app using WT Forms, SQLAlchemy ontop SQLite 

### Prerequiesites

Make sure to check out **requirements.txt** file provided in the project.

```pip install -r requirements.txt``` to install all needed packages.

NOTE: Development Python version was 3.6 but note if using VS Code Debugging currently supports >=3.8 versions

### Database setup

Currently folder holds already inited database with two needed tables hooked to corresponding models.

For fresh start feel free to delete **migration** folder and **sql.data** file and reinit with:

```flask db init```
```flask db -m "created new tables"```
```flask db upgrade```

NOTE:

Make sure that you have your environment variable setup for flask app:
```export FLASK_APP=adoption_site.py```
