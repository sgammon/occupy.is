from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/main/landing/frame.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/lite.html', '/source/main/landing/frame.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        if 0: yield None
        yield u"\n\t<div id='welcome'>\n\t\t<h1 id='maintitle'>what is <span class='highlight'>occupy</span> to you?</h1>\n\t\t<br />\n\t</div>\n"

    def block_header(context, environment=environment):
        if 0: yield None
        yield u"\n\t<header id='topwelcome' class='preview'>\n\t\t<b>header</b>\n\t</header>\n"

    def block_page_scripts(context, environment=environment):
        l_asset = context.resolve('asset')
        if 0: yield None
        yield u'\n<script src="%s"></script>\n' % (
            context.call(environment.getattr(l_asset, 'script'), 'landing', 'site'), 
        )

    def block_postnorth(context, environment=environment):
        l_asset = context.resolve('asset')
        if 0: yield None
        yield u'\n<link rel=\'stylesheet\' href="%s">\n' % (
            context.call(environment.getattr(l_asset, 'style'), 'landing', 'site'), 
        )

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u"\n\t<footer id='bottomwelcome' class='preview'>\n\t\t<b>footer</b>\n\t</footer>\n"

    blocks = {'content': block_content, 'header': block_header, 'page_scripts': block_page_scripts, 'postnorth': block_postnorth, 'footer': block_footer}
    debug_info = '1=9&16=15&9=19&31=23&32=27&4=30&5=34&24=37'
    return locals()