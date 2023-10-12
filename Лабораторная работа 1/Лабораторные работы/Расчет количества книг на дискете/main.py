# TODO Найдите количество книг, которое можно разместить на дискете
DISK_SIZE = 1.44  # mb
PAGE_NUMBERS = 100
ROWS_ON_PAGE = 50
SYMBOLS_IN_ROW = 25

symbols_in_rows = SYMBOLS_IN_ROW * ROWS_ON_PAGE
symbols_on_pages = symbols_in_rows * PAGE_NUMBERS

disk_size_in_bytes = DISK_SIZE * 1024 * 1024
symbols_on_pages_size = symbols_on_pages * 4

books_number = disk_size_in_bytes // symbols_on_pages_size

print("Количество книг, помещающихся на дискету:", int(books_number))

