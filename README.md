# Simple_Dashboard
Flask + D3:  A simple dashboard with Choropleth Map, Radar Chart and Bar Chart.
![overview](https://github.com/caoshiyi/Simple_Dashboard/blob/master/overview.png?raw=true)

## Components: 
* Global Map:  
    1. Move your mouse over the country to see detailed information in text and displayed on the right bottom bar chart.
    2. Click your mouse to add the country to the radar chart on the right. Click twice to cancel.
    3. You can select the comparison matric on the top left corner.
    4. You can change the year by dragging the component in the top middle area.
               
* Radar Chart ( Data in the radar chart are normalized for comparison among different matrics): 
    1. Move your mouse over the area to see which country it represents and detailed information.
    2. You can add/delete countries either by clicking on the map or choosing from the box in the top right corner.
    3. You can choose the matrics you want on the right.
    4. You can change the year by dragging the component in the top middle area.

* Bar Chart (The bar chart is used to show how the a country behaves in different years in term of the selected matric): 
    1. Move your mouse over the bars for detailed information.
    2. The bar chart is linked to the map. So just move your mouse over the map and you will see changes.

## Alerts: 
Alerts will be poped out when you try to add some countries without recorded data to the radar chart from the map.

## Special Representations/Cases: 
   1. Black area of the map represents those countries for which we have no records.
   2. 0% in the radar data represents that we have no recorded data for that country in term of the selected matric.
   3. When the matric you select in the top left corner is "surface area", you may not see any changes in the bar chart, since the surface area for each country remains same in every year.
                  But if you move your mouse over the bars you will see the data actually changes. 
   4. Since the number of countries showing in the map is not equal to that showing in the csv file, there are some countries in the csv file are not specified in the map.
                  However, for better visualization effect, the maximum or minimum value of a matric is computed with the data of countries existing in the map instead of the csv file. 
                  Normally everything's fine, despite some exception (When the matric is popularity density, Monaco has the maximum value. We do not have Monaco in the map.json file, so the maximum value for 2010 shown on the map is 1302.48 instead of 18594.5. 
