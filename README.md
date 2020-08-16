# Decisions.io
A framework builder to help you quantify and compare options in decisions.

## Setup
### Backend
Start the flask application with `cd backend && ./bootstrap` . This will set up the database.
To insert the sample data, run `python db/add_test_entries.py`.
### Frontend
`cd frontend && ng serve`

## References
+ Basic Tutorial for Flask + Angular app - https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/
+ Trees in DB - https://iamcam.wordpress.com/2006/03/24/storing-hierarchical-data-in-a-database-part-2a-modified-preorder-tree-traversal/
+ ORM - https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases
+ Angular Example Project - https://stackblitz.com/angular/emaeglreoro?file=src%2Fapp%2Fhero-detail%2Fhero-detail.component.css
