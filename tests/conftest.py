# -*- coding: utf-8 -*-
"""
Fixtures to be loaded at test start run
"""
# std imports
import os
import json

# third party imports
import pytest
from lxml import etree
from mock import MagicMock

# project imports
from artifactory import Artifactory


@pytest.fixture(scope="session", autouse=True)
def artifactory():
    return Artifactory(
            "http://127.0.0.1:8081",
            username="admin",
            password="password",
            )


@pytest.fixture(scope="session")
def mockup_get(request):
    return get_mock_data(request.param)

@pytest.fixture(scope="session")
def mockup_post(request):
    return get_mock_data(request.param)

@pytest.fixture(scope="session")
def mockup_put(request):
    return get_mock_data(request.param)

@pytest.fixture(scope="session")
def mockup_delete(request):
    return get_mock_data(request.param)


def get_mock_data(path):
    response = MagicMock()

    mock_data_directory = os.path.join(os.path.dirname(__file__), "data")
    mock_data_file = os.path.abspath(os.path.join(mock_data_directory, path))

    with open(mock_data_file, 'r') as fl:
        content = fl.read()

    try:
        response.json.return_value = json.loads(content)
    except:
        response.json.side_effect = Exception("Not a valid json")

        #NOTE: Ugly way of doing things, improve this in future
        try:
            response.content = etree.fromstring(content)
        except:
            response.content = content

    return response
