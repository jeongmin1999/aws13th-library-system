class LibraryError(Exception):
    pass
class BookNotExistsError(LibraryError):
    pass
class DuplicateBookError(LibraryError):
    pass
class DuplicateMemberError(LibraryError):
    pass
class MemberNotFound(LibraryError):
    pass
class BookAlreadyBorrowed(LibraryError):
    pass
class BookNotBorrowedByMember(LibraryError):
    pass
class BookNotBorrowed(LibraryError):
    pass