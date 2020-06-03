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

`python manage.py insert --name "Amit Shah" --timezone " Africa/Abidjan"  --activityperiod "[{'start_time': 'Feb 1 2020  1:33PM','end_time': 'Feb 1 2020 1:54 PM'}]"`

# Demo
https://aqueous-beyond-40132.herokuapp.com/

# Instructions

Please change your SECRET_KEY in settings.py file to run on localserver: 
SECRET_KEY = 'gu5tw4#b^asc387g(8!5=4tj1zlnzufc_2u7w4-p!&&=yx2y8e'
and comment the below line:
#SECRET_KEY= os.environ.get("SECRET_KEY")

