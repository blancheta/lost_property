# Lost Property

The goal of this project is to help people to submit found objects in a festival.
The staff can see which found objects when helping out attendees claiming for a lost object.

## Create virtualenv

```
python -m venv venv
```

## Activate virtualenv
```
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Create a new user
```
flask create-user admin admin
```

## Run the project
```
flask run
```

## Access the admin
[Admin](http://127.0.0.1:5000/admin)
