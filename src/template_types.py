from enum import Enum

class OutputTemplateType(str, Enum):
    ARCHITECTURE_NOTE = "architecture-note"
    ONE_PAGER = "one-pager"
    TWO_PAGER = "two-pager"
    BENCHMARKING = "benchmarking"
    BUY_SIDE_GAP_ANALYSIS = "buy-side-gap-analysis"
    DIAGNOSTIC_RECO_SELL_SIDE = "diagnostic-reco-sellside"
    OPPORTUNITY_NOTE_ICP = "opportunity-note-icp"

class TemplateLifecycle(str, Enum):
    CANDIDATE = "candidate"
    VALIDATED = "validated"
    PROMOTED = "promoted"
    RETIRED = "retired"

class GenerationMode(str, Enum):
    FROM_SCRATCH = "from-scratch"
    ITERATIVE = "iterative"
    FEEDBACK_DREAMING = "feedback-dreaming"
    RETRO_ENGINEERING = "retro-engineering"
