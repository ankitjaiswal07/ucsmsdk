"""This module contains the general information for FabricCartridgeSlotEpFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricCartridgeSlotEpFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_IDENTIFY_BEGIN = "IdentifyBegin"
    NAME_IDENTIFY_EXECUTE_LOCAL = "IdentifyExecuteLocal"
    NAME_IDENTIFY_EXECUTE_PEER = "IdentifyExecutePeer"
    NAME_IDENTIFY_FAIL = "IdentifyFail"
    NAME_IDENTIFY_SUCCESS = "IdentifySuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class FabricCartridgeSlotEpFsmStage(ManagedObject):
    """This is FabricCartridgeSlotEpFsmStage class."""

    consts = FabricCartridgeSlotEpFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricCartridgeSlotEpFsmStage", "fabricCartridgeSlotEpFsmStage", "stage-[name]", VersionMeta.Version251a, "OutputOnly", 0x7L, [], [""], [u'fabricCartridgeSlotEpFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x1L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, None, None, None, None, ["IdentifyBegin", "IdentifyExecuteLocal", "IdentifyExecutePeer", "IdentifyFail", "IdentifySuccess", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "FabricCartridgeSlotEpFsmStage", parent_mo_or_dn, **kwargs)
