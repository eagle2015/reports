# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from .forms import SqlForm
from echarts import Echart, Legend, Bar, Axis, Line, Tooltip
from tools import conn

def index(request):
    # data = '我的名字叫蒋文华'
    # return render(request, 'index.html', {'data': data})

    if request.method == 'POST':
        form = SqlForm(request.POST)
        if form.is_valid():
            sql = form.cleaned_data['sql']
            title = form.cleaned_data['title']
            x = form.cleaned_data['x_label']
            y = form.cleaned_data['y_label']

            x1, y1 = conn('wboss', 'postgres', '', '10.0.0.141', '5432', sql)

            # y1 = [2, 3, 4, 5, 6]
            # x1 = ['Nov', 'Dec', 'Jan', 'Feb', 'marth']
            chart = Echart(title,'')
            chart.use(Bar(y, y1))
            chart.use(Legend(['GDP']))
            chart.use(Axis('category', 'bottom', data=x1, name=x))
            chart.use(Tooltip())

            chart.plot()
            # return HttpResponse(res)
    else:
        form = SqlForm()
    return render(request, 'index.html', {'form': form})
