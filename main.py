import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

url = ('https://www.nba.com/stats/players/traditional?SeasonType=Playoffs')
top10ranking = {}
    '3pontos' : {'field': 'FG3M', 'label' : '3PM'},
    'pontos' : {'field': 'PTS', 'label' : 'PTS'},
    'assistencias' : {'field': 'AST', 'label' : 'AST'},
    'rebotes' : {'field': 'REB', 'label' : 'REB'},
    'roubos' : {'field': 'STL', 'label' : 'STL'},
    'bloqueios' : {'field': 'BLK', 'label' : 'BLK'},
    'rebotes defensivos' : {'field': 'DREB', 'label' : 'DREB'}
    }

def build_ranking(type):
    field = rankings[type]['field']
    label = rankings[type]['label']

    if field == 'FG3M':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[13]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')
        
    if field == 'PTS':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[9]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')

    if field == 'AST':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[22]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')
        
    if field == 'REB':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[21]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')

    if field == 'STL':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[24]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')

    if field == 'BLK':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[25]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')

    if field == 'DREB':
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[19]').click
        elemento = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        html_elemento = elemento.get_attribute('outerHTML')
        soup = BeautifulSoup(html_elemento, 'html.parser')
        table = soup.find(name='table')
        dataframe_full = pd.read_html(str(table)) [0].head(10)
        dataframe = dataframe_full[['Unnamed: 0', 'Player', 'Team', 'Age', label]]
        dataframe.columns = ['Pos', 'Jogador', 'Time', 'Idade', 'Pontos']
        return dataframe.to_dict('records')

option = Options()
option.add_argument("--headless=new")
driver = webdriver.Chrome(options=option)
driver.get(url)
sleep(5)

for k in rankings:
    top10ranking[k] = build_ranking(k)
driver.quit()

js = json.dumps(top10ranking)
fp = open('ranking.json','w')
fp.write(js)
fp.close()