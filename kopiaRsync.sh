#!/bin/bash

rsync -zavHW --stats --exclude="node_modules" /home/abc/gity/hugo1/hugo-scroll/exampleSite/public/. -e "ssh -i /home/abc/.ssh/ultronnazwa" root@server.pl:/var/www/hugo.ampere.pro

rsync -zavHW --stats --exclude="wp-data" -e "ssh -i /home/abc/.ssh/ultronnazwa" root@server.pl:/srv/www/blog.ampere.pro/. /home/abc/webdev1/TURBO/blog.ampere.pro

# rclone copy -vvv -P /home/abc/Dokumenty/WAZ megacrypt:/WAZ 
# rclone copy -vvv -P /home/abc/gity/devweb megacrypt:/devweb
# rclone copy -vvv -P /home/abc/webdev1 megacrypt:/webdev1

# rclone config
# rclone lsd blazeb2:1mainbucket

# rclone copy -vvv -P /home/abc/Dokumenty/WAZ blazeb2crypt:/WAZ 
rclone copy -vvv -P /home/abc/gity/US blazeb2crypt:/US
rclone copy -vvv -P /home/abc/webdev1 blazeb2crypt:/webdev1

rsync -aHAXvhc --update --ignore-existing --exclude="node_modules" --stats --log-file=/home/abc/Pobrane/kopia2$(date -I).txt /home/abc/gity/US/ /media/abc/Nowy/UBU21/US/
rsync -aHAXvhc --update --ignore-existing --stats --log-file=/home/abc/Pobrane/kopia_wd_WAZ$(date -I).txt /home/abc/Dokumenty/WAZ/ /media/abc/Nowy/UBU21/
rsync -aHAXvhc --update --ignore-existing --exclude="node_modules" --stats --log-file=/home/abc/Pobrane/kopia_wd_webdev$(date -I).txt /home/abc/webdev1/ /media/abc/Nowy/UBU21/webdev1/
rsync -aHAXvhc --update --ignore-existing --exclude="node_modules" --stats --log-file=/home/abc/Pobrane/kopia2$(date -I).txt /home/abc/gity/devweb/ /media/abc/Nowy/UBU21/devweb/