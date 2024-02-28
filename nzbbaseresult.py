from dataclasses import dataclass
from typing import List
from typing import Any

@dataclass
class Parameter:
    Name: str
    Value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Parameter':
        _Name = str(obj.Name)
        _Value = str(obj.Value)
        return vars(Parameter(_Name, _Value))

@dataclass
class ServerStats:
    ServerID: int
    SuccessArticles: int
    FailedArticles: int

    @staticmethod
    def from_dict(obj: Any) -> 'ServerStats':
        _ServerID = int(obj.ServerID)
        _SuccessArticles = int(obj.SuccessArticles)
        _FailedArticles = int(obj.FailedArticles)
        return vars(ServerStats(_ServerID, _SuccessArticles, _FailedArticles))

@dataclass
class BaseResult:
    Category: str
    CriticalHealth: int
    DeleteStatus: str
    Deleted: bool
    DestDir: str
    DownloadTimeSec: int
    DownloadedSizeHi: int
    DownloadedSizeLo: int
    DownloadedSizeMB: int
    DupeKey: str
    DupeMode: str
    DupeScore: int
    ExParStatus: str
    ExtraParBlocks: int
    FailedArticles: int
    FileCount: int
    FileSizeHi: int
    FileSizeLo: int
    FileSizeMB: int
    FinalDir: str
    Health: int
    Kind: str
    Log: List[object]
    MarkStatus: str
    MaxPostTime: int
    MessageCount: int
    MinPostTime: int
    MoveStatus: str
    NZBFilename: str
    NZBID: int
    NZBName: str
    NZBNicename: str
    ParStatus: str
    ParTimeSec: int
    Parameters: List[Parameter]
    PostTotalTimeSec: int
    RemainingFileCount: int
    RepairTimeSec: int
    ScriptStatus: str
    ScriptStatuses: List[object]
    