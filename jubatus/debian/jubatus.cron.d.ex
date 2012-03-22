#
# Regular cron jobs for the jubatus package
#
0 4	* * *	root	[ -x /usr/bin/jubatus_maintenance ] && /usr/bin/jubatus_maintenance
