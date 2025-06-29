# Create your views here.
from django.shortcuts import render

# Sample data
MARKET_DATA = {
    "Wheat": {"Delhi": 2200, "Punjab": 2100, "UP": 2050},
    "Rice": {"Delhi": 2500, "Punjab": 2400, "UP": 2300},
    "Potato": {"Delhi": 1200, "Punjab": 1300, "UP": 1100},
    "Tomato": {"Delhi": 1400, "Punjab": 1350, "UP": 1250},
}

def market_prices_home(request):
    selected_crop = None
    selected_region = None
    price = None

    if request.method == 'POST':
        selected_crop = request.POST.get('crop')
        selected_region = request.POST.get('region')

        if selected_crop in MARKET_DATA and selected_region in MARKET_DATA[selected_crop]:
            price = MARKET_DATA[selected_crop][selected_region]

    return render(request, 'market_prices/market.html', {
        'crops': list(MARKET_DATA.keys()),
        'regions': ['Delhi', 'Punjab', 'UP'],
        'selected_crop': selected_crop,
        'selected_region': selected_region,
        'price': price
    })
