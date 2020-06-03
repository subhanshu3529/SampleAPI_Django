from django.core.management.base import BaseCommand, CommandError
from Test.models import User,ActivityPeriod
import uuid
import pytz
import json
from datetime import datetime

class Command(BaseCommand):
    help = """
    It is used to insert data into the table User and ActivityPeriod
    arguement <name , tz>
    """

    def add_arguments(self, parser):
        parser.add_argument('-n','--name', type=str)
        parser.add_argument('-tz','--timezone', type=str)
        parser.add_argument('-t','--activityperiod',type=str, help ="pass the json using start time and end time in [{'start_time': 'Feb 1 2020  1:33PM', 'end_time': 'Feb 1 2020 1:54PM'}] format")

    def handle(self, **options):

        if(not options['name'].isalpha()):
            raise CommandError("Enter a valid name, the name must contain only alphabets")
        if(options['timezone'].replace(" ","") not in pytz.all_timezones):
            raise CommandError("please select a valid timezone. you can check your timezone from the link: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568")
        try:
            activitytime = eval(options['activityperiod'])
        except:
            raise CommandError("invalid activityperiod, format should be array of json eg: [{'start_time': 'Feb 1 2020  1:33PM', 'end_time': 'Feb 1 2020 1:54PM'}]")

        #inserting into the database:
        user = User()
        user.id =  uuid.uuid1().hex
        user.real_name = options['name']
        user.tz =options['timezone']

        activity_object =[]
        for period in activitytime:

            start_time = datetime.strptime( period['start_time'].replace(" ","") , '%b%d%y%H:%M%p')
            end_time = datetime.strptime( period['end_time'].replace(" ","") , '%b%d%y%H:%M%p')
            activityperiod =ActivityPeriod(start_time = start_time, end_time =end_time , user_id=user)
            activity_object.append(activityperiod)
            activityperiod =None

        user_id=user.save()
        for activityperiod in activity_object:
            activityperiod.save();
        self.stdout.write(self.style.SUCCESS('Successfully saved'))