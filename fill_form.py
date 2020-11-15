from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

downloadDir = r"C:\attestation_derogatoire"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", downloadDir)
fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/pdf')

fp.set_preference("browser.download.manager.showWhenStarting", False);
fp.set_preference("browser.download.manager.focusWhenStarting", False);
fp.set_preference("browser.download.useDownloadDir", True);
fp.set_preference("browser.helperApps.alwaysAsk.force", False);
fp.set_preference("browser.download.manager.alertOnEXEOpen", False);
fp.set_preference("browser.download.manager.closeWhenDone", True);
fp.set_preference("browser.download.manager.showAlertOnComplete", False);
fp.set_preference("browser.download.manager.useWindow", False);
fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False);
fp.set_preference("pdfjs.disabled", True);



driver = webdriver.Firefox(firefox_profile=fp)
driver.get('https://media.interieur.gouv.fr/deplacement-covid-19/')

prenom_xpath = '//*[@id="field-firstname"]'
nom_xpath = '//*[@id="field-lastname"]'

ddn_xpath = '//*[@id="field-birthday"]'
ldn_xpath = '//*[@id="field-placeofbirth"]'

addr_xpath = '//*[@id="field-address"]'
ville_xpath = '//*[@id="field-city"]'

cp_xpath = '//*[@id="field-zipcode"]'
heureSortie_xpath = '//*[@id="field-heuresortie"]'

motif_xpath = '//*[@id="checkbox-achats"]'
attestation_xpath = '//*[@id="generate-btn"]'


driver.find_element_by_xpath(prenom_xpath).send_keys("prenom")
driver.find_element_by_xpath(nom_xpath).send_keys("nom")
driver.find_element_by_xpath(ddn_xpath).send_keys("10/03/2005")
driver.find_element_by_xpath(ldn_xpath).send_keys("Paris")
driver.find_element_by_xpath(addr_xpath).send_keys("rue de Paris")
driver.find_element_by_xpath(ville_xpath).send_keys("Paris")
driver.find_element_by_xpath(cp_xpath).send_keys("75000")
driver.find_element_by_xpath(motif_xpath).click()
driver.find_element_by_xpath(heureSortie_xpath).send_keys("15:50")

# générer attestation
driver.find_element_by_xpath(attestation_xpath).click()
