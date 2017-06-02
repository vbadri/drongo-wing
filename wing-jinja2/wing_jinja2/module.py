import jinja2
import os


class SilentUndefined(jinja2.Undefined):
    def _fail_with_undefined_error(self, *args, **kwargs):
        return None


class Jinja2(object):
    def __init__(self, app, **config):
        self.app = app
        self.root_dir = config.get('root_dir')
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.root_dir),
            undefined=SilentUndefined
        )

    def get_template(self, name):
        return self.env.get_template(name)