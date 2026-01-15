import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# -----------------------------
# Charger les produits depuis le JSON
# -----------------------------
with open("data.json", "r") as f:
    data = json.load(f)
products = data["products"]


CHROME_PORTABLE_PATH = r'C:\chrome_Sources\chrome-win64\chrome.exe'
CHROME_DRIVER_PATH = r'C:\chrome_Sources\chromedriver-win64\chromedriver.exe'
URL = "https://www.saucedemo.com/"
UNITTEST = False

# -----------------------------
# Configuration du navigateur
# -----------------------------
def OpenChrome(chromedriver_path,chrome_portable_path):
 
    # Configurer les options de Chrome
    chrome_options = Options()
    chrome_options.binary_location = chrome_portable_path
    
    prefs = {
    # Désactiver le gestionnaire de mots de passe
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False
    }
    chrome_options.add_experimental_option("prefs",prefs)
    # chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-default-browser-check")


    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service,options=chrome_options)  # Assurez-vous d'avoir chromedriver installé

    return driver

def CloseChrome(driver):
    driver.quit()

# -----------------------------
# 1️⃣ Connexion avec l'utilisateur standard
# -----------------------------
def login(driver, login_data=data["login"], url=data["url"]):
    driver.get(url)
    driver.find_element(By.ID, "user-name").send_keys(login_data["username"])
    driver.find_element(By.ID, "password").send_keys(login_data["password"])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

# -----------------------------
# Vérifier que tous les produits sont présents
# -----------------------------
def verify_all_products_present(driver, products):
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in product_elements]
    for product in products:
        assert product["name"] in product_names, f"Produit manquant: {product['name']}"
    print("Tous les produits sont présents")

# -----------------------------
# Vérifier qu'une image est visible
# -----------------------------
def verify_image_visible(driver, product):
    img_elem = driver.find_element(By.CSS_SELECTOR, product["img_selector"])
    assert img_elem.is_displayed(), f"L'image pour {product['name']} n'est pas visible"
    print(f"Image visible : {product['name']}")

# -----------------------------
# Vérifier que le bouton "Add to cart" est présent
# -----------------------------
def verify_add_to_cart_button(driver, product):
    button_elem = driver.find_element(By.CSS_SELECTOR, product["button_selector"])
    assert button_elem.is_displayed(), f"Le bouton 'Add to cart' pour {product['name']} n'est pas visible"
    print(f"Bouton 'Add to cart' présent : {product['name']}")

# -----------------------------
# Vérifier que le nom du produit est cliquable
# -----------------------------
def verify_product_name_clickable(driver, product):
    name_elem = driver.find_element(By.CSS_SELECTOR, product["name_selector"])
    assert name_elem.is_displayed(), f"Le nom du produit {product['name']} n'est pas cliquable"
    print(f"Nom du produit cliquable : {product['name']}")

# -----------------------------
# 6️⃣ Retourner à la liste des produits
# -----------------------------
def return_to_products(driver):
    driver.find_element(By.ID, "back-to-products").click()
    time.sleep(1)

# -----------------------------
# 7️⃣ Vérifier le nombre total de produits
# -----------------------------
def verify_total_products(driver, expected_count):
    all_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(all_items) == expected_count, f"Nombre de produits incorrect: {len(all_items)}"
    print(f"Nombre total de produits correct ({len(all_items)})")

# -----------------------------
# Script principal
# -----------------------------
def main():
    # Initialiser le navigateur avec Chrome portable
    driver = OpenChrome(CHROME_DRIVER_PATH, CHROME_PORTABLE_PATH)
    try:
        # Connexion
        login(driver)

        # Vérifier que tous les produits sont présents
        verify_all_products_present(driver, products)

        # Vérifications individuelles pour chaque produit
        for product in products:
            verify_image_visible(driver, product)
            time.sleep(1)
            verify_add_to_cart_button(driver, product)
            time.sleep(1)
            verify_product_name_clickable(driver, product)
            time.sleep(1)

        # Vérifier le nombre total de produits
        verify_total_products(driver, len(products))

    finally:
        CloseChrome(driver)  # Fermer le navigateur proprement


if __name__ == "__main__":
    main()