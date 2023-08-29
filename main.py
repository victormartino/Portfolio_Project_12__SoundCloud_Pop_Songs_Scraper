from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import datetime as dtt
import csv


driver = webdriver.Chrome()
driver.get("https://soundcloud.com/discover/sets/charts-top:pop:us")

wait = WebDriverWait(driver, timeout=3)
wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'trackItem__content')))
window = driver.find_element(By.CSS_SELECTOR, 'body')
window.click()

for i in range(6):
    window.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

top_50_pop_hits = driver.find_elements(By.CLASS_NAME, value='trackItem__content')

# I'm using a list with tuples because a dictionary couldn't store multiple songs (values) for the same artist (key)
songs_with_artists = [(song.text.split(" - ")[0], song.text.split(" - ")[1]) for song in top_50_pop_hits]

now = dtt.datetime.now()
today = now.strftime('%d-%m-%Y')

with open(f"top-pop-songs-{today}.csv", "w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date:", today])
    writer.writerow("")
    writer.writerow(["Artist", "Song"])
    for song in songs_with_artists:
        writer.writerow([song[0], song[1]])

driver.quit()