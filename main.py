from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Seu ID de afiliado
affiliate_id = "18304320965"

# Página de promoções da Shopee
flash_sale_url = "https://shopee.com.br/flash_sale?promotionId=232735067287552"

@app.route("/links")
def get_links():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(flash_sale_url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    produtos = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/product/" in href:
            link_completo = f"https://shopee.com.br{href}?affiliate_id={affiliate_id}"
            if link_completo not in produtos:
                produtos.append(link_completo)
    
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
