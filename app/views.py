from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .equipment import equip
import json

@csrf_exempt
#home
def input1(request):
    return render(request,'input1.html')
#function to store the input values like age,number of years etc.. accordingly and move on to next page
def equip1(request):
    if request.method=='POST':
        age=request.POST['age']
        n=request.POST['n']
        rep=request.POST['rep']
        cost=request.POST['cost']
        request.session['age'] = age
        request.session['n'] = n
        request.session['rep']=rep
        request.session['cost']=cost 
        rows=[] 
        return render(request,'input2.html',{'rows':rows})      

rows=[]
#store the values of the respective revenue, salvage value and cost at each age  of the machine given by user in array format
def input2(request):

    if request.method =="POST":
        
        if "calculate" in request.POST:
            age = request.session.get('age', None)
            n = request.session.get('n', None)
            cost = request.session.get('cost', None)
            rep = request.session.get('rep', None)
            print(rows)
            t = [float(row[0]) for row in rows]
            r = [float(row[1]) for row in rows]
            c = [float(row[2]) for row in rows]
            s = [float(row[3]) for row in rows]
            age=int(age)
            n=int(n)
            cost=float(cost)
            rep=int(rep)
            #call the equip function pass the appropriate parameters to get the possible optimal policies and total cost and move on to next page to display it
            opt, calculated_cost = equip(age, n, cost, rep, t, r, c, s)
            return render(request,'output.html',{'opt':opt,'cost':calculated_cost})
        else:
            row=[]
            t = request.POST['t']
            r = request.POST['r']
            c = request.POST['c']
            s = request.POST['s']
            row.append(t)
            row.append(r)
            row.append(c)
            row.append(s)
            rows.append(row)
            return render(request, 'input2.html', {'rows':rows})