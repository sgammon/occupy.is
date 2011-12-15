from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/snippets/pane/header/intro.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'\n<div id=\'intro\' class=\'header pane\'>\n\t\n\t<div class=\'header\'>\n\t\t<h1 class=\'floatleft\'>what is this?</h1>\n\t\t<h1 class=\'absolute snapright\'>who are you? <a href="#">log in</a> / <a href="#">stay anonymous</a></h1>\n\t\t<div class=\'clearboth\'></div>\n\t</div>\n\n\t<div class=\'content\'>\n\t\t<p>I imagine there would be some sort of intro to what we do up here.</p>\n\t</div>\n\n</div>'

    blocks = {}
    debug_info = ''
    return locals()