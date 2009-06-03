from optparse import make_option

from django.core.management.base import AppCommand
from django.core.management.sql import sql_all
from django.db import connections

class Command(AppCommand):
    help = "Prints the CREATE TABLE, custom SQL and CREATE INDEX SQL statements for the given model module name(s)."

    option_list = AppCommand.option_list + (
        make_option('--database', action='store', dest='database',
            default='default', help='Selects what database to print the SQL for.'),
    )

    output_transaction = True

    def handle_app(self, app, **options):
        return u'\n'.join(sql_all(app, self.style, connections[options['database']])).encode('utf-8')
