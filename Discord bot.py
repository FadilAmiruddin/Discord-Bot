import discord
from discord.ext import commands

import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pytest
import time
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.options import Options
import socket
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.command import Command
import youtube_dl
import pycparser
import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openpyxl
import random


scope = ['https://www.googleapis.com/auth/spreadsheets',' https://www.googleapis.com/auth/drive.file', "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('Data.json',scope)
client = gspread.authorize(creds)

chrome_options = Options()
chrome_options.add_argument(
    r"--user-data-dir=C:\Users\Real fadil\AppData\Local\Google\Chrome\User")  # change to profile path
chrome_options.add_argument('--profile-directory=Profile 1')

l=0


def test_untitled(WebDriver,o):

    WebDriver.get("https://secret.ethanl.ee/")
    WebDriver.set_window_size(974, 1040)
    WebDriver.find_element(By.ID, "lobby-button-create").click()
    WebDriver.find_element(By.ID, "create-game-privacy").click()

    if (int(o) == 9):
        print("hi")
        dropdown = WebDriver.find_element(By.ID, "create-game-size")
        dropdown.find_element(By.XPATH, "//option[. = '9']").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
    if(int(o)==8):
        print("hi")
        dropdown = WebDriver.find_element(By.ID, "create-game-size")
        dropdown.find_element(By.XPATH, "//option[. = '8']").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
    if (int(o) == 7):
        print("hi")
        dropdown = WebDriver.find_element(By.ID, "create-game-size")
        dropdown.find_element(By.XPATH, "//option[. = '7']").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
    if (int(o) == 6):
        print("hi")
        dropdown = WebDriver.find_element(By.ID, "create-game-size")
        dropdown.find_element(By.XPATH, "//option[. = '6']").click()
        WebDriver.find_element(By.ID, "create-game-size").click()   
        WebDriver.find_element(By.ID, "create-game-size").click()
    if (int(o) == 5):
        print("hi")
        dropdown = WebDriver.find_element(By.ID, "create-game-size")
        dropdown.find_element(By.XPATH, "//option[. = '5']").click()
        WebDriver.find_element(By.ID, "create-game-size").click()
        WebDriver.find_element(By.ID, "create-game-size").click()

    WebDriver.find_element(By.ID, "lobby-create-confirm").click()
    WebDriver.implicitly_wait(1)
    x =(WebDriver.find_element(By.CSS_SELECTOR, "strong").text)

    return x


client = commands.Bot(command_prefix=("."))
@client.event
async def on_ready():
    print("hello world")
@client.command()
async def s(ctx,o=10):


    b = webdriver.Chrome(executable_path="C:\Fadil\chromedriver", chrome_options=chrome_options)

    n =test_untitled(b,o)

    u=await ctx.send('https://secret.ethanl.ee/join/'+n)
    await u.add_reaction(':LibsWin:703154301006250056')
    await u.add_reaction(':LibsLoose:703154288809213983')
    await u.add_reaction(':FacistWin:703154273436958790')
    await u.add_reaction(':FacistLoose:703154246312394803')


@client.event
async def on_reaction_add(reaction, user):
    with open('users.json', 'r') as f:
        users= json.load(f)


    await update_data(users,user,reaction)
    with open('users.json', 'w') as f:
        json.dump(users, f)

async def update_data(users,user,reaction):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['Lib wins'] = 0
        users[f'{user.id}']['Lib Loss'] = 0
        users[f'{user.id}']['Facist wins'] = 0
        users[f'{user.id}']['Facist Loss'] = 0
        clinet = openpyxl.load_workbook('Hitler Stats.xlsx')
        clinet.create_sheet(str(user), 0)
        clinet.save("Hitler Stats.xlsx")
    else:
        m= (str(reaction.emoji))

        if m == '<:FacistLoose:703154246312394803>':
            users[f'{user.id}']['Facist Loss'] = users[f'{user.id}']['Facist Loss'] +1

        if m == '<:LibsLoose:703154288809213983>':
            users[f'{user.id}']['Lib Loss'] = users[f'{user.id}']['Lib Loss'] + 1
        if m == '<:LibsWin:703154301006250056>':
            users[f'{user.id}']['Lib wins'] = users[f'{user.id}']['Lib wins'] + 1
        if m == '<:FacistWin:703154273436958790>':
            users[f'{user.id}']['Facist wins'] = users[f'{user.id}']['Facist wins'] + 1


@client.command(pass_context=True)
async def r(ctx):

    channel = ctx.author.voice.channel
    vc= await channel.connect()

    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg.exe", source="Nazi.mp3"))
@client.command(pass_context=True)
async def j(ctx):

    channel = ctx.author.voice.channel
    vc= await channel.connect()

    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg.exe", source="JoJo.mp3"))

@client.command(pass_context=True)
async def f(ctx):

    channel = ctx.author.voice.channel
    vc= await channel.connect()

    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg.exe", source="wwwwww   l.mp3"))

@client.command(pass_context=True)
async def g(ctx):
    await ctx.voice_client.disconnect()

@client.command(pass_context=True)
  
async def clear(ctx, amount =5):

        await ctx.channel.purge(limit=int((amount))+1)


@client.command()
async def showstat(ctx):
    x =(ctx.author.id)
    with open('users.json', 'r') as f:
        users = json.load(f)

    await ctx.send("Facist Wins:" + str(users[f'{x}']['Facist wins']))
    await ctx.send("Facist Loss:" + str(users[f'{x}']['Facist Loss']))
    await ctx.send("Lib Wins:" + str(users[f'{x}']['Lib wins']))
    await ctx.send("Lib Loss:" + str(users[f'{x}']['Lib Loss']))

@client.command()
async def GamesPlayed(ctx):

    with open('users.json', 'r') as f:
        users = json.load(f)

    await ctx.send("TotalGamesPlayed:" + str(users['701234205669064844']['Lib Loss']))


@client.command()
async def AmIGay(ctx):
    if (str(ctx.author.id) == '440309965337657345'):
       await ctx.send("you are not gay")
    else:
      await  ctx.send("you are " + str(random.randint(1, 101))+ "% " + "gay")
@client.command()
async def AmILib(ctx, m=1):
    while (True):
        await ctx.guild.ban(user.id("sajjaad khader#2520"), reason="loser")



client.run("NzAxMjM0MjA1NjY5MDY0ODQ0.XpuhPg.IH_Oy2ZaTUjj4sTsScwhCtUB_0A")