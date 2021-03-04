import schedule
import time

from django.core.management.base import BaseCommand

from erp.jobs import check_closed_erps
from subscription.jobs import notify_changed_erps
from erp.jobs import import_centres_vaccination


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        schedule.every().day.at("00:00").do(check_closed_erps.job, verbose=True)
        schedule.every(notify_changed_erps.HOURS_CHECK).hours.do(
            notify_changed_erps.job, verbose=True
        )
        schedule.every(6).hours.do(
            import_centres_vaccination.job, verbose=True, report=True
        )
        print("Scheduler started")
        while True:
            schedule.run_pending()
            time.sleep(1)
