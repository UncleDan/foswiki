COMMON_CONF = apache-credit apache-vhost
COMMON_OVERLAYS = apache

CREDIT_ANCHORTEXT = Foswiki Appliance
CREDIT_LOCATION = ~ "^/(?!(cgi-bin/twiki/view-kupu))"

include $(FAB_PATH)/common/mk/turnkey.mk
