from pathlib import Path
import os
from functools import lru_cache

@lru_cache(maxsize=1)
def get_project_root() -> Path:
    """
    Returns absolute root path 
    uses env var 'PROJECT_ROOT'

    """
    #using env var if defined
    if env_root:= os.getenv("PROJECT_ROOT"):
        return Path(env_root).resolve()
    
    #If not defined, detects root from current file location.
    return Path(__file__).resolve().parents[2] #going 2 levels up

def p(*parts:str) -> Path:
    """
    file location constructor
    Example: p('data', 'raw', 'file.csv')
    """
    return get_project_root().joinpath(*parts)
