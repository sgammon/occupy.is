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

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u"\n\t<footer id='bottomwelcome' class='collapsed'>\n\t\t"
        template = environment.get_template('snippets/pane/footer/aroundyou.html', '/source/main/landing/frame.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t</footer>\n'

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u"\n\t\n<script>\n\tfunction do_animations()\n\t{\n\t\t$('.droptext').animate({opacity: 0}, {duration: 300, complete: function () {\n\t\t\t\n\t\t\t$('.droptext').remove();\n\t\t\t$('#is').css({opacity: 0}).removeClass('hidden').animate({opacity: 1}, 300);\n\t\t\t$('#poststatus').css({opacity: 0}).removeClass('visualhidden').animate({opacity: 1}, 300);\n\t\t\t$('#topicstream').css({opacity: 0}).removeClass('hidden').animate({opacity: 1}, 300);\n\t\t\t$('.streamitem').css({opacity: 0}).removeClass('hidden').animate({opacity: 1}, 300);\n\t\t}});\n\t}\n\n\t$(document).ready(function ()\n\t{\n\t\tsetInterval(do_animations, 2550);\n\t});\n</script>\n\n"

    def block_content(context, environment=environment):
        l_range = context.resolve('range')
        if 0: yield None
        yield u"\n\n\t<!-- Main Title + Post Topic Form -->\n\t<div id='welcome'>\n\t\t<h1 id='maintitle'>\n\t\t\t<span class='droptext'>what is</span>\n\t\t\t<span class='highlight'>occupy</span>\n\t\t\t<span class='droptext'>to you?</span>\n\n\t\t\t<span id='is' class='hidden'>is...</span>\t\n\t\t</h1>\n\t\t\t\n\t\t<form id='poststatus' method='post' action='/' class='visualhidden'>\n\t\t\t<input id='tellus' class='large statusbox' name='topicbox' placeholder='money in politics' type='search' x-webkit-speech />\n\t\t</form>\n\t\t\n\t\t<div class='clearboth'></div>\n\n\t</div>\n\n\t<!-- Topic Stream -->\n\t<div id='topicstream' class='hidden'>\n\n\t\t<div id='streamcontainer'>\n\t\t\t\n\t\t\t"
        l_i = missing
        for l_i in context.call(l_range, 0, 25):
            if 0: yield None
            yield u'\n\t\t\t<div class=\'streamitem hidden\'>\n\t\t\t\t<div class=\'floatleft stream-img\'>\n\t\t\t\t\t<div class=\'profile_img\'>\n\t\t\t\t\t\t<img height="85" width="85" src=\'http://placehold.it/85x85&text=Occupier\' alt=\'occupier\' />\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\'floatleft stream-content\'>\n\t\t\t\t\t<div class=\'title\'>\n\t\t\t\t\t\t<div class=\'relative snapleft floatleft\'><span class=\'noun\'>sam</span> from <span class=\'noun\'>california</span>- 17 minutes ago</div>\n\t\t\t\t\t\t<div class=\'close-button absolute inline snapright floatright\'><a href=\'#\'>X</a></div>\n\t\t\t\t\t\t<div class=\'clearboth\'></div>\n\t\t\t\t\t</div>\n\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t'
        l_i = missing
        yield u'\n\n\t\t</div>\n\n\t</div>\n\n'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u"\n\t<header id='topwelcome' class='collapsed'>\n\t\t"
        template = environment.get_template('snippets/pane/header/intro.html', '/source/main/landing/frame.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t</header>\n'

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

    blocks = {'footer': block_footer, 'postsouth': block_postsouth, 'content': block_content, 'header': block_header, 'page_scripts': block_page_scripts, 'postnorth': block_postnorth}
    debug_info = '1=9&66=15&68=18&76=23&16=27&41=32&9=38&11=41&72=46&73=50&4=53&5=57'
    return locals()