# Installation
`pip install django`

`virtualenv env`

# For Mac/ Linux
`source env/bin/activate`

# For Window
`env\scripts\activate`



`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

# For creating Dummy data using command-line
`python manage.py insert -n "Narandre Modi" -tz " Africa/Abidjan"  --activityperiod "[{'start_time': 'Feb 1 2020  1:33PM','end_time': 'Feb 1 2020 1:54 PM'},{'start_time': 'Feb 1 2020  1:39PM','end_time': 'Feb 1 2020 1:54PM'}]"`
or
`python manage.py insert --name "Amit Shah" --timezone " Africa/Abidjan"  --activityperiod "[{'start_time': 'Feb 1 2020  1:33PM','end_time': 'Feb 1 2020 1:54 PM'}]"`


