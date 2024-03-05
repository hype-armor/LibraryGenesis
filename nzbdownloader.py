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
import os
import exceptions
import mover
from slugify import slugify
slug = slugify()


class Downloader:
    """_summary_"""

    def __init__(self, dest_dir, final_dir) -> None:
        self.q = queue.Queue()
        self.q_to_be_moved = queue.Queue()
        self.dest_dir = dest_dir
        self.final_dir = final_dir
        # Turn-on the worker thread.
        threading.Thread(target=self.worker, daemon=True).start()
        threading.Thread(target=self.mover, daemon=True).start()
        self.list_groups = ListGroups.Root("1.1", "00000000", [])
        self.history = History.Root("1.1", "00000000", [])
        self.start_id = int(time.time())


    
    def _set_id(self):
        self.start_id += 1
        return self.start_id
    
    def trim_dir_path(self, path, max_length=200):
        r = path
        if len(path) > max_length:
            r = path[:max_length]
        if r[-1] == '.':
            r = r[:-1]
        r = r.strip()
        return r
        

    def append(self, nbzdatab64):
        """_summary_

        Args:
            Result (_type_): _description_
        """
        nbzdata = base64.b64decode(nbzdatab64)
        # d1 = ET.fromstring(nbzdata)
        head = ET.fromstring(nbzdata)[0]
        name1 = head[1].text
        name2 = self.trim_dir_path(head[2].text)
        # d3 = ET.fromstring(nbzdata)[1][1]
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
        dest_dir = self.dest_dir + slug.run(name2)
        dest_dir = self.trim_dir_path(dest_dir) + '#' + str(rid)
        final_dir = self.final_dir + slug.run(name2)
        final_dir = self.trim_dir_path(final_dir)
        
        r = ListGroups.Result(
            Category="Books",
            CriticalHealth=898,
            DeleteStatus="NONE",
            Deleted=False,
            DestDir=dest_dir, # incomeplete dir
            DownloadTimeSec=0,
            DownloadedSizeHi=size_hi,
            DownloadedSizeLo=size_lo,
            DownloadedSizeMB=size_mb,
            DupeKey="",
            DupeMode="ALL",
            DupeScore=0,
            ExParStatus="NONE",
            ExtraParBlocks=0,
            FailedArticles=0,
            FileCount=1,
            FinalDir=final_dir, # completed dir
            Health=1000,
            Kind="NZB",
            Log=[],
            MarkStatus="NONE",
            MaxPostTime=0,
            MessageCount=0,
            MinPostTime=0,
            MoveStatus="NONE",
            NZBFilename=name2,
            NZBID=rid,
            NZBName=name2,
            NZBNicename=name2,
            ParStatus="NONE",
            ParTimeSec=0,
            Parameters=params,
            PostTotalTimeSec=0,
            RemainingFileCount=1,
            RepairTimeSec=0,
            ScriptStatus=serverstatus,
            ScriptStatuses=[],
            ActiveDownloads=0,
            FirstID=rid,
            LastID=rid,
            MaxPriority=0,
            MinPriority=0,
            PausedSizeHi=size_hi,
            PausedSizeLo=size_lo,
            PausedSizeMB=size_mb,
            PostInfoText="",
            PostStageProgress=1000,
            PostStageTimeSec=0,
            RemainingParCount=1,
            RemainingSizeHi=size_hi,
            RemainingSizeLo=size_lo,
            RemainingSizeMB=size_mb,
            ServerStats=serverstatus,
            Status="QUEUED",
            SuccessArticles=0,
            TotalArticles=1,
            URL=url,
            UnpackStatus="NONE",
            UnpackTimeSec=0,
            UrlStatus="NONE",
            FileSizeHi=size_hi,
            FileSizeLo=size_lo,
            FileSizeMB=size_mb,
        )
        # r = ListGroups.Result(rid, rid, size_lo, size_hi, size_mb, size_lo, size_hi, size_mb, 1, 1, 0, 0, 1, \
        #    'QUEUED', rid, name2, name2, 'NZB', url, name2+'.nzb', \
        #    self.DestDir + name2, "", "Books", "NONE", "NONE", "NONE", "NONE", "NONE", \
        #    "NONE", "NONE", "NONE", size_lo, size_hi, size_mb, 1, 1638493458, 1638493458, 1, 1, 0, \
        #    1000, 898, "", 0, "ALL", False, size_lo, size_hi, size_mb, 60, 0, 0, 0, 0, 4, 0, params, [], \
        #    serverstatus, "", 0, 0, [])
        results.append(r)
        self.q.put(r)
        return rid

    def status(self):
        """_summary_"""

    def get_list_groups(self, request_id):
        """_summary_

        Args:
            request_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        jsondata = vars(ListGroups.Root.from_dict(self.list_groups))
        # jsondata = vars(self.list_groups.from_dict(self.list_groups))
        # set id
        jsondata["id"] = request_id
        return jsondata

    def get_history(self, request_id):
        """_summary_"""
        for r in self.history.result:
            setattr(r, "ID", r.NZBID)
            setattr(r, "Name", r.NZBName)
            #setattr(r, "HistoryTime", int(time.time()))
            setattr(r, "UrlStatus", "NONE")
        jsondata = vars(History.Root.from_dict(self.history))
        # set id
        jsondata["id"] = request_id
        return jsondata

    def history_delete(self, id):
        # loop through history and find by id
        for item in self.history.result:
            if item.ID == id:
                self.history.result.remove(item)
                
    def group_final_delete(self, id):
        # loop through list groups and find by id
        for item in self.list_groups.result:
            if item.FirstID == id:
                self.list_groups.result.remove(item)

    def _set_status(self, result, status):
        try:
            result.Status = status
        except Exception:
            print("ERR: failed to set status!")
            
    def mover(self):
        print("started mover thread.")
        while True:
            item = self.q_to_be_moved.get()
            for i in range(5):
                time.sleep(1)
                result = self._get_result(self.history.result, item.NZBID)
                if result == {}:
                    continue
                
            if result.MoveStatus != "NONE":
                time.sleep(5)
                continue
            
            try:
                mover.move(result.DestDir, result.FinalDir)
            except PermissionError:
                print(f"Access is denied {result.FinalDir}")
                result.Health = result.Health -1
                continue
            except FileNotFoundError as e:
                print(f"{e} Folder not found {result.FinalDir}")
                result.Health = result.Health -1
                continue
            except FileExistsError as e:
                print(e)
                result.Health = result.Health -1
                continue
                
            if result.Health <= 800:
                result.Health = "FAILURE"
                print("Unable to move dir to final location.")
                self.q_to_be_moved.task_done()
                time.sleep(5)
                continue
            
            self.q_to_be_moved.task_done()
            result.MoveStatus = "SUCCESS"
            
            print(f"Moved: {result.NZBName}")
        
    def _get_result(self, results, nzbid):
        returnable = {}
        for result in results:
            if result.NZBID == nzbid:
                returnable = result
        return returnable

    def worker(self):
        """_summary_"""
        while True:
            try:
                result = self.q.get()
                print(f"Working on {result.NZBName}")
                rrs = self._get_result(self.list_groups.result, result.NZBID)
                rrs.Status = "DOWNLOADING"
                # download that boi
                lgresult = LG.result(rrs)
                lgresult.download()
                rrs.Status = "DOWNLOADED"
                self.q_to_be_moved.put(rrs)
            except exceptions.FailedToDownload:
                rrs.Status = "FAILURE"
                continue
            except Exception as e:
                rrs.Status = "FAILURE"
                print(f"ERR: {result.NZBName}")
                print(e)
            finally:
                self.q.task_done()
                setattr(rrs, "HistoryTime", int(time.time()))
                self.history.result.append(rrs)
                self.list_groups.result.remove(rrs)
                #print(f"Finished {result.NZBName}")
