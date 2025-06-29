# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random

# Dummy disease labels
DISEASES = ['Tomato Early Blight', 'Tomato Late Blight', 'Healthy', 'Bacterial Spot', 'Leaf Mold']

def detect_disease(request):
    prediction = None
    image_url = None

    if request.method == 'POST' and request.FILES.get('leaf_image'):
        image = request.FILES['leaf_image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        # Dummy prediction (replace with ML model later)
        prediction = random.choice(DISEASES)

    return render(request, 'disease_detection/detect.html', {
        'prediction': prediction,
        'image_url': image_url,
    })
