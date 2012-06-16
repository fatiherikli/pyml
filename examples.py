from pyml import *

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