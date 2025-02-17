# flake8: noqa: E501

from lazyllm.tools.rag.parser import SentenceSplitter
from lazyllm.tools.rag.store import DocNode, MetadataMode


class TestSentenceSplitter:
    def setup_method(self):
        """Setup for tests: initialize the SentenceSplitter."""
        self.splitter = SentenceSplitter(chunk_size=30, chunk_overlap=10)

    def test_forward(self):
        text = """ Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.
        """
        docs = [DocNode(text=text)]

        result = self.splitter.forward(docs)
        result_texts = [n.get_content(metadata_mode=MetadataMode.NONE) for n in result]
        expected_texts = [
            "Before college the two main things I worked on, outside of school, were writing and programming.I didn't write essays.",
            "I didn't write essays.I wrote what beginning writers were supposed to write then, and probably still are: short stories.My stories were awful.",
            "My stories were awful.They had hardly any plot, just characters with strong feelings, which I imagined made them deep.",
        ]
        assert (
            result_texts == expected_texts
        ), f"Expected {expected_texts}, but got {result_texts}"
