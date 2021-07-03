Python version: "Python 3.9.6"

install venv: python install venv venv

activate venv: venv\\Scripts\\activate

import requirements.txt: pip install -r requirements.txt

run server: python manage.py runserver
