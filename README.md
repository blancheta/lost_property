# Lost Property

The goal of this project is to help people submit found objects in a festival
Like that the staff can see which objects has been found when other attendees claim an lost object.

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
