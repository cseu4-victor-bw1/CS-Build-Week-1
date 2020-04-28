from django.contrib.auth.models import User
from adventure.models import Room, Player
from util.details import Room, Descriptions
import random


class Room:
    def __init__(self, id, name, descriptio)