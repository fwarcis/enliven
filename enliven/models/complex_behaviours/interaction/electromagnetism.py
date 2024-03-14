from enliven.models.bodies.interacting_bodies.a_interacting_body import AInteractingBody
from enliven.models.complex_behaviours.interaction.a_interaction import AInteraction


class Electromagnetism(AInteraction):
    def _calc_vect_len(
        self, body1: AInteractingBody, body2: AInteractingBody, dist: float
    ) -> float:
        return body1.inter_data.charge * body2.inter_data.charge / dist**2
