import time
from selenium import webdriver
from multiprocessing import Pool


def process_website(url):
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(url)
        time.sleep(5)

        driver.save_screenshot(f'{url.replace("http://", "").replace("https://", "")}.png')
        driver.quit()
    except Exception as e:
        print(f"Помилка під час обробки {url}: {str(e)}")


if __name__ == '__main__':
    websites = ['https://www.google.com', 'https://wikipedia.org', 'https://www.github.com']

    pool = Pool(processes=3)

    pool.map(process_website, websites)

    pool.close()
    pool.join()
