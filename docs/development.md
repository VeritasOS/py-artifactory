#### Development

- Clone repo and install dependencies

        git clone https://github.com/veritasos/py-artifactory.git
        cd py-artifactory
        pip install -r requirements-dev.txt
        pip install -e .


- Gettings details logs

        export ARTIFACTORY_LOGGER=dev


- Running test cases

        py.test tests/


- Implementing new apis

        from artifactory.http import HTTP

        class Version(HTTP):
            endpoint = "system/version"  # artifactory api

            _required = [
                    # field, tag, default
                    ("version", "version", ""),
                    ]

            _optional = [
                    # field, tag, default
                    ("revision", "revision", ""),
                    ("addons", "addons", []),
                    ("license", "license", ""),
                    ]

            def __init__(self, api):
                super(Version, self).__init__(api)


- Out of the box

        from artifactory.http import Api
        version = Version(Api("http://127.0.0.1:8081", "username", "password"))

        # Http methods
        version.get()
        version.post()
        version.put()
        version.delete()

        # json serialization/de-serialization
        version.to_payload()
        version.from_payload()

        # handy methods
        version.required
        version.optional
        version.abs_endpoint


**Start hacking ;)**
