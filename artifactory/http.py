# -*- coding: utf-8 -*-
"""
Artifactory client
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# std imports
import json
from urlparse import urljoin

# third party imports
import requests
from lxml import etree

# project imports
from .logger import log


class Api(object):
    API_PREFIX = "api/"

    def __init__(self, url, username, password,
            redirect="artifactory", log=log, *args, **kwargs):
        self.log = log

        self.url = urljoin(url,
                "/".join([redirect, self.API_PREFIX]))
        self.log.debug("API url set to {0}".format(self.url))

        self.username = username
        self.password = password


class HTTP(object):

    def __init__(self, api,
            log=log, *args, **kwargs):
        self.log = log
        self.api = api

    def get(self, data={}, endpoint=None, headers={"Content-Type": "application/json"},
            instance_class=None, *args, **kwargs):

        endpoint = self.abs_endpoint(endpoint)

        if kwargs:
            data = dict(data.iteritems() + kwargs.iteritems())

        response = requests.get(endpoint, headers=headers,
                params=data, auth=(self.api.username, self.api.password))

        return self.render(response, instance_class=instance_class)

    def post(self, endpoint=None, headers={"Content-Type": "application/json"},
            data=None, context={}, instance_class=None, *args, **kwargs):
        endpoint = self.abs_endpoint(endpoint)

        # give priority to user data
        if not data:
            data = dict(self.to_payload().iteritems() + context.iteritems()) if context else self.to_payload()

        response = requests.post(endpoint, headers=headers,
                data=data, auth=(self.api.username, self.api.password))

        response.raise_for_status()
        return self.render(response, instance_class=instance_class)

    def put(self, endpoint=None, headers={"Content-Type": "application/json"},
            data=None, context={}, instance_class=None, *args, **kwargs):

        endpoint = self.abs_endpoint(endpoint)

        # give priority to user data
        if not data:
            data = dict(self.to_payload().iteritems() + context.iteritems()) if context else self.to_payload()

        response = requests.put(endpoint, headers=headers,
                data=data, auth=(self.api.username, self.api.password))

        return self.render(response, instance_class=instance_class)

    def delete(self, endpoint=None, headers={"Content-Type": "application/json"},
            data=None, context={}, instance_class=None, *args, **kwargs):

        endpoint = self.abs_endpoint(endpoint)

        response = requests.delete(endpoint, headers=headers,
                data=data, auth=(self.api.username, self.api.password))

        return self.render(response, instance_class=instance_class)

    def abs_endpoint(self, endpoint):
        return urljoin(self.api.url, endpoint if endpoint else self.endpoint)

    def render(self, response, instance_class=None):

        try:
            response.raise_for_status()
        except Exception, e:
            # NOTE: Exception is re-raised as to add error message
            # to exception send by server side
            message = "{0}: {1}".format(e.message, response.content)
            self.log.error(message)
            e.args = (message,)
            raise

        try:
            if instance_class:
                data = response.json()

                self.log.debug("Rendering payload as instance {0} with json {1}".format(
                    instance_class, data))

                if isinstance(data, (list)):
                    instance_list = []
                    for payload in data:
                        instance_list.append(self.from_payload(
                            payload,
                            self._get_instance(data, instance_class)
                            ))
                    return instance_list
                else:
                    return self.from_payload(
                            data,
                            self._get_instance(data, instance_class)
                            )

            self.log.debug("Rendering payload as json {0}".format(
                response.json()))
            return response.json()
        except Exception, e:
            self.log.error(e)
            # NOTE: Improve this logic later
            try:
                root = etree.fromstring(response.content)
                self.log.debug("Rendering payload as xml {0}".format(
                    root))
                return root
            except Exception, e:
                self.log.error(e)
                self.log.debug("Rendering payload as content {0}".format(
                    response.content))
                return response.content

    def _get_instance(self, data, instance_class):
        return instance_class(self.api)

    def from_payload(self, data, instance):
        # tags match variable names sent by artifactory server
        tags = instance._get_tags()

        for tag, value in data.iteritems():
            field = tags.get(tag)
            # field[0] - variable name
            # field[1] - default type
            if field:
                self.log.debug("Setting field {0} with value {1} for instance {2}".format(
                    field[0], value, instance.__class__.__name__))
                setattr(instance, field[0], value)

        return instance

    def to_dict(self):
        data = {}
        for field, details in self._get_fields().iteritems():
            # details[0] - tags
            # details[1] - defualt value
            data[details[0]] = getattr(self, field, details[1])
        return data

    def to_payload(self):
        payload = json.dumps(self.to_dict())
        self.log.debug("Payload {0} to be posted for {1}".format(payload,
            self.__class__.__name__))
        return payload

    @property
    def _fields(self):
        return self._required + self._optional

    @property
    def required(self):
        return [field for field, tag, defualt in self._required]

    @property
    def optional(self):
        return [field for field, tag, defualt in self._optional]

    def _get_fields(self):
        fields = {}
        for field, tag, defualt in self._fields:
            fields[field] = (tag, defualt)
        return fields

    def _get_tags(self):
        tags = {}
        for field, tag, defualt in self._fields:
            tags[tag] = (field, defualt)
        return tags

