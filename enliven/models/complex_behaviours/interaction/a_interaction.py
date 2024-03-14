from abc import ABC, abstractmethod
from math import sqrt
from typing import Sequence

from enliven.models.bodies.interacting_bodies.a_interacting_body import AInteractingBody
from enliven.models.complex_behaviours.i_behaviour import IBehaviour
from enliven.models.quantities.position import Position
from enliven.models.quantities.vector import Vector


class AInteraction(IBehaviour, ABC):
    def work(self, entities: Sequence[AInteractingBody]) -> list[Vector]:
        forces = [Vector() for _ in range(len(entities))]

        for i in range(len(entities)):
            for j in range(len(entities)):
                if entities[i] is entities[j]:
                    continue

                forces[i] += self._calc_vect(entities[i], entities[j])

        return forces

    def _calc_vect(self, body1: AInteractingBody, body2: AInteractingBody) -> Vector:
        d_pos = body2.pos - body1.pos
        dist: float = self._calc_distance(d_pos) + 0.0000000000000000001
        vect_len: float = self._calc_vect_len(body1, body2, dist)
        cos: float = d_pos.x / dist
        sin: float = d_pos.y / dist

        return Vector(vect_len * cos, vect_len * sin)

    def _calc_distance(self, d_pos: Position) -> float:
        d_pos_sqr = d_pos * d_pos

        return sqrt(d_pos_sqr.x + d_pos_sqr.y)

    @abstractmethod
    def _calc_vect_len(
        self, body1: AInteractingBody, body2: AInteractingBody, dist: float
    ) -> float:
        pass
