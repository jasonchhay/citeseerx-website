from csv import DictReader
import csv
import os
from datetime import datetime
from django.core.files import File
import urllib
from django.core.management import BaseCommand

from people.models import TeamMember

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from team_data.csv into the TeamMember model"

    def handle(self, *args, **options):
        if TeamMember.objects.exists():
            print("Team member objects already exist")
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        else:
            with open('./team_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                print(reader)
                print("Loading team data")
                for row in reader:
                    team_member = TeamMember()
                    print(row)
                    team_member.fullname = row['\ufeffname']
                    team_member.role = row['role']
                    team_member.webpageurl = row['webpageurl']
                    team_member.description = row['description']
                    team_member.category = row['category']

                    with open("/mnt/f/psuwebsite/media/team_portraits/{}".format(row['image']), 'rb') as img:
                        team_member.image.save(os.path.basename("{}".format(row['image'])),img)
                    team_member.save()
                    print("Successfully added ",team_member.fullname)
        print("Team data finished loading")
