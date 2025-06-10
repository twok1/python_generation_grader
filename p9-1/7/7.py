def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

class Pagination:
    def __init__(self, pages, visible_pages):
        self.pages = split_list(pages, visible_pages)
        self.visible_pages = visible_pages
        self._current_page = 1
        self.total_pages = len(self.pages)

    @property
    def current_page(self):
        return self._current_page
    
    @current_page.setter
    def current_page(self, value):
        self._current_page = value
        if self._current_page < 1:
            self._current_page = 1
        elif self._current_page > len(self.pages):
            self._current_page = len(self.pages)
        

    def get_visible_items(self):
        return self.pages[self.current_page - 1]
    
    def prev_page(self):
        self.current_page -= 1
        return self
    
    def next_page(self):
        self.current_page += 1
        return self

    def last_page(self):
        self.current_page = len(self.pages)
        return self
    
    def go_to_page(self, page):
        self.current_page = page

    def first_page(self):
        self.current_page = 1
    