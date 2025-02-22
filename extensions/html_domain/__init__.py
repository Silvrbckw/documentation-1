"""
Defines a "raw HTML" domain with a ``div[classes]`` and a number of roles
rendered more or less directly to HTML.

.. warning::

    the purpose of this domain is *not* to document HTML or components

NOTE: this extension is only used by special accounting pages (memento, valuation, ...)
for directives likes .. h:div::
TO REMOVE AS SOON AS WE DROP MEMENTOES
"""

import sphinx
import sphinx.roles
from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.body import LineBlock
from sphinx.domains import Domain


def setup(app):
    app.add_domain(HtmlDomain)
    app.add_node(div, html=(
        lambda self, node: self.body.append(self.starttag(node, 'div')),
        lambda self, node: self.body.append('</div>\n')))
    # override parameter was added for version sphinx >= 1.4, TypeError before
    kw = {'override': True} if sphinx.version_info >= (1, 4) else {}
    app.add_node(address, html=(
        lambda self, node: self.body.append(self.starttag(node, 'address')),
        lambda self, node: self.body.append('</address>\n')
    ), **kw)  # docutils.nodes.address exists and is a bibliographic element
    app.add_node(cite, html=(visit_cite, depart_cite))
    for name, node in [('mark', mark), ('ins', insert), ('del', delete),
                       ('s', strikethrough), ('u', underline), ('small', small),
                       ('kbd', kbd), ('var', var), ('samp', samp)]:
        addnode(app, node, name)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }

class div(nodes.General, nodes.Element):
    pass


class Div(Directive):
    optional_arguments = 1
    final_argument_whitespace = 1
    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        try:
            classes = directives.class_option(self.arguments[0]) if self.arguments else []
        except ValueError:
            raise self.error(
                f'Invalid class attribute value for "{self.name}" directive: "{self.arguments[0]}".'
            )
        node = div(text)
        node['classes'].extend(classes)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class address(nodes.General, nodes.Element):
    pass


class Address(LineBlock):
    def run(self):
        [node] = super().run()
        ad = address(node.rawsource, *node.children)
        return [ad]


class mark(nodes.Inline, nodes.TextElement):
    pass


class insert(nodes.Inline, nodes.TextElement):
    pass


class delete(nodes.Inline, nodes.TextElement):
    pass


class strikethrough(nodes.Inline, nodes.TextElement):
    pass


class underline(nodes.Inline, nodes.TextElement):
    pass


class small(nodes.Inline, nodes.TextElement):
    pass


class kbd(nodes.Inline, nodes.FixedTextElement):
    pass


class var(nodes.Inline, nodes.FixedTextElement):
    pass


class samp(nodes.Inline, nodes.FixedTextElement):
    pass


def makerole(node):
    return lambda name, rawtext, text, lineno, inliner, options=None, content=None:\
        ([node(rawtext.strip(), text.strip())], [])


def addnode(app, node, nodename):
    app.add_node(
        node,
        html=(
            lambda self, n: self.body.append(self.starttag(n, nodename)),
            lambda self, n: self.body.append(f'</{nodename}>'),
        ),
    )


def initialism(*args, **kwargs):
    nodes, _ = sphinx.roles.abbr_role(*args, **kwargs)
    [abbr] = nodes
    abbr.attributes.setdefault('classes', []).append('initialism')
    return [abbr], []


def cite_role(typ, rawtext, text, lineno, inliner, options=None, content=None):
    text = utils.unescape(text)
    m = sphinx.roles._abbr_re.search(text)
    if m is None:
        return [cite(text, text, **(options or {}))], []
    content = text[:m.start()].strip()
    source = m.group(1)
    return [cite(content, content, source=source)], []


class cite(nodes.Inline, nodes.TextElement):
    pass


def visit_cite(self, node):
    attrs = {}
    if node.hasattr('source'):
        attrs['title'] = node['source']
    self.body.append(self.starttag(node, 'cite', '', **attrs))


def depart_cite(self, node):
    self.body.append('</abbr>')


class HtmlDomain(Domain):
    name = 'h'
    label = 'HTML'
    directives = {
        'div': Div,
        'address': Address,
    }
    roles = {
        'mark': makerole(mark),
        'ins': makerole(insert),
        'del': makerole(delete),
        's': makerole(strikethrough),
        'u': makerole(underline),
        'small': makerole(small),
        'initialism': initialism,
        'cite': cite_role,
        'kbd': makerole(kbd),
        'var': makerole(var),
        'samp': makerole(samp),
    }

    def merge_domaindata(self, docnames, otherdata) -> None:
        """Merge in data regarding *docnames* from a different domaindata
        inventory (coming from a subprocess in parallel builds).
        """
        # This extension doesn't store any data on the env
        # and therefore doesn't need to support this method.
        pass
