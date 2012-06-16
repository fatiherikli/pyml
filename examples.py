from pyml import *

doc =  \
HTML(
    HEAD(
        TITLE('Hello from PYML'),
    ),
    BODY(
        FORM(
                BUTTON("Button %s", style="color: red") << range(1, 5)
        ),
        UL(
            LI('Hi') * 5
        ),
        FOOTER(
            DIV("With div."),
            DIV("Div with parameters.", _id="foo", _class="bar"),
            "Without div."
        )
    )
)

print doc.render()