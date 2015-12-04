"""This module contains the general information for FirmwareImageLock ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareImageLockConsts():
    pass


class FirmwareImageLock(ManagedObject):
    """This is FirmwareImageLock class."""

    consts = FirmwareImageLockConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FirmwareImageLock", "firmwareImageLock", "fw-imagelock[name]", VersionMeta.Version222c, "InputOutput", 0x1fL, [], ["admin"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit', u'osController'], [], ["Get"])

    prop_meta = {
        "image_name_dn": MoPropertyMeta("image_name_dn", "ImageNameDn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "ImageNameDn": "image_name_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.image_name_dn = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareImageLock", parent_mo_or_dn, **kwargs)
