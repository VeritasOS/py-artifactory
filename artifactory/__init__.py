# -*- coding: utf-8 -*-
"""
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."


# std imports
import os

# 3rd party imports
from jinja2 import (
        Environment,
        FileSystemLoader,
        )


TEMPLATE_DIR = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
        autoescape=True)


# project imports
from .artifactory import Artifactory

__all__ = [
        "Artifactory",
        ]
