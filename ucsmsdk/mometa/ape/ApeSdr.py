"""This module contains the general information for ApeSdr ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeSdrConsts():
    ENTITY_TYPE_ADD_IN_CARD = "ADD_IN_CARD"
    ENTITY_TYPE_BACK_PANEL_BOARD = "BACK_PANEL_BOARD"
    ENTITY_TYPE_BATTERY = "BATTERY"
    ENTITY_TYPE_BIOS = "BIOS"
    ENTITY_TYPE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
    ENTITY_TYPE_CHASSIS_BACK_PANEL_BOARD = "CHASSIS_BACK_PANEL_BOARD"
    ENTITY_TYPE_CMC = "CMC"
    ENTITY_TYPE_CONNECTIVITY_SWITCH = "CONNECTIVITY_SWITCH"
    ENTITY_TYPE_COOLING_UNIT = "COOLING_UNIT"
    ENTITY_TYPE_DEVICE_BAY = "DEVICE_BAY"
    ENTITY_TYPE_DISK = "DISK"
    ENTITY_TYPE_DISK_DRIVE_BAY = "DISK_DRIVE_BAY"
    ENTITY_TYPE_DRIVE_BACKPLANE = "DRIVE_BACKPLANE"
    ENTITY_TYPE_EXTERNAL_ENVIRONMENT = "EXTERNAL_ENVIRONMENT"
    ENTITY_TYPE_FAN_COOLING = "FAN_COOLING"
    ENTITY_TYPE_FRONT_PANEL_BOARD = "FRONT_PANEL_BOARD"
    ENTITY_TYPE_GROUP = "GROUP"
    ENTITY_TYPE_IBMC = "IBMC"
    ENTITY_TYPE_IO_MODULE = "IO_MODULE"
    ENTITY_TYPE_IPMI_CHANNEL = "IPMI_CHANNEL"
    ENTITY_TYPE_MEMORY_DEVICE = "MEMORY_DEVICE"
    ENTITY_TYPE_MEMORY_MODULE = "MEMORY_MODULE"
    ENTITY_TYPE_MGMT_CONTROLLER_FIRMWARE = "MGMT_CONTROLLER_FIRMWARE"
    ENTITY_TYPE_OPERATING_SYSTEM = "OPERATING_SYSTEM"
    ENTITY_TYPE_OTHER = "OTHER"
    ENTITY_TYPE_OTHER_CHASSIS_BOARD = "OTHER_CHASSIS_BOARD"
    ENTITY_TYPE_OTHER_SYSTEM_BOARD = "OTHER_SYSTEM_BOARD"
    ENTITY_TYPE_PCI_BUS = "PCI_BUS"
    ENTITY_TYPE_PCI_EXPRESS_BUS = "PCI_EXPRESS_BUS"
    ENTITY_TYPE_PERIPHERAL = "PERIPHERAL"
    ENTITY_TYPE_PERIPHERAL_BAY = "PERIPHERAL_BAY"
    ENTITY_TYPE_POWER_MANAGEMENT_BOARD = "POWER_MANAGEMENT_BOARD"
    ENTITY_TYPE_POWER_MODULE = "POWER_MODULE"
    ENTITY_TYPE_POWER_SUPPLY = "POWER_SUPPLY"
    ENTITY_TYPE_POWER_SYSTEM_BOARD = "POWER_SYSTEM_BOARD"
    ENTITY_TYPE_POWER_UNIT = "POWER_UNIT"
    ENTITY_TYPE_PROCESSING_BLADE = "PROCESSING_BLADE"
    ENTITY_TYPE_PROCESSOR = "PROCESSOR"
    ENTITY_TYPE_PROCESSOR_BOARD = "PROCESSOR_BOARD"
    ENTITY_TYPE_PROCESSOR_FRONT_SIDE_BUS = "PROCESSOR_FRONT_SIDE_BUS"
    ENTITY_TYPE_PROCESSOR_IO_MODULE = "PROCESSOR_IO_MODULE"
    ENTITY_TYPE_PROCESSOR_MEMORY_MODULE = "PROCESSOR_MEMORY_MODULE"
    ENTITY_TYPE_PROCESSOR_MODULE = "PROCESSOR_MODULE"
    ENTITY_TYPE_REMOTE_MGMT_COMM_DEVICE = "REMOTE_MGMT_COMM_DEVICE"
    ENTITY_TYPE_SATA_SAS_BUS = "SATA_SAS_BUS"
    ENTITY_TYPE_SCSI_BUS = "SCSI_BUS"
    ENTITY_TYPE_SUB_CHASSIS = "SUB_CHASSIS"
    ENTITY_TYPE_SYSTEM_BOARD = "SYSTEM_BOARD"
    ENTITY_TYPE_SYSTEM_BUS = "SYSTEM_BUS"
    ENTITY_TYPE_SYSTEM_CHASSIS = "SYSTEM_CHASSIS"
    ENTITY_TYPE_SYSTEM_INTERNAL_EXPANSION_BOARD = "SYSTEM_INTERNAL_EXPANSION_BOARD"
    ENTITY_TYPE_SYSTEM_MANAGEMENT_MODULE = "SYSTEM_MANAGEMENT_MODULE"
    ENTITY_TYPE_SYSTEM_MANAGEMENT_SOFTWARE = "SYSTEM_MANAGEMENT_SOFTWARE"
    ENTITY_TYPE_UNKNOWN = "UNKNOWN"
    ENTITY_TYPE_UNSPECIFIED = "UNSPECIFIED"
    EVENT_READING_TYPE_DISCRETE_ACPI_POWER = "DISCRETE_ACPI_POWER"
    EVENT_READING_TYPE_DISCRETE_AVAILABILITY = "DISCRETE_AVAILABILITY"
    EVENT_READING_TYPE_DISCRETE_DEVICE_ENABLE = "DISCRETE_DEVICE_ENABLE"
    EVENT_READING_TYPE_DISCRETE_DEVICE_PRESENCE = "DISCRETE_DEVICE_PRESENCE"
    EVENT_READING_TYPE_DISCRETE_LIMIT_EXCEEDED = "DISCRETE_LIMIT_EXCEEDED"
    EVENT_READING_TYPE_DISCRETE_PERFORMANCE_MET = "DISCRETE_PERFORMANCE_MET"
    EVENT_READING_TYPE_DISCRETE_PREDICTIVE_FAILURE = "DISCRETE_PREDICTIVE_FAILURE"
    EVENT_READING_TYPE_DISCRETE_REDUNDANCY = "DISCRETE_REDUNDANCY"
    EVENT_READING_TYPE_DISCRETE_SEVERITY = "DISCRETE_SEVERITY"
    EVENT_READING_TYPE_DISCRETE_STATE = "DISCRETE_STATE"
    EVENT_READING_TYPE_DISCRETE_USAGE = "DISCRETE_USAGE"
    EVENT_READING_TYPE_OEM1 = "OEM1"
    EVENT_READING_TYPE_SENSOR_SPECIFIC = "SENSOR_SPECIFIC"
    EVENT_READING_TYPE_THRESHOLD = "THRESHOLD"
    EVENT_READING_TYPE_UNKNOWN = "UNKNOWN"
    SENSOR_TYPE_ADD_IN_CARD = "ADD_IN_CARD"
    SENSOR_TYPE_BATTERY = "BATTERY"
    SENSOR_TYPE_BOOT_ERROR = "BOOT_ERROR"
    SENSOR_TYPE_BUTTON = "BUTTON"
    SENSOR_TYPE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
    SENSOR_TYPE_CHASSIS = "CHASSIS"
    SENSOR_TYPE_CHIP_SET = "CHIP_SET"
    SENSOR_TYPE_COOLING_DEVICE = "COOLING_DEVICE"
    SENSOR_TYPE_CRITICAL_INTERRUPT = "CRITICAL_INTERRUPT"
    SENSOR_TYPE_CURRENT = "CURRENT"
    SENSOR_TYPE_DRIVE_SLOT = "DRIVE_SLOT"
    SENSOR_TYPE_ENTITY_PRESENCE = "ENTITY_PRESENCE"
    SENSOR_TYPE_EVENT_LOGGING_DISABLED = "EVENT_LOGGING_DISABLED"
    SENSOR_TYPE_FAN = "FAN"
    SENSOR_TYPE_FRU_STATE = "FRU_STATE"
    SENSOR_TYPE_LAN = "LAN"
    SENSOR_TYPE_MANAGEMENT_SUBSYSTEM_HEALTH = "MANAGEMENT_SUBSYSTEM_HEALTH"
    SENSOR_TYPE_MEMORY = "MEMORY"
    SENSOR_TYPE_MICROCONTROLLER_COPROCESSOR = "MICROCONTROLLER_COPROCESSOR"
    SENSOR_TYPE_MODULE_BOARD = "MODULE_BOARD"
    SENSOR_TYPE_MONITOR_ASIC_IC = "MONITOR_ASIC_IC"
    SENSOR_TYPE_OEM1 = "OEM1"
    SENSOR_TYPE_OEM2 = "OEM2"
    SENSOR_TYPE_OEM3 = "OEM3"
    SENSOR_TYPE_OEM4 = "OEM4"
    SENSOR_TYPE_OEM5 = "OEM5"
    SENSOR_TYPE_OEM7 = "OEM7"
    SENSOR_TYPE_OS_BOOT = "OS_BOOT"
    SENSOR_TYPE_OS_CRITICAL_STOP = "OS_CRITICAL_STOP"
    SENSOR_TYPE_OTHER_FRU = "OTHER_FRU"
    SENSOR_TYPE_OTHER_UNITS_BASED_SENSOR = "OTHER_UNITS_BASED_SENSOR"
    SENSOR_TYPE_PHYSICAL_SECURITY = "PHYSICAL_SECURITY"
    SENSOR_TYPE_PLATFORM_ALERT = "PLATFORM_ALERT"
    SENSOR_TYPE_PLATFORM_SECURITY = "PLATFORM_SECURITY"
    SENSOR_TYPE_POWER_MEMORY_RESIZE = "POWER_MEMORY_RESIZE"
    SENSOR_TYPE_POWER_SUPPLY = "POWER_SUPPLY"
    SENSOR_TYPE_POWER_UNIT = "POWER_UNIT"
    SENSOR_TYPE_PROCESSOR = "PROCESSOR"
    SENSOR_TYPE_SESSION_AUDIT = "SESSION_AUDIT"
    SENSOR_TYPE_SLOT_CONNECTOR = "SLOT_CONNECTOR"
    SENSOR_TYPE_SYSTEM_ACPI_POWER_STATE = "SYSTEM_ACPI_POWER_STATE"
    SENSOR_TYPE_SYSTEM_BOOT_INITIATED = "SYSTEM_BOOT_INITIATED"
    SENSOR_TYPE_SYSTEM_EVENT = "SYSTEM_EVENT"
    SENSOR_TYPE_SYSTEM_FIRMWARE_PROGRESS = "SYSTEM_FIRMWARE_PROGRESS"
    SENSOR_TYPE_TEMPERATURE = "TEMPERATURE"
    SENSOR_TYPE_TERMINATOR = "TERMINATOR"
    SENSOR_TYPE_UNKNOWN = "UNKNOWN"
    SENSOR_TYPE_VERSION_CHANGE = "VERSION_CHANGE"
    SENSOR_TYPE_VOLTAGE = "VOLTAGE"
    SENSOR_TYPE_WATCHDOG_1 = "WATCHDOG_1"
    SENSOR_TYPE_WATCHDOG_2 = "WATCHDOG_2"
    TYPE_COMPACT_SENSOR_RECORD = "COMPACT_SENSOR_RECORD"
    TYPE_FULL_SENSOR_RECORD = "FULL_SENSOR_RECORD"
    TYPE_UNKNOWN_RECORD = "UNKNOWN_RECORD"
    UNITS_AMPS = "AMPS"
    UNITS_BECQUERELS = "BECQUERELS"
    UNITS_BITS = "BITS"
    UNITS_BYTES = "BYTES"
    UNITS_CANDELA = "CANDELA"
    UNITS_CENTIMETERS = "CENTIMETERS"
    UNITS_CFM = "CFM"
    UNITS_CHARACTERS = "CHARACTERS"
    UNITS_COLLISIONS = "COLLISIONS"
    UNITS_COLOR_TEMP_DEG_K = "COLOR_TEMP_DEG_K"
    UNITS_CORRECTABLE_ERRORS = "CORRECTABLE_ERRORS"
    UNITS_COULOMBS = "COULOMBS"
    UNITS_CUBIC_CENTIMETERS = "CUBIC_CENTIMETERS"
    UNITS_CUBIC_FEET = "CUBIC_FEET"
    UNITS_CUBIC_INCHS = "CUBIC_INCHS"
    UNITS_CUBIC_METERS = "CUBIC_METERS"
    UNITS_CYCLES = "CYCLES"
    UNITS_DAY = "DAY"
    UNITS_DECIBELS = "DECIBELS"
    UNITS_DEGREES_C = "DEGREES_C"
    UNITS_DEGREES_F = "DEGREES_F"
    UNITS_DEGREES_K = "DEGREES_K"
    UNITS_DWORDS = "DWORDS"
    UNITS_DB_A = "DbA"
    UNITS_DB_C = "DbC"
    UNITS_ERRORS = "ERRORS"
    UNITS_FARADS = "FARADS"
    UNITS_FATAL_ERRORS = "FATAL_ERRORS"
    UNITS_FEET = "FEET"
    UNITS_FL_OZ = "FL_OZ"
    UNITS_FOOT_POUNDS = "FOOT_POUNDS"
    UNITS_GAUSS = "GAUSS"
    UNITS_GBITS = "GBITS"
    UNITS_GBYTES = "GBYTES"
    UNITS_GILBERTS = "GILBERTS"
    UNITS_GRAMS = "GRAMS"
    UNITS_GRAVITIES = "GRAVITIES"
    UNITS_GRAYS = "GRAYS"
    UNITS_HENRIES = "HENRIES"
    UNITS_HITS = "HITS"
    UNITS_HOUR = "HOUR"
    UNITS_HZ = "HZ"
    UNITS_INCHES = "INCHES"
    UNITS_JOULES = "JOULES"
    UNITS_KBITS = "KBITS"
    UNITS_KBYTES = "KBYTES"
    UNITS_KPA = "KPA"
    UNITS_LINES = "LINES"
    UNITS_LITERS = "LITERS"
    UNITS_LUMENS = "LUMENS"
    UNITS_LUX = "LUX"
    UNITS_MBITS = "MBITS"
    UNITS_MBYTES = "MBYTES"
    UNITS_MESSAGES = "MESSAGES"
    UNITS_METERS = "METERS"
    UNITS_MHENRIES = "MHENRIES"
    UNITS_MIL = "MIL"
    UNITS_MILLIMETERS = "MILLIMETERS"
    UNITS_MINUTE = "MINUTE"
    UNITS_MISSES = "MISSES"
    UNITS_MOLES = "MOLES"
    UNITS_MSECONDS = "MSECONDS"
    UNITS_NEWTONS = "NEWTONS"
    UNITS_NITS = "NITS"
    UNITS_OHMS = "OHMS"
    UNITS_OUNCES = "OUNCES"
    UNITS_OUNCE_INCHES = "OUNCE_INCHES"
    UNITS_OVERRUNS = "OVERRUNS"
    UNITS_PACKETS = "PACKETS"
    UNITS_POUNDS = "POUNDS"
    UNITS_PPM = "PPM"
    UNITS_PSI = "PSI"
    UNITS_QWORDS = "QWORDS"
    UNITS_RADIANS = "RADIANS"
    UNITS_RESETS = "RESETS"
    UNITS_RETRIES = "RETRIES"
    UNITS_REVOLUTIONS = "REVOLUTIONS"
    UNITS_RPM = "RPM"
    UNITS_SECONDS = "SECONDS"
    UNITS_SERADIANS = "SERADIANS"
    UNITS_SIEMENS = "SIEMENS"
    UNITS_SIEVERTS = "SIEVERTS"
    UNITS_UFARADS = "UFARADS"
    UNITS_UNCORRECTABLE_ERRORS = "UNCORRECTABLE_ERRORS"
    UNITS_UNDERRUNS = "UNDERRUNS"
    UNITS_UNSPECIFIED = "UNSPECIFIED"
    UNITS_USECONDS = "USECONDS"
    UNITS_VA = "VA"
    UNITS_VOLTS = "VOLTS"
    UNITS_WATTS = "WATTS"
    UNITS_WEEK = "WEEK"
    UNITS_WORDS = "WORDS"
    UNITS_RESERVED1 = "reserved1"


class ApeSdr(ManagedObject):
    """This is ApeSdr class."""

    consts = ApeSdrConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ApeSdr", "apeSdr", "sdr-[id]", VersionMeta.Version101e, "InputOutput", 0x1fffffL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "entity_type": MoPropertyMeta("entity_type", "entityType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["ADD_IN_CARD", "BACK_PANEL_BOARD", "BATTERY", "BIOS", "CABLE_INTERCONNECT", "CHASSIS_BACK_PANEL_BOARD", "CMC", "CONNECTIVITY_SWITCH", "COOLING_UNIT", "DEVICE_BAY", "DISK", "DISK_DRIVE_BAY", "DRIVE_BACKPLANE", "EXTERNAL_ENVIRONMENT", "FAN_COOLING", "FRONT_PANEL_BOARD", "GROUP", "IBMC", "IO_MODULE", "IPMI_CHANNEL", "MEMORY_DEVICE", "MEMORY_MODULE", "MGMT_CONTROLLER_FIRMWARE", "OPERATING_SYSTEM", "OTHER", "OTHER_CHASSIS_BOARD", "OTHER_SYSTEM_BOARD", "PCI_BUS", "PCI_EXPRESS_BUS", "PERIPHERAL", "PERIPHERAL_BAY", "POWER_MANAGEMENT_BOARD", "POWER_MODULE", "POWER_SUPPLY", "POWER_SYSTEM_BOARD", "POWER_UNIT", "PROCESSING_BLADE", "PROCESSOR", "PROCESSOR_BOARD", "PROCESSOR_FRONT_SIDE_BUS", "PROCESSOR_IO_MODULE", "PROCESSOR_MEMORY_MODULE", "PROCESSOR_MODULE", "REMOTE_MGMT_COMM_DEVICE", "SATA_SAS_BUS", "SCSI_BUS", "SUB_CHASSIS", "SYSTEM_BOARD", "SYSTEM_BUS", "SYSTEM_CHASSIS", "SYSTEM_INTERNAL_EXPANSION_BOARD", "SYSTEM_MANAGEMENT_MODULE", "SYSTEM_MANAGEMENT_SOFTWARE", "UNKNOWN", "UNSPECIFIED"], []), 
        "event_reading_type": MoPropertyMeta("event_reading_type", "eventReadingType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["DISCRETE_ACPI_POWER", "DISCRETE_AVAILABILITY", "DISCRETE_DEVICE_ENABLE", "DISCRETE_DEVICE_PRESENCE", "DISCRETE_LIMIT_EXCEEDED", "DISCRETE_PERFORMANCE_MET", "DISCRETE_PREDICTIVE_FAILURE", "DISCRETE_REDUNDANCY", "DISCRETE_SEVERITY", "DISCRETE_STATE", "DISCRETE_USAGE", "OEM1", "SENSOR_SPECIFIC", "THRESHOLD", "UNKNOWN"], []), 
        "hysterisis_down": MoPropertyMeta("hysterisis_down", "hysterisisDown", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], []), 
        "hysterisis_up": MoPropertyMeta("hysterisis_up", "hysterisisUp", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, None, [], []), 
        "instance": MoPropertyMeta("instance", "instance", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sensor_id": MoPropertyMeta("sensor_id", "sensorId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "sensor_type": MoPropertyMeta("sensor_type", "sensorType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["ADD_IN_CARD", "BATTERY", "BOOT_ERROR", "BUTTON", "CABLE_INTERCONNECT", "CHASSIS", "CHIP_SET", "COOLING_DEVICE", "CRITICAL_INTERRUPT", "CURRENT", "DRIVE_SLOT", "ENTITY_PRESENCE", "EVENT_LOGGING_DISABLED", "FAN", "FRU_STATE", "LAN", "MANAGEMENT_SUBSYSTEM_HEALTH", "MEMORY", "MICROCONTROLLER_COPROCESSOR", "MODULE_BOARD", "MONITOR_ASIC_IC", "OEM1", "OEM2", "OEM3", "OEM4", "OEM5", "OEM7", "OS_BOOT", "OS_CRITICAL_STOP", "OTHER_FRU", "OTHER_UNITS_BASED_SENSOR", "PHYSICAL_SECURITY", "PLATFORM_ALERT", "PLATFORM_SECURITY", "POWER_MEMORY_RESIZE", "POWER_SUPPLY", "POWER_UNIT", "PROCESSOR", "SESSION_AUDIT", "SLOT_CONNECTOR", "SYSTEM_ACPI_POWER_STATE", "SYSTEM_BOOT_INITIATED", "SYSTEM_EVENT", "SYSTEM_FIRMWARE_PROGRESS", "TEMPERATURE", "TERMINATOR", "UNKNOWN", "VERSION_CHANGE", "VOLTAGE", "WATCHDOG_1", "WATCHDOG_2"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "threshold_lc": MoPropertyMeta("threshold_lc", "thresholdLc", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], []), 
        "threshold_lnc": MoPropertyMeta("threshold_lnc", "thresholdLnc", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], []), 
        "threshold_lnr": MoPropertyMeta("threshold_lnr", "thresholdLnr", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], []), 
        "threshold_uc": MoPropertyMeta("threshold_uc", "thresholdUc", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, [], []), 
        "threshold_unc": MoPropertyMeta("threshold_unc", "thresholdUnc", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, None, [], []), 
        "threshold_unr": MoPropertyMeta("threshold_unr", "thresholdUnr", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, None, [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80000L, None, None, None, ["COMPACT_SENSOR_RECORD", "FULL_SENSOR_RECORD", "UNKNOWN_RECORD"], []), 
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100000L, None, None, None, ["AMPS", "BECQUERELS", "BITS", "BYTES", "CANDELA", "CENTIMETERS", "CFM", "CHARACTERS", "COLLISIONS", "COLOR_TEMP_DEG_K", "CORRECTABLE_ERRORS", "COULOMBS", "CUBIC_CENTIMETERS", "CUBIC_FEET", "CUBIC_INCHS", "CUBIC_METERS", "CYCLES", "DAY", "DECIBELS", "DEGREES_C", "DEGREES_F", "DEGREES_K", "DWORDS", "DbA", "DbC", "ERRORS", "FARADS", "FATAL_ERRORS", "FEET", "FL_OZ", "FOOT_POUNDS", "GAUSS", "GBITS", "GBYTES", "GILBERTS", "GRAMS", "GRAVITIES", "GRAYS", "HENRIES", "HITS", "HOUR", "HZ", "INCHES", "JOULES", "KBITS", "KBYTES", "KPA", "LINES", "LITERS", "LUMENS", "LUX", "MBITS", "MBYTES", "MESSAGES", "METERS", "MHENRIES", "MIL", "MILLIMETERS", "MINUTE", "MISSES", "MOLES", "MSECONDS", "NEWTONS", "NITS", "OHMS", "OUNCES", "OUNCE_INCHES", "OVERRUNS", "PACKETS", "POUNDS", "PPM", "PSI", "QWORDS", "RADIANS", "RESETS", "RETRIES", "REVOLUTIONS", "RPM", "SECONDS", "SERADIANS", "SIEMENS", "SIEVERTS", "UFARADS", "UNCORRECTABLE_ERRORS", "UNDERRUNS", "UNSPECIFIED", "USECONDS", "VA", "VOLTS", "WATTS", "WEEK", "WORDS", "reserved1"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "entityType": "entity_type", 
        "eventReadingType": "event_reading_type", 
        "hysterisisDown": "hysterisis_down", 
        "hysterisisUp": "hysterisis_up", 
        "id": "id", 
        "instance": "instance", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sensorId": "sensor_id", 
        "sensorType": "sensor_type", 
        "status": "status", 
        "thresholdLc": "threshold_lc", 
        "thresholdLnc": "threshold_lnc", 
        "thresholdLnr": "threshold_lnr", 
        "thresholdUc": "threshold_uc", 
        "thresholdUnc": "threshold_unc", 
        "thresholdUnr": "threshold_unr", 
        "type": "type", 
        "units": "units", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.entity_type = None
        self.event_reading_type = None
        self.hysterisis_down = None
        self.hysterisis_up = None
        self.instance = None
        self.name = None
        self.sacl = None
        self.sensor_id = None
        self.sensor_type = None
        self.status = None
        self.threshold_lc = None
        self.threshold_lnc = None
        self.threshold_lnr = None
        self.threshold_uc = None
        self.threshold_unc = None
        self.threshold_unr = None
        self.type = None
        self.units = None

        ManagedObject.__init__(self, "ApeSdr", parent_mo_or_dn, **kwargs)
