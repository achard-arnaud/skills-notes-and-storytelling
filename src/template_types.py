from enum import Enum

class OutputTemplateType(str, Enum):
    ARCHITECTURE_NOTE = "architecture-note"
    ONE_PAGER = "one-pager"
    TWO_PAGER = "two-pager"
    BENCHMARKING = "benchmarking"
    BUY_SIDE_GAP_ANALYSIS = "buy-side-gap-analysis"

class TemplateLifecycle(str, Enum):
    CANDIDATE = "candidate"
    VALIDATED = "validated"
    PROMOTED = "promoted"
    RETIRED = "retired"
