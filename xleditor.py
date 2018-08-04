import sys
import xlrd
import xlutils.copy

try:
    import mmap
    MMAP_AVAILABLE = 1
except ImportError:
    MMAP_AVAILABLE = 0
USE_MMAP = MMAP_AVAILABLE


VERSION = '1.0.2'


# ======================================
# NEED TO FIX !!!
# ==> xlwt.UnicodeUtils.upack2 
# change as follow:
# def upack2(s, encoding='ascii'):
#     # If not unicode, make it so.

#     if isinstance(s, unicode_type):
#         us = s
#     elif s:
#         us = unicode(s, encoding)
#     else:
#         us = u''
#     ...
# ======================================


class XBook(object):
    def __init__(self, r_book, w_book):
        self.r_book = r_book
        self.w_book = w_book

    def sheets(self):
        sheets = self.r_book.sheets()

        xsheets = []
        for i in range(len(sheets)):
            r_sheet = sheets[i]
            w_sheet = self.w_book.get_sheet(i)
            xsheet = XSheet(r_sheet, w_sheet)
            xsheets.append(xsheet)
        return xsheets

    def get_sheet(self, index):
        r_sheet = self.r_book.sheet_by_index(index)
        w_sheet = self.w_book.get_sheet(index)
        return XSheet(r_sheet, w_sheet)

    def get_sheet_by_index(self, index):
        return self.get_sheet(index)

    def get_sheet_by_name(self, name):
        r_sheet = self.r_book.sheet_by_name(name)
        index = r_sheet.number
        w_sheet = self.w_book.get_sheet(index)
        return XSheet(r_sheet, w_sheet)

    def save(self, filename_or_stream):
        return self.w_book.save(filename_or_stream)


class XSheet(object):
    def __init__(self, r_sheet, w_sheet):
        self.r_sheet = r_sheet
        self.w_sheet = w_sheet

    @property
    def nrows(self):
        return self.r_sheet.nrows

    @property
    def ncols(self):
        return self.r_sheet.ncols

    def get_value(self, i, j):
        try:
            return self.r_sheet.cell(i, j).value
        except:
            return None

    def cell(self, i, j):
        return self.r_sheet.cell(i, j)

    def row_values(self, colx, start_rowx=0, end_rowx=None):
        return self.r_sheet.row_values(colx, start_rowx=0, end_rowx=None)

    def col_values(self, colx, start_rowx=0, end_rowx=None):
        return self.r_sheet.col_values(colx, start_rowx=0, end_rowx=None)

    def write(self, i, j, *args, **kwargs):

        keep_style = kwargs.pop('keep_style', True)

        try:
            row = self.w_sheet._Worksheet__rows.get(i)
            cell = row._Row__cells.get(j)
            xf_idx = cell.xf_idx
        except Exception as e:
            keep_style = False

        self.w_sheet.write(i, j, *args, **kwargs)

        if keep_style:
            row = self.w_sheet._Worksheet__rows.get(i)
            cell = row._Row__cells.get(j)
            cell.xf_idx = xf_idx




def open_workbook(filename=None, logfile=sys.stdout, verbosity=0, use_mmap=USE_MMAP,
                  file_contents=None, encoding_override=None, formatting_info=True,
                  on_demand=False, ragged_rows=False):
    if 'xlsx' in filename:
        formatting_info = False
    r_book = xlrd.open_workbook(
        filename=filename,
        logfile=logfile,
        verbosity=verbosity,
        use_mmap=use_mmap,
        file_contents=file_contents,
        encoding_override=encoding_override,
        formatting_info=formatting_info,
        on_demand=on_demand,
        ragged_rows=ragged_rows,
    )
    w_book = xlutils.copy.copy(r_book)

    book = XBook(r_book, w_book)

    return book


