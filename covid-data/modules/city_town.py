def city_town(ma_df):
    towns = [
            "Chicopee",
            "Ludlow",
            "Palmer",
            "West Springfield",
            "Springfield",
            "Wilbraham",
            "Agawam",
            "Longmeadow",
            "East Longmeadow",
            ]
    print('<div class="container-fluid">\n')
    for i in range(len(towns)):
        color_class = 'gray'
        if ((i + 1) % 3 == 0): print('\t<div class="row">\n')
        if (ma_df[ma_df["City/Town"] == towns[i]]["Color"].tail(1).values[0] == 3):
            color_class = 'red'
        elif (ma_df[ma_df["City/Town"] == towns[i]]["Color"].tail(1).values[0] == 2):
            color_class = 'yellow'
        elif (ma_df[ma_df["City/Town"] == towns[i]]["Color"].tail(1).values[0] == 1):
            color_class = 'green'
        elif (ma_df[ma_df["City/Town"] == towns[i]]["Color"].tail(1).values[0] == 0):
            color_class = 'gray'

        print('\t\t<div class="', color_class, ' col-md-4">\n')
        print('<div class="town-block">')
        print('\t\t\t<span class="town">', towns[i], '</span>\n')
        print('\t\t\t<br />Two Wk Case Count: ', ma_df[ma_df["City/Town"] == towns[i]]["Two Week Case Counts"].tail(1).values[0], '\n')
        print('\t\t\t<br />Two Wk Positivity: ', round(ma_df[ma_df['City/Town'] == towns[i]]['Percent Positivity'].tail(1).values[0] * 100, 2), '%')
        print('</div>')
        print('\t\t</div>\n')
        if ((i + 1) % 3 == 0): print('\t</div>\n')
    print('</div>\n')
