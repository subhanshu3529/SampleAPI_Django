from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import User,ActivityPeriod
import json

#for sending response data of all users with activities in the json format
def call_response(request):
    result ={"members":[]}


    for user in User.objects.all():
        member ={}
        member["id"] = user.id
        member["real_name"]=user.real_name
        member["tz"]=user.tz
        member["activityperiod"]=[]

        activityperiod = ActivityPeriod.objects.filter(user_id=user);

        for activity in activityperiod:
            member["activityperiod"].append({
                "start_time" : activity.start_time.strftime('%b %d %Y %H:%M%p'),
                "end_time" : activity.end_time.strftime("'%b %d %Y %H:%M%p'") })

        result["members"].append(member);

    return  JsonResponse(json.dumps(result), safe=False)
