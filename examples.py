from pyml import *

doc = \
HTML(
    HEAD(
        TITLE('Hello from PYML'),
    ),
    BODY(
        FORM(
            BUTTON("Button %s", style="color: red") << range(1, 5) # map with list.
        ),
        UL(
            LI('Hi') * 5 # repeat 5 times.
        ),
        FOOTER(
            DIV("With div."),
            DIV("Div with parameters.", _id="foo", _class="bar"),
            "Without div."
        ),
        ~ FOOTER('comment-out footer'),
        )
)

print doc.render()