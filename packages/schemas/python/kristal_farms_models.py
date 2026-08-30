from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from typing import Any, Literal
from uuid import UUID
from pydantic import BaseModel, Field, model_validator

class Visibility(str,Enum):
    PUBLIC='PUBLIC'; PARTNER='PARTNER'; INTERNAL='INTERNAL'; RESTRICTED='RESTRICTED'
class EntityType(str,Enum):
    place='place'; asset='asset'; project='project'; corridor='corridor'; natural_feature='natural_feature'
class EvidenceStatus(str,Enum):
    verified='verified'; supported='supported'; scoped='scoped'; unverified='unverified'; conflicting='conflicting'; unknown='unknown'
class ProjectRole(str,Enum):
    external_reference='external_reference'; kristal_candidate='kristal_candidate'; kristal_project='kristal_project'
class SourceType(str,Enum):
    user_input='user_input'; engineering_assumption='engineering_assumption'; derived='derived'; evidence='evidence'; default='default'

class Entity(BaseModel):
    id: UUID; canonical_key: str; entity_type: EntityType; name: str; status: str|None=None; visibility: Visibility=Visibility.PUBLIC; metadata: dict[str,Any]=Field(default_factory=dict)
class Source(BaseModel):
    id: UUID; source_key: str; title: str; publisher: str|None=None; source_type: str|None=None; url: str|None=None; publication_date: date|None=None; retrieved_at: date|None=None; document_reference: str|None=None; license: str|None=None; metadata: dict[str,Any]=Field(default_factory=dict)
class Evidence(BaseModel):
    id: UUID; evidence_key: str; evidence_type: str; claim: str; status: EvidenceStatus; confidence: str|None=None; valid_from: date|None=None; valid_to: date|None=None; observed_at: datetime|None=None; published_at: datetime|None=None; retrieved_at: date|None=None; metadata: dict[str,Any]=Field(default_factory=dict)
class Observation(BaseModel):
    id: UUID; subject_id: UUID; metric: str; value_numeric: float|None=None; value_text: str|None=None; unit: str|None=None; valid_from: date|None=None; valid_to: date|None=None; observed_at: datetime|None=None; source_evidence_id: UUID|None=None; derivation_type: SourceType; metadata: dict[str,Any]=Field(default_factory=dict)
    @model_validator(mode='after')
    def one_value(self):
        if self.value_numeric is None and self.value_text is None: raise ValueError('observation requires numeric or text value')
        return self
class ScreeningDimensionState(BaseModel):
    id: UUID; entity_id: UUID; dimension: Literal['energy','hydrology','environment','rights_governance','telecom','logistics','community','regulation','economics','engineering']; status: str; evidence_completeness: str|None=None; open_questions: list[str]=Field(default_factory=list); last_reviewed: date|None=None; metadata: dict[str,Any]=Field(default_factory=dict)
    @model_validator(mode='after')
    def no_ranking(self):
        forbidden={'rank','score','priority_score','suitability_score'}
        if forbidden.intersection(self.metadata): raise ValueError('ranking metadata forbidden in unranked screening')
        return self


class ObservationSeries(BaseModel):
    id: UUID; subject_id: UUID; metric: str; unit: str|None=None; source_id: UUID; source_release: str|None=None; collection_key: str
    record_start: date|None=None; record_end: date|None=None; row_count: int=0; valid_value_count: int=0; provisional_value_count: int=0
    raw_artifact_uri: str|None=None; raw_sha256: str|None=None; retrieved_at: datetime|None=None
    status: Literal['materialized','partial','superseded','invalid','not_materialized']; metadata: dict[str,Any]=Field(default_factory=dict)
    @model_validator(mode='after')
    def materialized_has_rows(self):
        if self.status=='materialized' and self.row_count<=0: raise ValueError('materialized observation series requires rows')
        if self.valid_value_count>self.row_count: raise ValueError('valid count exceeds row count')
        return self

class ObservationDerivation(BaseModel):
    observation_id: UUID; algorithm_key: str; algorithm_version: str; source_series_ids: list[UUID]
    coverage_start: date|None=None; coverage_end: date|None=None; raw_value_count: int; completeness_fraction: float|None=None
    parameters: dict[str,Any]=Field(default_factory=dict); metadata: dict[str,Any]=Field(default_factory=dict)
    @model_validator(mode='after')
    def provenance_required(self):
        if self.raw_value_count<=0: raise ValueError('derived observation requires source values')
        if not self.source_series_ids: raise ValueError('derived observation requires source series')
        if self.completeness_fraction is not None and not 0<=self.completeness_fraction<=1: raise ValueError('invalid completeness fraction')
        return self
