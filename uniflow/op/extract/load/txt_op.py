"""Extract txt op."""

import copy
import re
from typing import Sequence

from uniflow.node import Node
from uniflow.op.op import Op


class ExtractTxtOp(Op):
    """Extract txt Op Class."""

    def __call__(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Op.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        output_nodes = []
        for node in nodes:
            value_dict = copy.deepcopy(node.value_dict)
            with open(
                value_dict["filename"],
                "r",
                encoding=value_dict.get("encoding", "utf-8"),
            ) as f:
                text = f.read()
            output_nodes.append(
                Node(
                    name=self.unique_name(),
                    value_dict={"text": text},
                    prev_nodes=[node],
                )
            )
        return output_nodes


class ProcessTxtOp(Op):
    """Process txt Op Class."""

    def __call__(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Op.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        output_nodes = []
        for node in nodes:
            value_dict = copy.deepcopy(node.value_dict)
            text = value_dict["text"]
            text = re.split(r"\s*\n\s*", text.strip())
            output_nodes.append(
                Node(
                    name=self.unique_name(),
                    value_dict={"text": text},
                    prev_nodes=[node],
                )
            )
        return output_nodes
