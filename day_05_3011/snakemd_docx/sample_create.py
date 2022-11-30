def markdown_doc(filename: str, code: str, mid: float, table_no: str):
    import snakemd
    doc = snakemd.new_doc(filename)
    doc.add_header("Kurs Waluty z dnia.")
    doc.add_horizontal_rule()
    doc.add_paragraph(f"Tablica nr: {table_no}")
    doc.add_horizontal_rule()
    doc.add_code(f"Wartość kursu: {mid}")
    doc.add_horizontal_rule()
    doc.output_page()



class MarkdownDoc:

    def __init__(self, filename: str, code: str, table: str = "A"):
        from functions.nbp import Nbp_table
        import snakemd
        self.file: str = filename
        self.code: str = code
        self.table: str = table
        self.mid: float = 0
        self.doc = snakemd.new_doc(self.file)
        self.nbp = Nbp_table(self.table, self.code)

        if self.nbp.get_table():
            self.mid = self.nbp.kurs
            self.doc.add_header("Kurs Waluty z dnia.")
            self.doc.add_horizontal_rule()
            self.doc.output_page()

def md_to_docx(filename: str):
    import subprocess  # wywoływanie poleceń systemowych !!!
    import os

    output_file = os.path.splitext(filename)[0] + ".docx"
    print(f"{filename} -> {output_file}")

    if not os.access(filename, os.R_OK):
        return False


    try:
        command = ["pandoc", "-o", output_file, filename]
        ret_code = subprocess.run(command, capture_output=True)
        print(f"Returned: {ret_code}")
    except Exception as e:
        print(f"ERROR: {e}")

def markdown_to_word_file(directory: str):
    import os
    for any_file in os.listdir(directory):
        full_file = os.path.join(directory, any_file)
        ext = os.path.splitext(full_file)[1].lower()
        if "." in ext and ext.split(".")[1] == "md":
            # mamy markdown
            print(any_file, full_file, ext)




if __name__ == "__main__":
    q = md_to_docx("/home/adasiek/test.md._inny.md")
    print(q)
    q = md_to_docx("../output/USD.md")
    print(q)
    test_md = MarkdownDoc("pliczek", "CHF")
    markdown_doc("pliczek", "CHF", 4.345, "AAAA/Aby")

