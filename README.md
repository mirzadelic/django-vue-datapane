# django-vue-datapane

## Install

### Backend:
```sh
cd backend/
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
```

### Frontend:
```sh
cd frontend/
npm i
```

## Run

Open two terminals.

Terminal 1:
```sh
cd frontend/
npm run serve
```

Terminal 2:
```sh
cd backend/
source venv/bin/activate
python manage.py runserver
```

Go to: http://localhost:8000/
