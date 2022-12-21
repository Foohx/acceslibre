import csv
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List
from unittest.mock import ANY

import pytest
import requests
from django.core import management
from frictionless import Resource, Schema, validate_resource, validate_schema

from erp.export.export import export_schema_to_csv
from erp.export.generate_schema import generate_schema
from erp.export.mappers import EtalabMapper
from erp.models import Erp


def test_csv_creation(data):
    dest_path = NamedTemporaryFile(suffix=".csv").name

    try:
        erps = Erp.objects.having_a11y_data().all()[0:10]
        export_schema_to_csv(dest_path, erps, EtalabMapper)

        assert Path(dest_path).exists() is True
    finally:
        os.remove(dest_path)


def test_export_command(mocker, data, settings):
    settings.DATAGOUV_API_KEY = "fake"  # To pass the check before uploading
    mocker.patch("requests.post")

    # tweak the existing ERP to have some fields to export
    data.erp.accessibilite.accueil_audiodescription_presence = True
    data.erp.accessibilite.accueil_audiodescription = ["avec_app"]
    data.erp.accessibilite.save()

    assert Erp.objects.all(), "No ERP"

    management.call_command("export_to_datagouv")
    assert os.path.isfile("acceslibre.csv")
    assert os.stat("acceslibre.csv").st_size > 0
    with open("acceslibre.csv", "r") as f:
        reader = csv.reader(f)
        header, erp_csv = iter(reader)
        assert len(header) == 73, "New exported field or missing field in export"
        assert erp_csv == [
            ANY,
            "Aux bons croissants",
            "34830",
            "Jacou",
            "4",
            "grand rue",
            "",
            "",
            "52128577500016",
            "Boulangerie",
            "",
            "",
            "3.9047933",
            "43.6648217",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "True",
            '["avec_app"]',
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "True",
            "False",
            "",
            "",
            "",
            "",
        ]

    os.unlink("acceslibre.csv")


def test_export_failure(mocker, data, settings):
    settings.DATAGOUV_API_KEY = "fake"  # To pass the check before uploading
    mocker.patch(
        "requests.post",
        side_effect=requests.RequestException("KO"),
    )

    with pytest.raises(management.CommandError) as err:
        management.call_command("export_to_datagouv")

    if os.path.isfile("acceslibre.csv"):
        os.unlink("acceslibre.csv")
    assert "Erreur lors de l'upload" in str(err.value)


@pytest.mark.skip(reason="Dependencies error.")
def test_generate_schema(db, activite):
    base = "erp/export/static/base-schema.json"
    outfile = "schema-test.json"
    repository = "https://github.com/MTES-MCT/acceslibre-schema/raw/v0.0.10/"

    generate_schema(base, outfile, repository)

    try:
        with open("schema-test.json", "r") as test_schema, open("erp/export/static/schema.json", "r") as actual_schema:
            assert test_schema.read().strip() == actual_schema.read().strip()
    finally:
        os.remove(test_schema.name)
