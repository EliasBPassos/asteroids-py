import os
import mysql.connector
import pygame
from pygame import Vector2
from entity import Entity
from utils import *
from score import Score

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leaderboard"
)

cursor = conn.cursor()
comando = ''
cursor.execute(comando)
#conn.commit() #edit


class Leaderboard(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "leaderboard", GREEN)
        self.leaderboard = cursor.fetchall()





cursor.close()
conn.close()