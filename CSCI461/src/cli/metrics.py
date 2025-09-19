from __future__ import annotations
import time
from typing import Any, Dict, Tuple

def _timed(fn, *args, **kwargs) -> Tuple[float, int]:
    t0 = time.perf_counter()
    v = float(fn(*args, **kwargs))
    t1 = time.perf_counter()
    return v, int(round((t1 - t0) * 1000))

def ramp_up_time(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.8)

def bus_factor(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.5)

def performance_claims(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.6)

def license_score(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.7)

def size_score(ctx: Dict[str, Any]) -> Tuple[Dict[str, float], int]:
    t0 = time.perf_counter()
    val = {
        "raspberry_pi": 0.6,
        "jetson_nano": 0.8,
        "desktop_pc": 1.0,
        "aws_server": 1.0,
    }
    t1 = time.perf_counter()
    return val, int(round((t1 - t0) * 1000))

def dataset_and_code_score(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.9)

def dataset_quality(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.7)

def code_quality(ctx: Dict[str, Any]) -> Tuple[float, int]:
    return _timed(lambda: 0.85)

def compute_all_metrics(ctx: Dict[str, Any]) -> Dict[str, Any]:
    r_ru, ms_ru = ramp_up_time(ctx)
    r_bf, ms_bf = bus_factor(ctx)
    r_pc, ms_pc = performance_claims(ctx)
    r_lic, ms_lic = license_score(ctx)
    r_sz, ms_sz = size_score(ctx)
    r_dcs, ms_dcs = dataset_and_code_score(ctx)
    r_dq, ms_dq = dataset_quality(ctx)
    r_cq, ms_cq = code_quality(ctx)

    return {
        "ramp_up_time": r_ru, "ramp_up_time_latency": ms_ru,
        "bus_factor": r_bf, "bus_factor_latency": ms_bf,
        "performance_claims": r_pc, "performance_claims_latency": ms_pc,
        "license": r_lic, "license_latency": ms_lic,
        "size_score": r_sz, "size_score_latency": ms_sz,
        "dataset_and_code_score": r_dcs, "dataset_and_code_score_latency": ms_dcs,
        "dataset_quality": r_dq, "dataset_quality_latency": ms_dq,
        "code_quality": r_cq, "code_quality_latency": ms_cq,
    }

def compute_net_score(metrics: Dict[str, Any]) -> Tuple[float, int]:
    def logic() -> float:
        w = {
            "ramp_up_time": 0.18,
            "bus_factor": 0.12,
            "performance_claims": 0.12,
            "license": 0.18,
            "dataset_and_code_score": 0.12,
            "dataset_quality": 0.14,
            "code_quality": 0.14,
        }
        return sum(w[k] * float(metrics[k]) for k in w)  # in [0,1]
    return _timed(logic)

