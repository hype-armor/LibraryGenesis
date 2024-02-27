"""_summary_

Returns:
    _type_: _description_
"""
import threading
import queue
import listgroups as ListGroups
import librarygenesis as LG
import base64
import xml.etree.ElementTree as ET

class Downloader:
    """_summary_
    """
    def __init__(self) -> None:
        self.q = queue.Queue()
        self.DestDir = '/downloads/watch/'
        # Turn-on the worker thread.
        threading.Thread(target=self.worker, daemon=True).start()
        self.list_groups = ListGroups.Root('1.1', '00000000', [])

    def _set_id(self):
        base = int(2500)
        count = int(self.q.qsize())
        return base + count
    

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
        r = ListGroups.Result(rid, rid, size_lo, size_hi, size_mb, size_lo, size_hi, size_mb, 1, 1, 0, 0, 1, \
            'QUEUED', rid, name2, name2, 'NZB', url, name2+'.nzb', \
            self.DestDir + name2, "", "Books", "NONE", "NONE", "NONE", "NONE", "NONE", \
            "NONE", "NONE", "NONE", size_lo, size_hi, size_mb, 1, 1638493458, 1638493458, 1, 1, 0, \
            1000, 898, "", 0, "ALL", False, size_lo, size_hi, size_mb, 60, 0, 0, 0, 0, 4, 0, params, [], \
            serverstatus, "", 0, 0, [])
        results.append(r)
        self.q.put(r)

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
        return self.list_groups.from_dict(self.list_groups)

    def history(self):
        """_summary_
        """
        
    def _set_status(self, result, status):
        try:
            result.Status = status
        except Exception:
            print('ERR: failed to set status!')


    def worker(self):
        """_summary_"""
        while True:
            result = self.q.get()
            rrs = {}
            for rs in self.list_groups.result:
                if rs.NZBID == result.NZBID:
                    rrs = rs

            self._set_status(rrs, "DOWNLOADING")
            print(f'Working on {result.NZBName}')
            lgresult = LG.result(result.URL)
            lgresult.download()
            print(f'Finished {result.NZBName}')
            self._set_status(rrs, "DOWNLOADED")
            self.q.task_done()
            