import logging

import numpy as np
import pyvista
import treefiles as tf
from MeshObject import Mesh
from MeshObject.bindvista.plotter import Plotter, Themes

from FractalTree.generator import PurkinjeGenerator
from FractalTree.network import PurkinjeNetwork


def pp(root):
    purk = PurkinjeNetwork.load(root.purk)
    pts = 2, 422
    ds = {k: purk.compute_geodesic(b=k, name=f"d_{k}", optimized=False) for k in pts}

    with Plotter(
        theme=Themes.DOC,
        title="Purkinje",
        shape=(1, 2),
        no_orientation=True,
        off_screen=True,
    ) as p:
        for i, (k, v) in enumerate(ds.items()):
            p[0, i].add_text(f"Distance from {k}")
            # Surface mesh
            p.add_mesh(Mesh.load(root.surf), show_edges=True, opacity=0.2)
            # Purkinje tubes
            p.add_mesh(purk, radius=0.3, scalars=f"d_{k}", cmap="jet_r")
            p.add_points(
                purk.point(k),
                render_points_as_spheres=True,
                point_size=10,
                color="red",
            )
        p.link_views()
        p.camera_position = [
            (441.3386549977921, 0.539158512621313, 313.91112797800054),
            (285.94983200151114, 52.388594205420354, 226.67431758527576),
            (-0.4602127457269528, 0.10419482128403948, 0.8816732205800777),
        ]
        p.render()
        p.screenshot(root / "dists.png")


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    _root = tf.f(__file__)
    _root.file(surf="endo_lv.obj", purk="purkinje_lv.vtk")

    pp(_root)
