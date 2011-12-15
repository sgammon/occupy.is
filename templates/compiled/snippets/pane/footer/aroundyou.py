from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/snippets/pane/footer/aroundyou.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u"\n<div id='aroundyou' class='footer pane'>\n\t\n\t<div class='header'>\n\t\t<h1 class='halfwidth'>happenings near you</h1>\n\t\t<h1 class='halfwidth'>your topics + movements</h1>\n\t</div>\n\n\t<div class='content'>\n\t\t<p>Down here, I imagine we'd have some data about what people are saying near you.</p>\n\t</div>\n</div>"

    blocks = {}
    debug_info = ''
    return locals()