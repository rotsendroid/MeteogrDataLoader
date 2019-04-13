## MeteogrDataLoader

__Objective__:
<br/>Create a utility which will download the meteorological data of http://meteosearch.meteo.gr/ (property of National Observatory of Athens - NOA) and then it will export them in .csv format.

__Brief description__:
<br/>The data provided by meteo.gr are in .txt file format, so in order to be able to process them in a software like Excel or SPSS, we should have a utility that will parse and store them in a commonly used format for tabular data.

__Basic usage example__:
<br/><code>$ python3 meteo_load.py -a nemea -i 2008 -f 2009</code>
<br/><br/>Arguments explanation:<br/>
* -a area-name
* -i start-year
* -f stop-year

The **area-name** is the name of the meteorological station. You can see the list of available area names by typing: 
<code>meteo_load.py -d</code>.<br/><br/>
The arguments **start-year** and **stop-year** define the range of the years in which we want to parse the data.

The **.csv** file format is:<br/>
date;avg-temperature;min-temperature;max-temperature;rain

For help type: <code>meteo_load.py -h</code>