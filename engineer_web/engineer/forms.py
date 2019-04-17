from django import forms

class notifyForm(forms.Form):
    # required=False 可选项属性
    errotype = forms.CharField(label='违规类型')
    dealvalue = forms.CharField(label='处理情况')
    s = forms.IntegerField(label="安全员ID")
    w = forms.IntegerField(label="工地ID")
    createTime=forms.DateTimeField(label='生成时间')
    changeTime=forms.DateTimeField(label='最后变更时间')