import abc
from typing import Any, Tuple

from ..pipeline_block import PipelineBlock


class FramesExtractor(PipelineBlock):
    """Frame extractor base interface"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'next') and callable(subclass.next)
            and hasattr(subclass, 'frame') and callable(subclass.frame) 
            or NotImplemented
        )

    def init(self, input: str) -> None:
        """Bind input file"""
        self.input = input
        self.cap = None
        self.current_frame = 0

    @abc.abstractmethod
    def info(self) -> Tuple[Tuple[int, int], int, int]:
        """Return input info: ((width, height), fps, frames_count)"""
        pass

    @abc.abstractmethod
    def next(self) -> Tuple[bool, Any]:
        """Get next frame"""
        pass
    
    @abc.abstractmethod
    def frame(self, num: int) -> Any | None:
        """Get frame by name"""
        pass
