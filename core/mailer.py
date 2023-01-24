import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from sib_api_v3_sdk import (
    ApiClient,
    Configuration,
    SendSmtpEmail,
    SendSmtpEmailSender,
    SendSmtpEmailTo,
    TransactionalEmailsApi,
)
from sib_api_v3_sdk.rest import ApiException
from waffle import switch_is_active

logger = logging.getLogger(__name__)


class Mailer:
    # FIXME: when all mails will be migrated, clean those args, should be sufficient to keep only to_list and template
    def send_email(self, to_list, subject, template, context=None, reply_to=None, fail_silently=True):
        raise NotImplementedError

    def mail_admins(self, *args, **kwargs):
        return self.send_email([settings.DEFAULT_FROM_EMAIL], *args, **kwargs)


class DefaultMailer(Mailer):
    def send_email(self, to_list, subject, template, context=None, reply_to=None, fail_silently=True):
        context = context if context else {}
        context["SITE_NAME"] = settings.SITE_NAME
        context["SITE_ROOT_URL"] = settings.SITE_ROOT_URL

        email = EmailMessage(
            subject=subject,
            body=render_to_string(template, context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to_list,
            reply_to=[reply_to] if reply_to else [settings.DEFAULT_FROM_EMAIL],
        )
        # Note: The return value will be the number of successfully delivered messages
        # (which can be 0 or 1 since send_mail can only send one message).
        return 1 == email.send(fail_silently=fail_silently)


class SendInBlueMailer(Mailer):
    configuration = None

    def __init__(self) -> None:
        self.configuration = Configuration()
        self.configuration.api_key["api-key"] = settings.SEND_IN_BLUE_API_KEY
        super().__init__()

    def send_email(self, to_list, subject, template, context=None, reply_to=None, fail_silently=True):
        context = context or {}
        context["site_name"] = settings.SITE_NAME
        context["site_url"] = settings.SITE_ROOT_URL

        if template not in settings.SEND_IN_BLUE_TEMPLATE_IDS:
            logger.error(f"Template {template} not found")
            return False

        template_id = settings.SEND_IN_BLUE_TEMPLATE_IDS.get(template)
        send_smtp_email = SendSmtpEmail(
            to=[SendSmtpEmailTo(email=to_list)],
            sender=SendSmtpEmailSender(email=settings.DEFAULT_EMAIL),
            template_id=template_id,
            params=context,
        )
        api_instance = TransactionalEmailsApi(ApiClient(self.configuration))

        try:
            if switch_is_active("USE_REAL_EMAILS"):
                api_instance.send_transac_email(send_smtp_email)
            return True
        except ApiException:
            return False


def get_mailer():
    return DefaultMailer()
