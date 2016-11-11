# -*- coding: utf-8 -*-
"""
Artifactory search endpoint
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# project imports
from ..http import HTTP


class Search(HTTP):
  endpoint = "search"

  _required = [
  ("results", "results", "")
  ]

  _optional = [
  ]

  def __init__(self, api):
    self.api = api
    super(Search, self).__init__(self.api)

  def fetchbydaterange(self, repos, fromepoch , toepoch=None):
    endpoint = "{0}/{1}".format(self.endpoint, "dates")
    
    qryparams={ "dateFields" : "created,lastModified,lastDownloaded",
    "repos" : repos,
    "from" : fromepoch
    }
    
    if toepoch is not None:
      qryparams ["to"] = toepoch

    return self.get(endpoint=endpoint, data = qryparams, instance_class=Search)
