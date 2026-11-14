from enum import Enum

class TemplateClass(str, Enum):
    PRODUCT = "product"
    BUSINESS = "business"
    TECH = "tech"
    PEDAGOGIQUE = "pedagogique"

class OutputTemplateType(str, Enum):
    ARCHITECTURE_NOTE = "architecture-note"
    STRATEGIC_MARKET_NOTE = "strategic-market-note"
    ONE_PAGER = "one-pager"
    BENCHMARKING = "benchmarking"
    BUY_SIDE_GAP_ANALYSIS = "buy-side-gap-analysis"
    DIAGNOSTIC_RECO_SELL_SIDE = "diagnostic-reco-sellside"
    OPPORTUNITY_NOTE_ICP = "opportunity-note-icp"
    INTEGRATION_NOTE = "integration-note"
    AI_ENTERPRISE_LEARNING_SIX_PAGE = "ai-enterprise-learning-six-page"

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
