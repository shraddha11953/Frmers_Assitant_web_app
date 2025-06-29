# Create your views here.
from django.shortcuts import render

def recommend_crop(request):
    recommended_crop = None
    if request.method == 'POST':
        soil = request.POST.get('soil')
        temp = float(request.POST.get('temperature'))
        rainfall = float(request.POST.get('rainfall'))

        # Simple rules
        if soil == 'clay' and temp > 25 and rainfall > 100:
            recommended_crop = 'Rice'
        elif soil == 'loamy' and 20 < temp < 30:
            recommended_crop = 'Wheat'
        elif soil == 'sandy' and temp > 30:
            recommended_crop = 'Millets'
        elif soil == 'black' and temp > 25:
            recommended_crop = 'Cotton'
        else:
            recommended_crop = 'Please consult with expert or test soil further.'

    return render(request, 'crop_recommendation/recommend.html', {
        'recommended_crop': recommended_crop
    })
