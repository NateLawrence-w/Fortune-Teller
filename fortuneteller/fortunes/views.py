from django.shortcuts import render
import random 

# Create your views here.
def  fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        "fortune": fortune
    }
    return render(request, 'fortunes/fortune.html', context)

fortuneList = ["All will go well,", "Be weary of the wolf within your mind but dont be lead astray from the wolf eaither", "This is your momment dont be afraid.", "The greatest risk is not taking one.", "Dont let pride be your fall, but let courage be your guide."]

