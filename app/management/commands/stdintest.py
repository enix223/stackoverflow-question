from django.core.management.base import BaseCommand
import sys
import argparse


class Command(BaseCommand):
    help = 'Test stdin as input file'

    def add_arguments(self, parser):
        parser.add_argument('foo', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    def handle(self, *args, **options):
        foo = options.get('foo')
        sys.stdout.write(foo.read())
