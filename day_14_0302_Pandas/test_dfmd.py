"""
Podgląd w Hackmd.io
pandoc do zmiany na dokument Word'a: https://pandoc.org/
"""

import snakemd
import pandas as pd
from snakemd import Document, MDList, Paragraph, InlineText, Table


doc = snakemd.new_doc("test_df01")
df = pd.read_csv("lotniska.csv", delimiter=";")

doc.add_header("Nasz piękny dokument", level=1)
doc.add_horizontal_rule()

doc.add_element(Paragraph([InlineText("Test DataFrame", italics=True)]))
data_ = df.values.tolist()

doc.add_table(
    ["Rok", "Chopin", "Modlin", "Gdańsk"],
    data_,)

doc.add_horizontal_rule()


doc.add_quote("""
W ten sposób mamy stworzony dokument,
który możemy przygotować automatycznie.
""")
doc.add_header("Zmiana na docx", level=4)
doc.add_code("pandoc -o test.docx test00.md", lang="shell")
doc.output_page()
