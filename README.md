Pyml
====

Python HTML Generator


Example
-------

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

    doc.lang_attr = "en"
    doc.hede_budu_attr = "bla bla"

    print doc.render()


Output
------

    <html lang="en" hede_budu="bla bla">
        <head>
            <title>Hello from PYML</title>
        </head>
        <body>
            <form>
                <button style="color: red">Button 1</button>
                <button style="color: red">Button 2</button>
                <button style="color: red">Button 3</button>
                <button style="color: red">Button 4</button>
            </form>
            <ul>
                <li>Hi</li>
                <li>Hi</li>
                <li>Hi</li>
                <li>Hi</li>
                <li>Hi</li>
            </ul>
            <footer>
                <div>With div.</div>
                <div class="bar" id="foo">Div with parameters.</div>
                Without div.
            </footer>
            <!-- <footer>comment-out footer</footer> -->
        </body>
    </html>
