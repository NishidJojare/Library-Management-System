class Library:
    def __init__(self,libid=None,is_any_book_issued=None):
        self.library_set={}
        self.libid=libid
        self.is_any_book_issued=is_any_book_issued
        
    def create_library_account(self):
        self.library_set['LibId']=self.libid
        self.library_set['Is any book Issued ? ']=self.is_any_book_issued
        return self.library_set
        
    def remove_library_account(self,libid):
        self.library_set.pop(libid)
        return self.library_set    
    
