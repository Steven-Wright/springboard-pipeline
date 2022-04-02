class DatabaseUtils:
    def select_popular_tickets(self):
        raise NotImplementedError()
    
    def insert_ticket_sales(self, record):
        raise NotImplementedError()

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, type, val, traceback):
        raise NotImplementedError()