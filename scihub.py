try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError:
    print("Install selenium: conda install -c conda-forge selenium")

try:
    from urllib.parse import urlparse
except ImportError:
    print("Install urllib")

try:
    import requests
except ImportError:
    print("Install requests")

import os
import time

class SciHub:
    def __init__(self, url="https://sci-hub.se/", waitTime=5, folder="./"):
        self.url = url
        self.waitTime = waitTime
        self.folder= folder

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--enable-javascript")
        profile={"plugins.plugins_list": [{ "enabled": False,
                                            "name": "Chrome PDF Viewer"}],
                 "download.deafult_directory": folder,
                 "download.extensions_to_open" : ""}
        self.options.add_experimental_option("prefs", profile)

        self.driver = webdriver.Chrome(chrome_options=self.options)
        print("chrome browser opened")
        self.driver.implicitly_wait(self.waitTime)
        self.driver.get(url)
        print("website opened")

        time.sleep(self.waitTime)

    def __del__(self):
        try:
            print("closing browser")
            self.driver.close()
            print("browser closed")
            self.driver.quit()
            print("selenium quit")
        except Exception as ex:
            print("SciHub::__del__() Exception:", str(ex))

    def download(self, doi):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/form/input[2]"))
            )
            print("found doi input text box")
            el.send_keys(doi)
            print("doi entered")
        except Exception as ex:
            print("doi input error:", str(ex))
            return False

        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[7]"))
            )
            print("found open button")
            el.click()
            print("clicked open button")
            time.sleep(self.waitTime)
        except Exception as ex:
            print("open doi click error:", str(ex))
            return False


        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located((By.ID, "pdf"))
            )
            print("pdf element iframe found",el.tag_name)
            if "iframe" in el.tag_name:
                print("iframe pdf found")
            else:
                print("iframe pdf not found")
                return False

        except Exception as ex:
            print("id=pdf error:", str(ex))
            return False

        try:
            url = self.driver.find_element_by_id("pdf").get_attribute("src")
            print("url found", url)

            fname = self.folder + os.path.basename(urlparse(url).path)
            print("filename=", fname)

            data = requests.get(url)
            print("content downloaded")

            with open(fname, "wb") as f:
                print(fname, "opened")
                f.write(data.content)
                print(fname, "content saved")

            print(fname, "download completed")
        except Exception as ex:
            print("download error:", str(ex))
            return False

        return True


def main():
    s = SciHub(waitTime=2)
    print("download complete" if s.download("https://doi.org/10.1109/PS.2006.4350204") else "download failed")

if __name__=="__main__":
    main()

