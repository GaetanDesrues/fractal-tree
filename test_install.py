import logging

import treefiles as tf
from MeshObject import Mesh

from FractalTree.network import PurkinjeMesh


def main():
    m = Mesh.Sphere(theta_res=5, phi_res=5)
    m = PurkinjeMesh(m.data)
    d = m.compute_distances()
    m.addPointData(d, "distances")
    m.plot(scalars="distances")
    if d[0] == 0 and d[3] > 0:
        log.info("All good !")
    else:
        log.error("Error")


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    main()