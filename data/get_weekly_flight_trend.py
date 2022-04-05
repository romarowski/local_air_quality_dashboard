def button_format(weekly_count):
    #Function receieves a numpy array with the weekly count of flights it then calculates
    #trend and returns dict to format Traffic Button

    trend = (weekly_count[-1] - weekly_count[-2]) / weekly_count[-2] * 100
    trend = int(trend)
    if trend > 0:
        ans = {'text': '⇧ ' + str(trend) + '%', 'color' : 'info'}
    else:
        ans = {'text': '⇩ ' + str(abs(trend)) + '%', 'color' : 'info'}

    return ans




