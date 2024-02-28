from typing import List
from typing import Any
from dataclasses import dataclass
import nzbbaseresult
import json
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
class Result(nzbbaseresult.BaseResult):
    HistoryTime: int
    ID: int
    Name: str
    RetryData: bool
    ServerStats: List[ServerStats]
    Status: str
    SuccessArticles: int
    TotalArticles: int
    URL: str
    UnpackStatus: str
    UnpackTimeSec: int
    UrlStatus: str

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _ID = int(obj.ID)
        _Name = str(obj.Name)
        _RemainingFileCount = int(obj.RemainingFileCount)
        _RetryData = False
        _HistoryTime = int(obj.HistoryTime)
        _Status = str(obj.Status)
        _Log = []
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
        return vars(Result(ID=_ID, Name=_Name, RemainingFileCount=_RemainingFileCount, RetryData=_RetryData, HistoryTime=_HistoryTime, Status=_Status, Log=_Log, NZBID=_NZBID, NZBName=_NZBName, NZBNicename=_NZBNicename, Kind=_Kind, URL=_URL, NZBFilename=_NZBFilename, DestDir=_DestDir, FinalDir=_FinalDir, Category=_Category, ParStatus=_ParStatus, ExParStatus=_ExParStatus, UnpackStatus=_UnpackStatus, MoveStatus=_MoveStatus, ScriptStatus=_ScriptStatus, ScriptStatuses=[], DeleteStatus=_DeleteStatus, MarkStatus=_MarkStatus, UrlStatus=_UrlStatus, FileSizeLo=_FileSizeLo, FileSizeHi=_FileSizeHi, FileSizeMB=_FileSizeMB, FileCount=_FileCount, MinPostTime=_MinPostTime, MaxPostTime=_MaxPostTime, TotalArticles=_TotalArticles, SuccessArticles=_SuccessArticles, FailedArticles=_FailedArticles, Health=_Health, CriticalHealth=_CriticalHealth, DupeKey=_DupeKey, DupeScore=_DupeScore, DupeMode=_DupeMode, Deleted=_Deleted, DownloadedSizeLo=_DownloadedSizeLo, DownloadedSizeHi=_DownloadedSizeHi, DownloadedSizeMB=_DownloadedSizeMB, DownloadTimeSec=_DownloadTimeSec, PostTotalTimeSec=_PostTotalTimeSec, ParTimeSec=_ParTimeSec, RepairTimeSec=_RepairTimeSec, UnpackTimeSec=_UnpackTimeSec, MessageCount=_MessageCount, ExtraParBlocks=_ExtraParBlocks, Parameters=_Parameters, ServerStats=_ServerStats))

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
