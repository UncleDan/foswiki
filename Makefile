COMMON_CONF = apache-credit

CREDIT_ANCHORTEXT = Foswiki Appliance
CREDIT_LOCATION = ~ "^/(?!(cgi-bin/twiki/view-kupu))"
include $(FAB_PATH)/common/mk/turnkey/apache.mk
include $(FAB_PATH)/common/mk/turnkey.mk
