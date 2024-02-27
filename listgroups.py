from typing import List
from typing import Any
from dataclasses import dataclass
import json
from enum import Enum

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
class Result:
    FirstID: int
    LastID: int
    RemainingSizeLo: int
    RemainingSizeHi: int
    RemainingSizeMB: int
    PausedSizeLo: int
    PausedSizeHi: int
    PausedSizeMB: int
    RemainingFileCount: int
    RemainingParCount: int
    MinPriority: int
    MaxPriority: int
    ActiveDownloads: int
    Status: str
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
    ServerStats: List[ServerStats]
    PostInfoText: str
    PostStageProgress: int
    PostStageTimeSec: int
    Log: List[object]

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _FirstID = int(obj.FirstID)
        _LastID = int(obj.LastID)
        _RemainingSizeLo = int(obj.RemainingSizeLo)
        _RemainingSizeHi = int(obj.RemainingSizeHi)
        _RemainingSizeMB = int(obj.RemainingSizeMB)
        _PausedSizeLo = int(obj.PausedSizeLo)
        _PausedSizeHi = int(obj.PausedSizeHi)
        _PausedSizeMB = int(obj.PausedSizeMB)
        _RemainingFileCount = int(obj.RemainingFileCount)
        _RemainingParCount = int(obj.RemainingParCount)
        _MinPriority = int(obj.MinPriority)
        _MaxPriority = int(obj.MaxPriority)
        _ActiveDownloads = int(obj.ActiveDownloads)
        _Status = str(obj.Status)
        _NZBID = int(obj.NZBID)
        _NZBName = str(obj.NZBName)
        _NZBNicename = str(obj.NZBNicename)
        _Kind = str(obj.Kind)
        _URL = str(obj.URL)
        _NZBFilename = str(obj.NZBFilename)
        _DestDir = str(obj.DestDir)
        _FinalDir = str(obj.FinalDir)
        _Category = str(obj.Category)
        _ParStatus = str(obj.ParStatus)
        _ExParStatus = str(obj.ExParStatus)
        _UnpackStatus = str(obj.UnpackStatus)
        _MoveStatus = str(obj.MoveStatus)
        _ScriptStatus = str(obj.ScriptStatus)
        _DeleteStatus = str(obj.DeleteStatus)
        _MarkStatus = str(obj.MarkStatus)
        _UrlStatus = str(obj.UrlStatus)
        _FileSizeLo = int(obj.FileSizeLo)
        _FileSizeHi = int(obj.FileSizeHi)
        _FileSizeMB = int(obj.FileSizeMB)
        _FileCount = int(obj.FileCount)
        _MinPostTime = int(obj.MinPostTime)
        _MaxPostTime = int(obj.MaxPostTime)
        _TotalArticles = int(obj.TotalArticles)
        _SuccessArticles = int(obj.SuccessArticles)
        _FailedArticles = int(obj.FailedArticles)
        _Health = int(obj.Health)
        _CriticalHealth = int(obj.CriticalHealth)
        _DupeKey = str(obj.DupeKey)
        _DupeScore = int(obj.DupeScore)
        _DupeMode = str(obj.DupeMode)
        _Deleted = False
        _DownloadedSizeLo = int(obj.DownloadedSizeLo)
        _DownloadedSizeHi = int(obj.DownloadedSizeHi)
        _DownloadedSizeMB = int(obj.DownloadedSizeMB)
        _DownloadTimeSec = int(obj.DownloadTimeSec)
        _PostTotalTimeSec = int(obj.PostTotalTimeSec)
        _ParTimeSec = int(obj.ParTimeSec)
        _RepairTimeSec = int(obj.RepairTimeSec)
        _UnpackTimeSec = int(obj.UnpackTimeSec)
        _MessageCount = int(obj.MessageCount)
        _ExtraParBlocks = int(obj.ExtraParBlocks)
        _Parameters = [Parameter.from_dict(y) for y in obj.Parameters]
        _ServerStats = [ServerStats.from_dict(y) for y in obj.ServerStats]
        _PostInfoText = str(obj.PostInfoText)
        _PostStageProgress = int(obj.PostStageProgress)
        _PostStageTimeSec = int(obj.PostStageTimeSec)
        return vars(Result(_FirstID, _LastID, _RemainingSizeLo, _RemainingSizeHi, _RemainingSizeMB, _PausedSizeLo, _PausedSizeHi, _PausedSizeMB, _RemainingFileCount, _RemainingParCount, _MinPriority, _MaxPriority, _ActiveDownloads, _Status, _NZBID, _NZBName, _NZBNicename, _Kind, _URL, _NZBFilename, _DestDir, _FinalDir, _Category, _ParStatus, _ExParStatus, _UnpackStatus, _MoveStatus, _ScriptStatus, _DeleteStatus, _MarkStatus, _UrlStatus, _FileSizeLo, _FileSizeHi, _FileSizeMB, _FileCount, _MinPostTime, _MaxPostTime, _TotalArticles, _SuccessArticles, _FailedArticles, _Health, _CriticalHealth, _DupeKey, _DupeScore, _DupeMode, _Deleted, _DownloadedSizeLo, _DownloadedSizeHi, _DownloadedSizeMB, _DownloadTimeSec, _PostTotalTimeSec, _ParTimeSec, _RepairTimeSec, _UnpackTimeSec, _MessageCount, _ExtraParBlocks, _Parameters, _ScriptStatus ,_ServerStats, _PostInfoText, _PostStageProgress, _PostStageTimeSec, []))




@dataclass
class Root:
    version: str
    id: str
    result: List[Result]

    @staticmethod
    def from_dict(self) -> 'Root':
        _version = str(self.version)
        _id = str(self.id)
        _result = [Result.from_dict(y) for y in self.result]
        return Root(_version, _id, _result)
# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
