from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/"
}

@app.get('/info')
async def get_info(url : str):
    async with httpx.AsyncClient() as client:
        res = await client.get(url , headers=headers)
        soup = BeautifulSoup(res.text , 'html.parser')
        div = soup.find("div" , {"class" : 'x-price-primary'})
        price = div.find("span" , {"class" : 'ux-textspans'})
        div2 = soup.find("h1" , {"class" : "x-item-title__mainTitle"})
        pname = div2.find("span" , {"class" : 'ux-textspans'})

        if price:
            price_txt = price.text.replace("US" , "").replace("," , "").strip()
            pname_txt = pname.text.strip()

            return {"Product Name": pname_txt , "Price" : price_txt}