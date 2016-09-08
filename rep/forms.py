# -*- coding: utf-8 -*- 
__author__ = 'jwh5566'

from django import forms


class SqlForm(forms.Form):
    sql = forms.CharField(widget=forms.Textarea(attrs={
                              'style': 'height: 200px;width:500px'}), label=u'Sql语句')
    title = forms.CharField(max_length=100, label=u'报表标题')
    x_label = forms.CharField(max_length=100, label=u'X轴标签')
    y_label = forms.CharField(max_length=100, label=u'Y轴标签')