from django.shortcuts import render
from plot.utils import SIR
# Create your views here.

def home(request):
    if request.method == 'POST':
        m = SIR(eons = int(request.POST['Susceptible']) + int(request.POST['Infected']),  Infected = int(request.POST['Infected']), Susceptible = int(request.POST['Susceptible']), rateIR = float(request.POST['rateIR']), rateSI = float(request.POST['rateSI']) )        
        m.run()
        # 
        # print(m.plot())
        return render(request, 'index.html',{'graph':m.plot()})

    return render(request,'home.html')
