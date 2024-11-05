from .grid.grid import Grid

__version__ = "0.1.5"
__all__ = ["Grid"]

# grid_research/exceptions.py
class GridResearchException(Exception):
    """Base exception for grid_research package"""
    pass

class EmptyTopicError(GridResearchException):
    """Raised when research topic is empty"""
    pass

class EmptyQueryError(GridResearchException):
    """Raised when search query is empty"""
    pass