# openHAB2

Configuration files for my openHAB2 installation. Including Modbus communication with Nilan(R) heatpump and Astro bindings.

## Installed Bindings

### Astro

* [org.openhab.binding.astro](https://github.com/openhab/openHAB2-addons/tree/master/addons/binding/org.openhab.binding.astro)

### Modbus - Nilan(R) heatpump Comfort 300 Top (cts-602 control board)

* [Product documentation](http://www.nilan.de/startseite/losungen/wohnungslosungen/luftung/comfort-serien/comfort-300-top)
* [Modbus documentation](http://reader.livedition.dk/nilan/272/)

### Harmony Hub Binding

* [Harmony Hub Binding documentation](https://www.openhab.org/addons/bindings/harmonyhub/)

### GPIO Binding

* [GPIO Binding documentation](https://www.openhab.org/addons/bindings/gpio1/)

### Kodi Binding

* [Kodi Binding documentation](https://www.openhab.org/addons/bindings/kodi/)

## Installed Persistence

* [RRD4j Persistence](http://docs.openhab.org/addons/persistence/rrd4j/readme.html)

## Installed Transformations

* [Map Transformation](https://github.com/openhab/openhab1-addons/wiki/Transformations)
* [Javascript Transformation](https://github.com/openhab/openhab1-addons/wiki/Transformations)

## Installed UIs

* Basic UI
* HABot
* HABPanel
* Home Builder
* Paper UI

## Quick Setup

Copy config files from openhab2 folder into your openHAB2 installation (i.e. /etc/openhab2)

## Details

Some details how I created my config-files.

* Create nilan heatpump modbus items out of csv file / nilan documentation
```sh
$ cd /etc/openHAB2/scripts
$ python createNilanItems.py > ../items/nilan.items
```
* Add modbus address binding according to nilan address-specifications and the configuration in services/modbus.cfg
* Add Items into your main.sitemap file.

## Some issues due to early adopting modbus plugin 1.10.0-SNAPSHOT

If modbus plugin not already >= v1.10.0.201704100111 (build #1457 or greater) [download](https://openhab.ci.cloudbees.com/job/openHAB1-Addons/lastSuccessfulBuild/artifact/bundles/binding/org.openhab.binding.modbus/target) and copy plugin to /usr/share/openhab2/addons

If modbus communication isn't working see [issue](https://github.com/openhab/openhab2-addons/pull/362/#issuecomment-173125977).

```openhab2-console
feature:install openhab-transport-serial
```

## Other useful links

* <https://github.com/nickma82/nilan_communication_bringup>
* <https://community.openhab.org/t/openhab1-nilan-heatpump/23538>
* <https://github.com/roggmaeh/nilan-openhab>
* <https://github.com/openhab/openhab1-addons/wiki/Samples-Binding-Config#serial-modbus-nilan-heatpump-configuration>
