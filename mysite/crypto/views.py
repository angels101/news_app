from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
#Grab Crypto Price Data
    price_request =requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

#Grab Crypto News
    api_request =requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api':api, 'price': price})



def prices(request):
    if request.method == 'POST':
        import requests
        import json
    
        quote = request.POST['quote']
        quote   = quote.upper()
         #Grab Crypto Price Data
        crypto_request =requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto':crypto})

    
    else:

        notfound="Enter a Crypto currency symbol in the form above"
        return render(request, 'prices.html', {'notfound': notfound})

        
