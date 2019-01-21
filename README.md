# World-Population-Map-using-Pygal
Using 2010 population data, maps population and densities on pygal world map.

Since pygal has a built in worldmap module, using a built in COUNTRY module that uses a 2 digit country code to correspond to each country, I was able to map populations of world countries based on population data I downloaded from the UN website. 

In working on this, I saw that there was an issue as pygal used contry codes to correspondingly plot data to countries on the map and the UN data did not have country codes that matches pygal's. However, I found if I wrote a function the would compare pygal's COUNTRY module country names and the UN's .json file's country names and return the pygal country code if there was a match, then we would be able to plot the UN population data on pygal. This did mean identifying all the countries that did not have 1:1 name matches from Pygal's countries module and the UN's dictoniaries, but once those were identified i modified the UN .json file to have all the country names match their respective pygal country name equivalent. 

From then it was a matter of plotting and styling, with a color scheme broken into three visible categories:
0-10M
10M-1B
>1B

