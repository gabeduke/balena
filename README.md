## Setup of the USB memory Stick for Influxdb
The data of the influxdb will be stored in the mount location `\mnt\influxdb`.
The *influxdb* container is configured (see Dockerfile and my_entrypoint.sh) so that a USB drive (e.g. a USB memory stick) with label `influxdb` will be mounted to this mount location.  It is currently also expecting (see Dockerfile) that this USB drive is formatted in `ext4` format.

If no USB drive (or memory stick) with label `influxdb` is connected to the raspberry pi then the named volume `influxdb-data` will be mounted to this location as is specified in the `docker-compose.yml` file.

Notes
1. the current *Balena* version doesn't yet support the definition of a volume for such a mounted drive in the docker compose yaml file therefore this is handled through the influxdb container setup as described here above.
2. It is not possible to mount the same USB drive also in telegraf container (I have tried that) and consequently telegraf is not able to report the `disk` metrics for this USB drive.