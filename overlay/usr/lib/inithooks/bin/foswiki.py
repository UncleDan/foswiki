#!/usr/bin/python
"""Set FosWiki admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache

from subprocess import check_output
from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Foswiki Password",
            "Enter new password for the Foswiki 'AdminUser' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Foswiki Email",
            "Enter email address for the Foswiki 'AdminUser' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    config_args = ['perl', '-CA', '/var/www/foswiki/tools/configure', '-save', '-set']

    check_output(config_args + ['{Password}=%s' % password])
    (config_args + ['{WebMasterEmail}=%s' % email])


if __name__ == "__main__":
    main()

