

####create map####
import pandas as pd
import folium
import branca
from folium.plugins import MarkerCluster


df = pd.read_csv('D:/Users/rsilva/Documents/Python Scripts/webscrap/projects/tripadvisor/tripadvisor_restaurants_final.csv', encoding = 'utf-8-sig')
df['name'] = df['name'].replace(r'[^\w\s]|_', '', regex=True)

df['name'] = df['name'].astype(pd.StringDtype())

print(df.dtypes)
print(df.count())
#create map object with centering at coordinates mean
m = folium.Map(location=df[["lat", "lon"]].mean().to_list(), zoom_start=5)

#filter so restaurants shown are in Mexico only
df = df[df['lon'].between(-118.5, -86.3)]
df = df[df['lat'].between(14.2, 33.3)]


#create popup function to customize popup
def popup_html(row):
    i = row
    restaurant_name = df['name'].iloc[i]
    restaurant_mail = df['mail'].iloc[i]
    restaurant_phone = df['phone_number'].iloc[i]
    reviews = df['no_reviews'].iloc[i]
    score = df['score'].iloc[i]
    food_types = df['food_type'].iloc[i]

    left_col_color = "#0063B2FF"
    right_col_color = "#9CC3D5FF"

    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(restaurant_name) + """
    </head>
        <table style="height: 126px; width: 350px;">
    <tbody>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Phone Number</span></td>
    <td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(restaurant_phone) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Contact E-mail</span></td>
    <td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(restaurant_mail) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Number of reviews</span></td>
    <td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(reviews) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Score</span></td>
    <td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(score) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Type of Food</span></td>
    <td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(food_types) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html




marker_cluster = MarkerCluster().add_to(m)

for i in range(len(df)):
    location = (df["lat"].iloc[i], df["lon"].iloc[i])
    html = popup_html(i)
    iframe = branca.element.IFrame(html = html, width=510, height=280)
    # my_string = 'name: {}\n, phone: {}\n, food_type: {}'.format(r['name'], r['phone_number'], r['food_type'])
    popup = folium.Popup(folium.Html(html, script=True), max_width=500)
    folium.Marker(location=location, popup = popup).add_to(marker_cluster)




# for i,r in df.iterrows():
#     location = (r["lat"], r["lon"])
#     html = popup_html(i)
#     iframe = branca.element.IFrame(html = html, width=510, height=280)
#     # my_string = 'name: {}\n, phone: {}\n, food_type: {}'.format(r['name'], r['phone_number'], r['food_type'])
#     popup = folium.Popup(folium.Html(html, script=True), max_width=500)
#     folium.Marker(location=location, popup = popup).add_to(marker_cluster)

m.save('tripadvisor_restaurants_mexico2.html')