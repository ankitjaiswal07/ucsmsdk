"""This module contains the general information for TopSystem ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class TopSystemConsts():
    MODE_CLUSTER = "cluster"
    MODE_STAND_ALONE = "stand-alone"
    MODE_UNSPECIFIED = "unspecified"


class TopSystem(ManagedObject):
    """This is TopSystem class."""

    consts = TopSystemConsts()
    naming_props = set([])

    mo_meta = MoMeta("TopSystem", "topSystem", "sys", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "ext-lan-config"], [u'topRoot'], [u'aaaAuthRealm', u'aaaLdapEp', u'aaaRadiusEp', u'aaaSessionInfoTable', u'aaaTacacsPlusEp', u'aaaUserEp', u'commSvcEp', u'computeRackUnit', u'domainEnvironmentFeatureCont', u'domainNetworkFeatureCont', u'domainServerFeatureCont', u'domainStorageFeatureCont', u'equipmentChassis', u'equipmentFex', u'extmgmtIfMonPolicy', u'extvmmEp', u'featureContextEp', u'firmwareCatalogue', u'firmwareStatus', u'firmwareSystem', u'firmwareUpgradeInfo', u'fsmStatus', u'initiatorRequestorEp', u'initiatorRequestorGrpEp', u'licenseEp', u'lstorageSvcSched', u'mgmtAccessPolicy', u'mgmtBackup', u'mgmtBackupPolicyConfig', u'mgmtController', u'mgmtEntity', u'mgmtImporter', u'mgmtIntAuthPolicy', u'networkElement', u'pkiEp', u'policyControlEp', u'powerEp', u'swatInjection', u'syntheticDirectory', u'syntheticFsObj', u'sysdebugCoreFileRepository', u'sysdebugEp', u'sysdebugTechSupFileRepository', u'topInfoPolicy', u'trigLocalSched', u'trigMeta', u'trigSched', u'versionEp'], ["Get", "Set"])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "ipv6_addr": MoPropertyMeta("ipv6_addr", "ipv6Addr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster", "stand-alone", "unspecified"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[a-zA-Z][a-zA-Z0-9-]{0,29}""", [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_up_time": MoPropertyMeta("system_up_time", "systemUpTime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", [], []), 
    }

    prop_map = {
        "address": "address", 
        "childAction": "child_action", 
        "currentTime": "current_time", 
        "descr": "descr", 
        "dn": "dn", 
        "ipv6Addr": "ipv6_addr", 
        "mode": "mode", 
        "name": "name", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "site": "site", 
        "status": "status", 
        "systemUpTime": "system_up_time", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.address = None
        self.child_action = None
        self.current_time = None
        self.descr = None
        self.ipv6_addr = None
        self.mode = None
        self.name = None
        self.owner = None
        self.sacl = None
        self.site = None
        self.status = None
        self.system_up_time = None

        ManagedObject.__init__(self, "TopSystem", **kwargs)
