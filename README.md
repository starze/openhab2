# openHAB2
Configuration files for my openHAB2 installation. Including Modbus communication with Nilan(R) heatpump and Astro bindings.

## Installed bindings, services and things
### Astro 
* [org.openhab.binding.astro](https://github.com/openhab/openHAB2-addons/tree/master/addons/binding/org.openhab.binding.astro)

### Modbus - Nilan(R) heatpump Comfort 300 Top (cts-602 control board)
* [Product documentation](http://www.nilan.de/startseite/losungen/wohnungslosungen/luftung/comfort-serien/comfort-300-top)

* [Modbus documentation](http://reader.livedition.dk/nilan/272/)


## Quick Setup

Copy config files from openhab2 folder into your openHAB2 installation (i.e. /etc/openhab2)


## Details

### Create nilan heatpump modbus items out of csv file 
```sh
$ cd /etc/openHAB2/scripts
$ python createNilanItems.py > ../items/nilan.items
```

### Automatically update items that are not bind with openHAB2 Modbus binding 
Currently I didn't get all items bind with openHAB2 so I used a workaround to get all the nilan sensors into openHAB2 items.

```sh
$ echo "* * * * * root cd /etc/openHAB2/scripts/ && python readNilan.py" >> /etc/contab
```

## Other useful links
* https://github.com/nickma82/nilan_communication_bringup
* https://community.openhab.org/t/openhab1-nilan-heatpump/23538 
* https://github.com/roggmaeh/nilan-openhab
* https://github.com/openhab/openhab1-addons/wiki/Samples-Binding-Config#serial-modbus-nilan-heatpump-configuration
