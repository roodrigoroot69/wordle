from mamba import describe, context, it, after, before
from expects import equal, expect
from unittest.mock import Mock, create_autospec

from wordle.app.wordle_play import WordlePlayProcessor

with describe(WordlePlayProcessor) as self:

    with before.all:
        self.word_repository_mock = Mock()
        WordlePlayProcessor(
            word_repository=self.word_repository_mock,
        )

    with context(''):
        with it(''):
            ...
