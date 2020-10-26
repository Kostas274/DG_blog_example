from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Change user password'
    
    def add_arguments(self, parser):
        parser.add_argument('usid', nargs="+", type=int)
        parser.add_argument('uspsw', nargs="+", type=str)
    
    def handle(self, *args, **options):
        user_id = options['usid'][0]
        user_password = options['uspsw'][0]
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise CommandError('User "%s" does not exist' % user_id)
            
        user.set_password(user_password) 
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully changed password for user "%s"' % user_id))