from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/layouts/main.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', '/source/layouts/main.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_layout_wrap(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block_main(context, environment=environment):
        if 0: yield None
        yield u"\n\n\t\n\t<div id='templates' class='hidden resource'>\n\t\t"
        for event in context.blocks['jstemplates'][0](context):
            yield event
        yield u"\n\t</div>\n\n\t\n\t<div id='app' class='web latest'>\n\t\t"
        for event in context.blocks['layout_wrap'][0](context):
            yield event
        yield u'\n\t</div>\n\n'

    def block_jstemplates(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    blocks = {'layout_wrap': block_layout_wrap, 'main': block_main, 'jstemplates': block_jstemplates}
    debug_info = '1=9&13=15&3=19&7=22&13=25&7=29'
    return locals()