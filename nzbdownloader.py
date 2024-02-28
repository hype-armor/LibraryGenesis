"""_summary_

Returns:
    _type_: _description_
"""
import threading
import queue
import listgroups as ListGroups
import history as History
import librarygenesis as LG
import base64
import xml.etree.ElementTree as ET
import time

class Downloader:
    """_summary_
    """
    def __init__(self) -> None:
        self.q = queue.Queue()
        self.DestDir = '/downloads/watch/'
        # Turn-on the worker thread.
        threading.Thread(target=self.worker, daemon=True).start()
        self.list_groups = ListGroups.Root('1.1', '00000000', [])
        self.history = History.Root('1.1', '00000000', [])
        self.start_id = int(time.time())

    def _set_id(self):
        self.start_id += 1
        return self.start_id
    

    def append(self, nbzdatab64):
        """_summary_

        Args:
            Result (_type_): _description_
        """
        nbzdata = base64.b64decode(nbzdatab64)
        #d1 = ET.fromstring(nbzdata)
        head = ET.fromstring(nbzdata)[0]
        name2 = head[2].text
        #d3 = ET.fromstring(nbzdata)[1][1]
        url = ET.fromstring(nbzdata)[1][1][0].text

        results = self.list_groups.result
        rid = self._set_id()
        param_drone = ListGroups.Parameter("drone", "d188d0297746457d8820ea655b47df42")
        param_unpack = ListGroups.Parameter("Unpack:", "yes")
        params = []
        params.append(param_drone)
        params.append(param_unpack)
        serverstatus = [ListGroups.ServerStats(1, 0, 0)]
        size_lo = 287985404
        size_hi = 0
        size_mb = 274
        r = ListGroups.Result(Category='Books', CriticalHealth=898, DeleteStatus='NONE', Deleted=False, \
            DestDir=self.DestDir, DownloadTimeSec=0, DownloadedSizeHi=size_hi, DownloadedSizeLo=size_lo, \
            DownloadedSizeMB=size_mb, DupeKey='', DupeMode='ALL', DupeScore=0, ExParStatus='NONE', \
            ExtraParBlocks=0, FailedArticles=0, FileCount=1, FinalDir=(self.DestDir + name2), Health=1000, \
            Kind="NZB", Log=[], MarkStatus='NONE', MaxPostTime=0, MessageCount=0, MinPostTime=0, \
            MoveStatus='NONE', NZBFilename=name2, NZBID=rid, NZBName=name2, NZBNicename=name2, \
            ParStatus='NONE', ParTimeSec=0, Parameters=params , PostTotalTimeSec=0, RemainingFileCount=1, \
            RepairTimeSec=0, ScriptStatus=serverstatus, ScriptStatuses=[], ActiveDownloads=0, FirstID=rid, LastID=rid, \
            MaxPriority=0, MinPriority=0, PausedSizeHi=size_hi, PausedSizeLo=size_lo, PausedSizeMB=size_mb, \
            PostInfoText="", PostStageProgress=1000, PostStageTimeSec=0, RemainingParCount=1, \
            RemainingSizeHi=size_hi, RemainingSizeLo=size_lo, RemainingSizeMB=size_mb, \
            ServerStats=serverstatus, Status="QUEUED", SuccessArticles=0, TotalArticles=1, URL=url, \
            UnpackStatus="NONE", UnpackTimeSec=0, UrlStatus="NONE", FileSizeHi=size_hi, FileSizeLo=size_lo, \
            FileSizeMB=size_mb)
        #r = ListGroups.Result(rid, rid, size_lo, size_hi, size_mb, size_lo, size_hi, size_mb, 1, 1, 0, 0, 1, \
        #    'QUEUED', rid, name2, name2, 'NZB', url, name2+'.nzb', \
        #    self.DestDir + name2, "", "Books", "NONE", "NONE", "NONE", "NONE", "NONE", \
        #    "NONE", "NONE", "NONE", size_lo, size_hi, size_mb, 1, 1638493458, 1638493458, 1, 1, 0, \
        #    1000, 898, "", 0, "ALL", False, size_lo, size_hi, size_mb, 60, 0, 0, 0, 0, 4, 0, params, [], \
        #    serverstatus, "", 0, 0, [])
        results.append(r)
        self.q.put(r)
        return rid

    def status(self):
        """_summary_
        """


    def get_list_groups(self, request_id):
        """_summary_

        Args:
            request_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        jsondata = vars(ListGroups.Root.from_dict(self.list_groups))
        #jsondata = vars(self.list_groups.from_dict(self.list_groups))
        # set id
        jsondata['id'] = request_id
        return jsondata

    def get_history(self, request_id):
        """_summary_
        """
        for r in self.history.result:
            setattr(r, 'ID', r.NZBID)
            setattr(r, 'Name', r.NZBName)
            setattr(r, 'HistoryTime', 0)
            setattr(r, 'UrlStatus', "NONE")
        jsondata = vars(History.Root.from_dict(self.history))
        # set id
        jsondata['id'] = request_id
        return jsondata
    
    def append_history(self, item):
        """_summary_

        Args:
            item (_type_): _description_
        """
        
    def _set_status(self, result, status):
        try:
            result.Status = status
        except Exception:
            print('ERR: failed to set status!')


    def worker(self):
        """_summary_"""
        while True:
            try:
                result = self.q.get()
                print(f'Working on {result.NZBName}')
                rrs = {}
                for rs in self.list_groups.result:
                    if rs.NZBID == result.NZBID:
                        rrs = rs

                self._set_status(rrs, "DOWNLOADING")

                # download that boi
                lgresult = LG.result(rrs)
                lgresult.download()
            except Exception:
                print("ERR: {result.NZBName}")
            finally:
                self._set_status(rrs, "DOWNLOADED")
                self.q.task_done()
                print(f'Finished {result.NZBName}')
                self.history.result.append(rrs)
            