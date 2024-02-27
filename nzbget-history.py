from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Parameter:
    Name: str
    Value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Parameter':
        _Name = str(obj.get("Name"))
        _Value = str(obj.get("Value"))
        return Parameter(_Name, _Value)

@dataclass
class Result:
    ID: int
    Name: str
    RemainingFileCount: int
    RetryData: bool
    HistoryTime: int
    Status: str
    Log: List[object]
    NZBID: int
    NZBName: str
    NZBNicename: str
    Kind: str
    URL: str
    NZBFilename: str
    DestDir: str
    FinalDir: str
    Category: str
    ParStatus: str
    ExParStatus: str
    UnpackStatus: str
    MoveStatus: str
    ScriptStatus: str
    DeleteStatus: str
    MarkStatus: str
    UrlStatus: str
    FileSizeLo: int
    FileSizeHi: int
    FileSizeMB: int
    FileCount: int
    MinPostTime: int
    MaxPostTime: int
    TotalArticles: int
    SuccessArticles: int
    FailedArticles: int
    Health: int
    CriticalHealth: int
    DupeKey: str
    DupeScore: int
    DupeMode: str
    Deleted: bool
    DownloadedSizeLo: int
    DownloadedSizeHi: int
    DownloadedSizeMB: int
    DownloadTimeSec: int
    PostTotalTimeSec: int
    ParTimeSec: int
    RepairTimeSec: int
    UnpackTimeSec: int
    MessageCount: int
    ExtraParBlocks: int
    Parameters: List[Parameter]
    ScriptStatuses: List[object]
    ServerStats: List[ServerStat]

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _ID = int(obj.get("ID"))
        _Name = str(obj.get("Name"))
        _RemainingFileCount = int(obj.get("RemainingFileCount"))
        _RetryData = 
        _HistoryTime = int(obj.get("HistoryTime"))
        _Status = str(obj.get("Status"))
        _Log = [.from_dict(y) for y in obj.get("Log")]
        _NZBID = int(obj.get("NZBID"))
        _NZBName = str(obj.get("NZBName"))
        _NZBNicename = str(obj.get("NZBNicename"))
        _Kind = str(obj.get("Kind"))
        _URL = str(obj.get("URL"))
        _NZBFilename = str(obj.get("NZBFilename"))
        _DestDir = str(obj.get("DestDir"))
        _FinalDir = str(obj.get("FinalDir"))
        _Category = str(obj.get("Category"))
        _ParStatus = str(obj.get("ParStatus"))
        _ExParStatus = str(obj.get("ExParStatus"))
        _UnpackStatus = str(obj.get("UnpackStatus"))
        _MoveStatus = str(obj.get("MoveStatus"))
        _ScriptStatus = str(obj.get("ScriptStatus"))
        _DeleteStatus = str(obj.get("DeleteStatus"))
        _MarkStatus = str(obj.get("MarkStatus"))
        _UrlStatus = str(obj.get("UrlStatus"))
        _FileSizeLo = int(obj.get("FileSizeLo"))
        _FileSizeHi = int(obj.get("FileSizeHi"))
        _FileSizeMB = int(obj.get("FileSizeMB"))
        _FileCount = int(obj.get("FileCount"))
        _MinPostTime = int(obj.get("MinPostTime"))
        _MaxPostTime = int(obj.get("MaxPostTime"))
        _TotalArticles = int(obj.get("TotalArticles"))
        _SuccessArticles = int(obj.get("SuccessArticles"))
        _FailedArticles = int(obj.get("FailedArticles"))
        _Health = int(obj.get("Health"))
        _CriticalHealth = int(obj.get("CriticalHealth"))
        _DupeKey = str(obj.get("DupeKey"))
        _DupeScore = int(obj.get("DupeScore"))
        _DupeMode = str(obj.get("DupeMode"))
        _Deleted = 
        _DownloadedSizeLo = int(obj.get("DownloadedSizeLo"))
        _DownloadedSizeHi = int(obj.get("DownloadedSizeHi"))
        _DownloadedSizeMB = int(obj.get("DownloadedSizeMB"))
        _DownloadTimeSec = int(obj.get("DownloadTimeSec"))
        _PostTotalTimeSec = int(obj.get("PostTotalTimeSec"))
        _ParTimeSec = int(obj.get("ParTimeSec"))
        _RepairTimeSec = int(obj.get("RepairTimeSec"))
        _UnpackTimeSec = int(obj.get("UnpackTimeSec"))
        _MessageCount = int(obj.get("MessageCount"))
        _ExtraParBlocks = int(obj.get("ExtraParBlocks"))
        _Parameters = [Parameter.from_dict(y) for y in obj.get("Parameters")]
        _ScriptStatuses = [.from_dict(y) for y in obj.get("ScriptStatuses")]
        _ServerStats = [ServerStat.from_dict(y) for y in obj.get("ServerStats")]
        return Result(_ID, _Name, _RemainingFileCount, _RetryData, _HistoryTime, _Status, _Log, _NZBID, _NZBName, _NZBNicename, _Kind, _URL, _NZBFilename, _DestDir, _FinalDir, _Category, _ParStatus, _ExParStatus, _UnpackStatus, _MoveStatus, _ScriptStatus, _DeleteStatus, _MarkStatus, _UrlStatus, _FileSizeLo, _FileSizeHi, _FileSizeMB, _FileCount, _MinPostTime, _MaxPostTime, _TotalArticles, _SuccessArticles, _FailedArticles, _Health, _CriticalHealth, _DupeKey, _DupeScore, _DupeMode, _Deleted, _DownloadedSizeLo, _DownloadedSizeHi, _DownloadedSizeMB, _DownloadTimeSec, _PostTotalTimeSec, _ParTimeSec, _RepairTimeSec, _UnpackTimeSec, _MessageCount, _ExtraParBlocks, _Parameters, _ScriptStatuses, _ServerStats)

@dataclass
class Root:
    version: str
    id: str
    result: List[Result]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _version = str(obj.get("version"))
        _id = str(obj.get("id"))
        _result = [Result.from_dict(y) for y in obj.get("result")]
        return Root(_version, _id, _result)

@dataclass
class ServerStat:
    ServerID: int
    SuccessArticles: int
    FailedArticles: int

    @staticmethod
    def from_dict(obj: Any) -> 'ServerStat':
        _ServerID = int(obj.get("ServerID"))
        _SuccessArticles = int(obj.get("SuccessArticles"))
        _FailedArticles = int(obj.get("FailedArticles"))
        return ServerStat(_ServerID, _SuccessArticles, _FailedArticles)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
