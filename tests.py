import unittest
from pyml import *

class TestGenerateHtml(unittest.TestCase):

    def test_simple_tag(self):
        self.assertEqual(
            DIV('hi!').render(),
            '<div>hi!</div>'
        )

    def test_sub_tags(self):
        self.assertEqual(
            DIV(DIV('hi!')).render(),
            '<div>\n'
            '    <div>hi!</div>\n'
            '</div>'
        )

    def test_self_closing(self):
        self.assertEqual(
            BR().render(),
            '<br />'
        )

    def test_parameters(self):
        self.assertEqual(
            DIV('hi', style='display:none').render(),
            '<div style="display:none">hi</div>'
        )

    def test_multiplier(self):
        self.assertEqual(
            DIV(BR() * 4).render(),
            '<div>\n'
            '    <br />\n'
            '    <br />\n'
            '    <br />\n'
            '    <br />\n'
            '</div>'
        )

    def test_mapping(self):
        self.assertEqual(
            UL(LI('hi %s') << range(1, 5)).render(),
            '<ul>\n'
            '    <li>hi 1</li>\n'
            '    <li>hi 2</li>\n'
            '    <li>hi 3</li>\n'
            '    <li>hi 4</li>\n'
            '</ul>'
        )

    def test_attr_setting(self):
        doc = HTML(HEAD(TITLE('hi')))
        doc.lang_attr = "en"

        self.assertEqual(
            doc.render(),
            '<html lang="en">\n'
            '    <head>\n'
            '        <title>hi</title>\n'
            '    </head>\n'
            '</html>'
        )

    def test_comments(self):
        self.assertEqual(
            ( ~BR() ).render(),
            '<!-- <br /> -->'
        )



if __name__ == '__main__':
    unittest.main()