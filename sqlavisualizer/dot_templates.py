CLASS_TEMPLATE = """
    %(name)s [label=<
    <TABLE BGCOLOR="lightyellow" BORDER="0"
        CELLBORDER="0" CELLSPACING="0">
            <TR><TD COLSPAN="2" CELLPADDING="4"
                    ALIGN="CENTER" BGCOLOR="palegoldenrod"
            ><FONT FACE="Helvetica Bold" COLOR="black"
            >%(name)s</FONT></TD></TR>%(cols)s
    </TABLE>
>]
"""

COLUMN_TEMPLATE = """<TR><TD ALIGN="LEFT" BORDER="0"
    ><FONT FACE="Bitstream Vera Sans">%(name)s</FONT
    ></TD><TD ALIGN="LEFT"
    ><FONT FACE="Bitstream Vera Sans">%(type)s</FONT
    ></TD></TR>"""

RELATION_TEMPLATE = "    \"%(from)s\" -> \"%(to)s\" [label = \"%(by)s\"]"

INIT_TEMPLATE = \
    """
    digraph G {
        fontname = "Bitstream Vera Sans"
        fontsize = 8

        node [
            fontname = "Bitstream Vera Sans"
            fontsize = 8
            shape = "plaintext"
        ]

        edge [
            fontname = "Bitstream Vera Sans"
            fontsize = 8
        ]
"""
