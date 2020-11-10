#!/usr/bin/python3

import calendar

#*****************************************************************************************

def _cal_html_header():

    cal_html_header = '''\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
table {
  width: 100%
}
</style>
</head>
'''
    return(cal_html_header)

def _cal_html_style():

    cal_html_style = '''\
<style>
body {
  width: 50em;
  margin: 0 auto;
  font-family: Tahoma, Verdana, Arial, sans-serif;
 }
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
td {
  border: 1px solid black;
  border-collapse: collapse;
  text-align: right;
  vertical-align: top;
  padding: 5px;
  height:100px;
  width:100px
}
table {
  width: 100%
}
caption {
  padding: 50px 50px;
  border: 0px solid green;
  text-align: center;
  font-size: 40px;
  font-weight: bold;
  font-size: 200%;
}
</style>
'''
    return(cal_html_style)

def _cal_html_body():

    cal_html_body = '''\
<body>
'''
    return(cal_html_body)

def _cal_html_table(year, month):

    (first_day_in_month, days_in_month) = calendar.monthrange(year, month)
    first_day_of_week = 0

    day_month_Names = [
                       ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat",  "Sun"],
                       ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                       ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                       ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                      ]

    cal_html_table = ''

    cal_html_table = "" + "  <table>\n"
    cal_html_table += "    <caption>Gregorian Calendar " + str(year) +  " " + day_month_Names[3][month - 1] + "</caption>"

    cal_html_table += " \n    <tr>\n"

    for col in range(7):
        cal_html_table += "      <th>" + day_month_Names[0][(col + first_day_of_week) % 7] + "</th>\n"

    cal_html_table += "    <tr>\n"

    dummy_days = (first_day_in_month - first_day_of_week + 7) % 7

    for col in range(dummy_days):
        dummy_text = ""
        cal_html_table += "      <td>" + dummy_text + "</td>\n"

    for day_in_month in range(days_in_month):
        current_table_box = day_in_month + dummy_days
        if (current_table_box % 7) == 0:
            cal_html_table += "    </tr>\n"
            cal_html_table += "    <tr>\n"
        cal_html_table += "      <td>" + str(day_in_month + 1) + "</td>\n"

    dummy_days = (7 - (dummy_days + days_in_month)) % 7

    for col in range(dummy_days):
        dummy_text = ""
        cal_html_table += "      <td>" + dummy_text + "</td>\n"

    return(cal_html_table)

def _cal_html_tail():

    cal_html_tail = '''\
</body>
</html>
'''
    return(cal_html_tail)

#*****************************************************************************************

def main():

    # print (calendar.month(2021,9,2,1))

    html_test = '<font size="0%">This is really tiny text.</font>\n'
    html_test1 = '<p hidden>This paragraph should be hidden.</p>\n'
    html_test1 = '<p visible>This paragraph should be hidden.</p>\n'

    cal_html = ''
    # cal_html = _cal_html_header() + _cal_html_style() + _cal_html_body() + html_test + html_test1 + _cal_html_table(2021, 9) + _cal_html_tail()
    cal_html = _cal_html_header() + _cal_html_style() + _cal_html_body() + html_test + html_test1 + _cal_html_table(2021, 1) + _cal_html_tail()
    print(cal_html)

    # 1111 12 - na, itt gond van!!!
    # ncal -M -b

if __name__ == "__main__":
 
    main()
