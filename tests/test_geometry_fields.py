import numpy as np
from coherence_simulation import geometry_fields

def test_spiral_mask_shape():
    mask = geometry_fields.spiral_mask(20)
    assert mask.shape == (20, 20)

def test_arc_mask_shape():
    mask = geometry_fields.arc_mask(15)
    assert mask.shape == (15, 15)


def test_dual_core_mask_shape():
    mask = geometry_fields.dual_core_mask(10)
    assert mask.shape == (10, 10)
