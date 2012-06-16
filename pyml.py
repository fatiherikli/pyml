from copy import copy
from utils import flatten

class BaseNode(object):
    indent = 0 # will be computed runtime
    commented = False
    data = None

    def get_indent(self):
        return ' ' * 4 * self.indent


class TextNode(BaseNode):

    def __init__(self, *args):
        self.content = map(str, flatten(args))

    def render(self):
        return '\n'.join(self.content)

    def __str__(self):
        return self.render()


class TagNode(BaseNode):

    tag_name = None
    self_closing = False

    def __init__(self, *args, **kwargs):

        def convert_text_node(item):
            if not isinstance(item, BaseNode):
                return TextNode(item)
            return item

        self.content = map(convert_text_node, flatten(args))
        self.parameters = kwargs

    def start_tag(self):
        if self.parameters:
            return '<%s %s>' % (self.tag_name, ' '.join(self.build_attrs()))
        return '<%s>' % self.tag_name

    def close_tag(self):
        return '</%s>' % self.tag_name

    def close_self(self):
        if self.parameters:
            return '<%s %s>' % (self.tag_name, ' '.join(self.build_attrs()))
        return '<%s />' % self.tag_name

    def build_attrs(self):
        for param, value in self.parameters.iteritems():
            if param.startswith('_'):
                param = param[1:]
            yield '%s="%s"' % (param, value)

    def build_text_node(self):
        yield self.start_tag()
        text_node = '\n'.join(map(str, self.content))
        if self.data:
            yield text_node % self.data
        else:
            yield text_node
        yield self.close_tag()

    def build_lines(self):
        yield self.start_tag()
        for item in self.content:
            yield item.get_indent() + item.render()
        yield self.get_indent() + self.close_tag()

    def _recursive_for_indent(self, tag, indent=1):
        for sub_tag in tag.content:
            sub_tag.indent = indent
            if isinstance(sub_tag, TagNode):
                self._recursive_for_indent(sub_tag, indent+1)

    def have_sub_tags(self):
        return any([isinstance(item, TagNode) for item in self.content])

    def prepare(self):
        if not self.indent:
            self._recursive_for_indent(self)

        if self.self_closing:
            return self.close_self()

        if not self.have_sub_tags():
            return ''.join(self.build_text_node())

        return '\n'.join(self.build_lines())

    def render(self):
        if self.commented:
            return '<!-- %s -->' % self.prepare()
        return self.prepare()


    # OPERATOR OVERLOADINGS

    def __mul__(self, multiplier):
        return [self, ] * multiplier

    def __invert__(self):
        self.commented = True
        return self

    def __lshift__(self, mappings):
        mapped_list = []
        for mapping in mappings:
            clone_object = copy(self)
            clone_object.data = mapping
            mapped_list.append(clone_object)
        return mapped_list


class HTML(TagNode):
    tag_name = "html"

class DIV(TagNode):
    tag_name = "div"

class P(TagNode):
    tag_name = "p"

class BR(TagNode):
    tag_name = "br"
    self_closing = True

class SPAN(TagNode):
    tag_name = "span"

class UL(TagNode):
    tag_name = "ul"

class LI(TagNode):
    tag_name = "li"


doc =  HTML(
            UL(
                LI(
                    SPAN(
                        SPAN(
                            'SELAMMMM',
                            ~ DIV('OK')
                        )
                    )
                ),
                LI('SELAM'),
                LI('--> %s') << range(1, 5) ,
                LI('SELAM') ,
                LI('SELAM'),
                LI('SELAM'),
                "SELAM",
                "NABER",
                BR(),
                "IYI MISIN?",
            ),
            DIV(
                SPAN('OK', id="selam", _class="naber") * 10
            ),
            DIV(),
)

print doc.render()