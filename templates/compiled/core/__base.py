from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/core/__base.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<!doctype html>\n<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->\n<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->\n<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->\n<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->\n<head>\n'
        for event in context.blocks['prenorth'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['north'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['postnorth'][0](context):
            yield event
        yield u'\n</head>\n\n<body>\n'
        for event in context.blocks['prebody'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['body'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['postbody'][0](context):
            yield event
        yield u'\n\n'
        for event in context.blocks['presouth'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['south'][0](context):
            yield event
        yield u'\n'
        for event in context.blocks['postsouth'][0](context):
            yield event
        yield u'\n</body>\n</html>'

    def block_prenorth(context, environment=environment):
        if 0: yield None

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_postbody(context, environment=environment):
        if 0: yield None

    def block_north(context, environment=environment):
        if 0: yield None
        yield u'\n'
        template = environment.get_template('core/__north.html', '/source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'

    def block_postsouth(context, environment=environment):
        if 0: yield None

    def block_presouth(context, environment=environment):
        if 0: yield None

    def block_prebody(context, environment=environment):
        if 0: yield None

    def block_south(context, environment=environment):
        if 0: yield None
        yield u'\n'
        template = environment.get_template('core/__south.html', '/source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'
        for event in context.blocks['page_scripts'][0](context):
            yield event
        yield u'\n'

    def block_page_scripts(context, environment=environment):
        if 0: yield None

    def block_postnorth(context, environment=environment):
        if 0: yield None

    blocks = {'prenorth': block_prenorth, 'body': block_body, 'postbody': block_postbody, 'north': block_north, 'postsouth': block_postsouth, 'presouth': block_presouth, 'prebody': block_prebody, 'south': block_south, 'page_scripts': block_page_scripts, 'postnorth': block_postnorth}
    debug_info = '7=9&8=12&11=15&15=18&16=21&18=24&20=27&21=30&25=33&7=37&16=40&18=44&8=47&9=50&25=55&20=58&15=61&21=64&22=67&23=71&11=78'
    return locals()