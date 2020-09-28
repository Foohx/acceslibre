import pytest
import html

from django.contrib.auth.models import User
from django.core import mail
from django.urls import reverse
from splinter import Browser

from erp.models import Erp
from erp import schema

from tests.fixtures import data


@pytest.fixture
def browser():
    return Browser("django")


def login(browser, username, password, next=None):
    next_qs = f"?next={next}" if next else ""
    browser.visit(reverse("login") + next_qs)
    browser.fill("username", username)
    browser.fill("password", password)
    button = browser.find_by_css("form button[type=submit]")
    button.click()


def test_home(data, browser, capsys):
    browser.visit(reverse("home"))

    assert browser.title.startswith("Accueil")
    assert len(browser.find_by_css("#home-communes-list .card")) == 1

    assert data.erp.geom is not None
    assert data.erp.published == True
    assert data.erp.accessibilite is not None
    assert len(browser.find_by_css("#home-latest-erps-list a")) == 1


def test_erp_details(data, browser):
    browser.visit(data.erp.get_absolute_url())

    assert browser.title.startswith("Aux bons croissants | Boulangerie | Jacou")
    assert browser.is_text_present(data.erp.nom)
    assert browser.is_text_present(data.erp.activite.nom)
    assert browser.is_text_present(data.erp.adresse)
    assert browser.is_text_present("Sanitaires")
    assert browser.is_text_present(
        html.unescape(schema.get_help_text_ui("sanitaires_presence"))
    )
    assert browser.is_text_present(
        html.unescape(schema.get_help_text_ui("sanitaires_adaptes"))
    )


# TODO improve test to check for dedicated section edit links
# def test_erp_details_edit_links(data, browser, capsys):
#     browser.visit(data.erp.get_absolute_url())

#     assert browser.title.startswith(data.erp.nom)
#     assert browser.is_text_not_present("Modifier ces informations")

#     login(browser, "niko", "Abc12345!", next=data.erp.get_absolute_url())

#     assert browser.title.startswith(data.erp.nom)
#     assert browser.is_text_present("Modifier ces informations")


def test_registration_flow(data, browser):
    browser.visit(reverse("django_registration_register") + "?next=/contactez-nous/")
    browser.fill("username", "johndoe")
    browser.fill("first_name", "John")
    browser.fill("last_name", "Doe")
    browser.fill("email", "john@doe.com")
    browser.fill("password1", "Abcdef123!")
    browser.fill("password2", "Abcdef123!")
    button = browser.find_by_css("form button[type=submit]")
    button.click()

    user = User.objects.get(username="johndoe")
    assert user.is_active == False

    assert len(mail.outbox) == 1
    assert "Activation de votre compte" in mail.outbox[0].subject
    assert "johndoe" in mail.outbox[0].body
    assert "http://testserver/accounts/activate" in mail.outbox[0].body
    assert "?next=/contactez-nous/" in mail.outbox[0].body

    activation_url = [
        line
        for line in mail.outbox[0].body.split("\n")
        if line.startswith("http") and "/activate/" in line
    ][0].strip()
    browser.visit(activation_url)

    assert browser.is_text_present("Votre compte est désormais actif")
    user = User.objects.get(username="johndoe")
    assert user.is_active == True

    connect_link = browser.find_by_text("Je me connecte")
    connect_link.click()

    assert browser.is_text_present("Nom d’utilisateur")
    browser.fill("username", "johndoe")
    browser.fill("password", "Abcdef123!")
    button = browser.find_by_css("form button[type=submit]")
    button.click()

    # ensure we've been redirected to where we registered initially from
    assert browser.url == "/contactez-nous/"
    assert browser.is_text_present("Contactez-nous")
