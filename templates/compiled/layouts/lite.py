from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/layouts/lite.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', '/source/layouts/lite.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_liteheader(context, environment=environment):
        if 0: yield None

    def block_layout_wrap(context, environment=environment):
        if 0: yield None
        yield u"\n<div id='occupy' class='lite layout'>\n\t"
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n</div>\n'

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u'\n\t'
        for event in context.blocks['litefooter'][0](context):
            yield event
        yield u'\n'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'\n\n\t\t\n\t\t\n\t\t<h1>occupy the world!</h1>\n\t\t<br />\n\t\t<center>:)</center>\n\n\t'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n\t'
        for event in context.blocks['liteheader'][0](context):
            yield event
        yield u'\n'

    def block_litefooter(context, environment=environment):
        if 0: yield None

    blocks = {'liteheader': block_liteheader, 'layout_wrap': block_layout_wrap, 'footer': block_footer, 'content': block_content, 'header': block_header, 'litefooter': block_litefooter}
    debug_info = '1=9&5=15&9=18&11=21&24=25&25=28&11=32&4=36&5=39&25=43'
    return locals()